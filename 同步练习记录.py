# -*- coding: utf-8 -*-
"""
同步练习记录（两地做题同步工具）
用法：python 同步练习记录.py
流程：拉取 GitHub 上的练习记录 → 与本地按"每题时间新者胜"合并 → 写回本地 → 推送仓库
建议：每天做完题跑一次；换机器前跑一次；做题前跑一次（先拿到另一台机器的进度）。
注意：跑之前最好关掉 17 系统页面（避免页面缓存的旧数据随后覆盖）。
"""
import json, os, subprocess, sys, shutil, tempfile

DIR = os.path.dirname(os.path.abspath(__file__))
LOCAL = os.path.join(DIR, '软考-练习记录.json')
REPO = 'git@github.com:szLyk/ruankao_mid.git'
NAME = '软考-练习记录.json'

def load(p):
    try:
        d = json.load(open(p, encoding='utf-8'))
        return d if isinstance(d, dict) and isinstance(d.get('answers'), dict) else None
    except Exception:
        return None

def merge(a, b):
    """b(远端) 合并进 a(本地)。规则与 17 系统 mergeFromFile 一致：
    每题按 lastTs 新者胜；history 按 (t,k,c,ok) 去重合并；daily 按天取大。返回 (a, changed)"""
    if not b: return a, False
    ch = False
    for k, f in b.get('answers', {}).items():
        l = a['answers'].get(k)
        if not l:
            a['answers'][k] = f; ch = True; continue
        ft, lt = f.get('lastTs', ''), l.get('lastTs', '')
        if ft > lt or (ft == lt and f.get('attempts', 0) > l.get('attempts', 0)):
            a['answers'][k] = f; ch = True
    seen, all_h = set(), []
    for h in (b.get('history') or []) + (a.get('history') or []):
        key = (h.get('t'), h.get('k'), h.get('c'), h.get('ok'))
        if key not in seen:
            seen.add(key); all_h.append(h)
    all_h.sort(key=lambda x: x.get('t', ''))
    if len(all_h) != len(a.get('history') or []): ch = True
    a['history'] = all_h[-3000:]
    for day, f in (b.get('daily') or {}).items():
        l = a.get('daily', {}).get(day)
        if not l:
            a.setdefault('daily', {})[day] = f; ch = True; continue
        done = max(f.get('done', 0), l.get('done', 0))
        m = {'done': done, 'ok': min(max(f.get('ok', 0), l.get('ok', 0)), done)}
        if m != l: a['daily'][day] = m; ch = True
    a['seeded'] = bool(a.get('seeded') or b.get('seeded'))
    la, lb = a.get('lastUpdated', ''), b.get('lastUpdated', '')
    if lb > la: a['lastUpdated'] = lb
    return a, ch

def git(*args):
    env = dict(os.environ, GIT_SSH_COMMAND='ssh -o BatchMode=yes')
    return subprocess.run(['git'] + list(args), capture_output=True, text=True, env=env)

def main():
    local = load(LOCAL) or {'app': 'rk-practice-v1', 'seeded': False, 'answers': {}, 'history': [], 'daily': {}}

    tmp = tempfile.mkdtemp(prefix='rk_sync_')
    try:
        r = git('clone', '--depth', '1', REPO, tmp)
        if r.returncode != 0:
            print('克隆仓库失败：', r.stderr.strip()[:200]); sys.exit(1)
        remote = load(os.path.join(tmp, NAME))

        merged, changed_local = merge(local, remote)
        json.dump(merged, open(LOCAL, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

        n_ans = len(merged.get('answers', {}))
        days = merged.get('daily', {})
        total_done = sum(v.get('done', 0) for v in days.values())
        print(f"合并完成：本地+远端共 {n_ans} 道作答记录，{len(days)} 天，累计 {total_done} 次作答")

        shutil.copy(LOCAL, os.path.join(tmp, NAME))
        git('-C', tmp, 'add', NAME)
        r2 = git('-C', tmp, '-c', 'user.name=sync-script', '-c', 'user.email=sync@local',
                 'commit', '-m', f"sync: 练习记录 {n_ans} 题作答（{os.environ.get('COMPUTERNAME','this-pc')}）")
        if r2.returncode != 0:
            print('远端记录与本地一致，无需推送。'); return
        r3 = git('-C', tmp, 'push', 'origin', 'master')
        if r3.returncode != 0:
            print('推送失败：', r3.stderr.strip()[:200]); sys.exit(1)
        print('已推送到 GitHub ✅（另一台机器：git pull 后打开 17 系统绑定该 json，或再跑一次本脚本）')
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

if __name__ == '__main__':
    main()
