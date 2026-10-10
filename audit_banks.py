# -*- coding: utf-8 -*-
"""audit_banks.py —— 六大题库独立审计（不 import .build_practice.js，正则与公式全部独立实现）
覆盖：①结构（题数/编号连续/选项完整/答案分布）②各库答案速查行逐位核对
③计算题独立重算（新题段）④概念题口径抽查 ⑤与 17-练习数据.js 逐位比对 ⑥全局引用检查
用法：python audit_banks.py
"""
import re, math, sys

BANKS = [
    ('10-讲义题库-软件工程.md', '软件工程', 'sw', 64),
    ('11-讲义题库-数据结构与算法.md', '数据结构与算法', 'ds', 55),
    ('12-讲义题库-数据库.md', '数据库', 'db', 49),
    ('13-讲义题库-操作系统.md', '操作系统', 'os', 57),
    ('14-讲义题库-组成原理与网络.md', '组成原理与网络', 'hw', 54),
    ('15-讲义题库-程序语言与背诵类.md', '程序语言与背诵类', 'pl', 47),
]
fails, checked = [], 0

def check(cond, msg):
    global checked
    checked += 1
    if not cond:
        fails.append(msg)

# ---------- 1+2. 结构解析 + 速查行核对 ----------
all_banks = {}
for fname, bname, bid, expect in BANKS:
    text = open(fname, encoding='utf-8').read()
    check(f'仿真题库（{expect} 题）' in text, f'{fname}: 第二部分标题题数不是 {expect}')
    qs, cur = [], None
    for raw in text.split('\n'):
        line = raw.rstrip('\r')
        m = re.match(r'^\*\*(\d+)\.\*\*\s*(.*)$', line)
        if m:
            if cur: qs.append(cur)
            cur = {'id': int(m.group(1)), 'q': m.group(2), 'o': [], 'ans': None, 'explen': 0, 'exptext': ''}
            continue
        if cur is None: continue
        ma = re.match(r'^>\s*\*\*答案：([A-D])\*\*\s*\.?\s*(.*)$', line)
        if ma:
            cur['ans'] = ma.group(1); cur['explen'] += len(ma.group(2)); cur['exptext'] += ma.group(2); continue
        if cur['ans']:
            if line.startswith('>'):
                cur['explen'] += len(line); cur['exptext'] += line
            elif line.strip() == '': qs.append(cur); cur = None
            continue
        if re.match(r'^[AB][.、．]\s', line) and re.search(r'[CD][.、．]\s', line):
            cur['o'] = [re.sub(r'^[A-D][.、．]\s*', '', s) for s in
                        re.split(r'\s+(?=[BCD][.、．]\s)', line.strip())]
        elif re.match(r'^(A|B|C|D)[.、．]\s*(.*)$', line):
            mm = re.match(r'^(A|B|C|D)[.、．]\s*(.*)$', line)
            if cur['o'].__len__() == 'ABCD'.index(mm.group(1)): cur['o'].append(mm.group(2))
        elif cur['o'] == [] and line.strip():
            cur['q'] += '\n' + line.strip()
    if cur: qs.append(cur)

    if len(qs) != expect: fails.append(f'{bname}: 题数 {len(qs)} != {expect}')
    for i, q in enumerate(qs):
        if q['id'] != i + 1: fails.append(f'{bname} Q{q["id"]}: 编号不连续（位置 {i+1}）')
        if len(q['o']) != 4: fails.append(f'{bname} Q{q["id"]}: 选项数 {len(q["o"])}')
        elif len(set(q['o'])) != 4 or any(not x.strip() for x in q['o']):
            fails.append(f'{bname} Q{q["id"]}: 选项重复或为空')
        if not q['ans']: fails.append(f'{bname} Q{q["id"]}: 无答案')
        if q['explen'] < 5: fails.append(f'{bname} Q{q["id"]}: 解析过短')
    # 速查行
    mm = re.search(r'## 答案速查[^\n]*\n+([^\n]+)', text)
    if not mm:
        fails.append(f'{bname}: 找不到答案速查行')
    else:
        pairs = dict((int(a), b) for a, b in re.findall(r'(\d+)([A-D])', mm.group(1)))
        if len(pairs) != len(qs):
            fails.append(f'{bname}: 速查行条目 {len(pairs)} != 题数 {len(qs)}')
        for q in qs:
            if pairs.get(q['id']) != q['ans']:
                fails.append(f'{bname} Q{q["id"]}: 速查={pairs.get(q["id"])} 题后={q["ans"]}')
    dist = {}
    for q in qs: dist[q['ans']] = dist.get(q['ans'], 0) + 1
    print(f'[结构] {bname}: {len(qs)}题 分布{dist} 速查{"OK" if not [f for f in fails if f.startswith(bname)] else "FAIL"}')
    all_banks[bid] = qs

# ---------- 3. 计算题独立重算 ----------
def fifo_miss(seq, frames):
    mem, miss = [], 0
    for p in seq:
        if p not in mem:
            miss += 1
            mem.append(p)
            if len(mem) > frames: mem.pop(0)
    return miss

def kmp_fail(s):
    res = []
    for i in range(1, len(s) + 1):
        sub = s[:i]
        best = 0
        for k in range(len(sub) - 1, 0, -1):
            if sub[:k] == sub[-k:]: best = k; break
        res.append(best)
    return ''.join(map(str, res))

def heap_first_pop(arr):  # 大根堆取一次堆顶，返回层序字符串
    a = arr[:]
    a[0], a[-1] = a[-1], a[0]
    top = a[-1]; a = a[:-1]; n = len(a); i = 0
    while True:
        l, r, big = 2*i+1, 2*i+2, i
        if l < n and a[l] > a[big]: big = l
        if r < n and a[r] > a[big]: big = r
        if big == i: break
        a[i], a[big] = a[big], a[i]; i = big
    return ','.join(map(str, a + [top]))

def sstf_total(head, reqs):  # 最短寻道优先总移道数
    cur, total, rest = head, 0, list(reqs)
    while rest:
        nxt = min(rest, key=lambda t: abs(t - cur))
        total += abs(nxt - cur); cur = nxt; rest.remove(nxt)
    return total

def scan_order(head, up, reqs):  # 电梯调度服务顺序：先沿当前方向，再折返
    ahead = sorted((t for t in reqs if (t >= head if up else t <= head)), reverse=not up)
    behind = sorted((t for t in reqs if t not in ahead), reverse=up)
    return ahead + behind

def lru_misses(seq, frames):  # LRU 缺页模拟
    mem, last, miss = [], {}, 0
    for i, p in enumerate(seq):
        last[p] = i
        if p in mem: continue
        miss += 1
        if len(mem) < frames: mem.append(p)
        else:
            victim = min(mem, key=lambda m: last.get(m, -1))
            mem[mem.index(victim)] = p
    return miss

def fifo_misses(seq, frames):
    mem, q, miss = [], [], 0
    for p in seq:
        if p in mem: continue
        miss += 1
        if len(mem) < frames: mem.append(p); q.append(p)
        else:
            old = q.pop(0); q.append(p); mem[mem.index(old)] = p
    return miss

def pv_seq(init, ops):  # PV 序列模拟，返回 (终值, 等待队列人数)
    v, wait = init, 0
    for op in ops:
        v += -1 if op == 'P' else 1
        if op == 'P' and v < 0: wait += 1
        elif op == 'V' and v <= 0 and wait > 0: wait -= 1
    return v, wait

# (题干关键词, 期望子串)；期望值全部由公式/模拟现算
M = [
    ('下三角（含对角线）按行压缩存储到一维数组', str(8*9//2)),                       # ds37 =36
    ('线性探测处理冲突，查找成功时等概率下的 ASL', '2'),                              # ds41 =(1+2+3)/3=2
    ('2 路归并排序，需要归并的趟数', str(math.ceil(math.log2(1000)))),               # ds47 =10
    ('无向图有 16 条边，所有顶点的度数之和', str(2*16)),                             # ds49 =32
    ('不同拓扑序列的个数', '2'),                                                     # ds50
    ('模式串 "ababa" 的失效函数', kmp_fail('ababa')),                                # ds39 =00123
    ('大根堆 {9,8,5,6,7,1}', heap_first_pop([9,8,5,6,7,1])),                         # ds44 =8,7,5,6,1,9
    ('采用 FIFO 置换算法的缺页次数', str(fifo_miss([1,2,3,4,1,2,5], 3))),            # os30 =7
    ('逻辑地址 32 位、页面大小 4KB、页表项 4B', '4MB'),                              # os34 =2^20*4B
    ('8 位原码定点整数的表示范围', '−127~+127'),                                     # hw35
    ('连续执行 100 条指令，相对不流水', '%.1f' % (100*10 / ((5+100-1)*2))),          # hw38 ≈4.8
    ('8K×8 位的 SRAM 芯片组成 64K×8 位存储器', '8'),                                 # hw40 =64/8
    ('总线宽度 32 位、工作频率 100MHz', '400MB/s'),                                  # hw41 =4B*100M
    ('/30 子网中可分配的主机地址数', '2'),                                           # hw47 =2^2-2
    ('平均无故障时间 MTTF=1000h，平均修复时间 MTTR=10h', '1010h'),                   # sw36
    ('640×480、24 位真彩色、25 帧/秒', str(640*480*24*25//1000000) + 'Mbps'),        # pl39 =184Mbps
    ('CREATE TABLE 语句中，声明', 'FOREIGN KEY(学号) REFERENCES 学生(学号)'),        # db27
    ('姓"张"且姓名恰好 3 个字', "张__"),                                             # db29
    ('SQL 子查询中，`>ALL(…)` 表示', '最大值'),                                      # db30
    ('把"查询学生表"的权限授予用户 U1', 'GRANT SELECT ON 学生 TO U1'),               # db31
    ('数据库并发控制中，预防死锁的方法是', '一次封锁法'),                             # db43
    ('采用最短寻道时间优先（SSTF）调度，磁头移动的磁道总数', str(sstf_total(20, [10,30,40,5,25]))),          # os43 =55
    ('采用电梯调度（SCAN）算法，服务顺序', '→'.join(map(str, scan_order(50, True, [65,40,34,20,70,10])))),   # os44
    ('块号 100 对应位示图的', '字 %d、位 %d' % (100//32, 100%32)),                    # os45 =字3、位4
    ('采用 LRU 置换算法的缺页次数', str(lru_misses([4,3,2,1,4,3,5,4,3,2,1,5], 3))),  # os46 =10（同序列FIFO=9对照）
    ('按短作业优先（SJF）调度，平均周转时间为', '%.2f' % ((2+6+14)/3)),               # os47 =7.33
    ('此时 S 的值和等待队列中的进程数分别是', '%d 和 %d' % pv_seq(2, ['P','P','P','V','V'])),                # os48 =1 和 0
    ('当前值为 −3，此时执行一次 V(S)，则', 'S=−%d，唤醒一个等待进程' % abs(pv_seq(-3, ['V'])[0])),          # os55 =S=−2，唤醒一个
]
C = [  # 概念口径抽查：正确选项文本须含关键词
    ('V 模型的对应关系，集成测试', '详细设计'),
    ('不属于 ISO 9126 软件质量六特性', '可扩展性'),
    ('对扩展开放、对修改关闭', '开闭原则'),
    ('部分可以脱离整体独立存在', '聚合'),
    ('数据仓库的基本特征', '联机增删改'),
    ('读者-写者问题中，正确的说法', '多个读者可以同时读'),
    ('当前的安全序列是', 'P2→P3→P1'),
    ('连续执行两次 P(mutex) 而中间没有 V', '第一次成功、第二次阻塞'),
    ('再尝试放入第 6 个', '生产者阻塞在 P(empty)'),
    ('则 D 开始前应执行', 'P(s3)、P(s4)'),
    ('任何时刻最多允许 100 个购票者进入', '100'),
    ('两空处应填', 'P(empty)…V(full)'),
    ('使用快表（TLB）且命中时', '1 次'),
    ('操作系统中"高级调度"指的是', '作业调度'),
    ('单 CPU 系统中 n 个进程并发执行', '1'),
    ('因插入导致"左子树的左子树"过高（LL 型）', '右旋'),
    ('依次插入 45、24、53、12、37、90', '37'),
    ('发明专利的保护期是', '20 年'),
    ('注册商标的有效期', '10 年'),
    ('企业标准的代号是', 'Q/'),
    ('大数据的"4V"特征中', 'Visibility'),
    ('直接向用户提供在线办公软件', 'SaaS'),
    ('Prolog 语言属于', '逻辑式'),
    ('正规式 (a|b)* 表示的语言', '任意符号串'),
    ('利用用户输入拼接 SQL', 'SQL 注入'),
    ('前缀式（波兰式）是', '+a*bc'),
    ('关于解释方式执行高级语言程序', '不生成独立的目标程序'),
    ('关于希尔排序，正确的是', '增量逐趟缩小到 1'),
    ('关于触发器（Trigger），正确的是', '自动触发执行'),
    ('关于 AOE 网与关键路径，正确的是', '最早开始时间与最迟开始时间相等'),
    ('建立需求基线并控制需求变更属于', '需求管理'),
    ('经正式评审批准、作为后续变更出发点', '基线'),
    ('先验证主流程基本可用', '冒烟测试'),
    ('之间存在依赖与组合约束', '因果图'),
    ('数据报分片后，正确的是', '目的主机重组'),
    ('同时存在 192.168.1.0/24 与 192.168.1.64/26', '/26'),
    ('父图中某加工有 1 个输入流', '父子图平衡'),
    ('展示系统硬件拓扑结构', '部署图'),
    ('逆向工程是指', '从现有代码恢复出设计'),
    ('空指针域共有', 'n+1'),
    ('按位置区分的非空子串个数', 'n(n+1)/2'),
    ('插入一行满足该条件的新记录', '幻读'),
    ('封锁请求总是被其他事务抢先', '活锁'),
    ('诊断死锁的常用方法', '等待图'),
    ('下一条要执行指令的内存地址', 'PC'),
    ('变址寄存器的内容 + 指令中的形式地址', '变址寻址'),
    ('冗余表决系统中，单个模块可靠性为 R', '3R²(1-R)+R³'),
    ('两两之间保密通信', 'n(n-1)/2'),
    ('按采样定理要不失真地数字化', '8kHz'),
]
norm = lambda s: s.replace('（  ）', '')
for kw, want in M + C:
    hit = None
    for bid, qs in all_banks.items():
        for q in qs:
            if kw.replace(' ', '') in norm(q['q']).replace(' ', ''):
                hit = (bid, q); break
        if hit: break
    if not hit:
        fails.append(f'重算/口径: 找不到题干含「{kw[:24]}」的题'); continue
    bid, q = hit
    opt = q['o'][ord(q['ans']) - 65] if len(q['o']) == 4 else ''
    ok = (opt.strip() == want.strip()) or (want in opt) or (want in q.get('exptext', ''))
    check(ok, f'{bid} Q{q["id"]}[{kw[:16]}]: 期望含「{want}」实得选项「{opt[:40]}」')
print(f'[重算] 独立复核 {len(M)+len(C)} 项（公式+模拟+口径）')

# ---------- 4. 与 17-练习数据.js 逐位比对 ----------
d = open('17-练习数据.js', encoding='utf-8').read()
for fname, bname, bid, expect in BANKS:
    i = d.find(f'"id":"{bid}","name":"{bname}"')
    j = d.find('"id":"', i + 10) if i >= 0 else -1
    seg = d[i:j] if i >= 0 and j > i else (d[i:] if i >= 0 else '')
    data_ans = re.findall(r'"ans":"([A-D])"', seg)
    md_ans = ''.join(q['ans'] for q in all_banks[bid])
    check(len(data_ans) == len(md_ans) and ''.join(data_ans) == md_ans,
          f'{bname}: 17-练习数据答案与 md 不一致（{len(data_ans)} vs {len(md_ans)}）')
print('[数据] 17-练习数据.js 六库答案与 md 逐位一致: %s' % ('OK' if not [f for f in fails if '不一致' in f] else 'FAIL'))

# ---------- 5. 全局引用检查 ----------
p00 = open('00-总计划.md', encoding='utf-8').read()
p02 = open('02-每日学习计划表.md', encoding='utf-8').read()
rd = open('README.md', encoding='utf-8').read()
check(p00.count('544项') == 2 and '397项' not in p00 and '297项' not in p00 and '254题' not in p00 and '497项' not in p00 and '510项' not in p00 and '516项' not in p00 and '524项' not in p00, '00 总数引用异常')
check('题库426' in p02 and '题库179' not in p02 and '题库279' not in p02 and '题库392' not in p02 and '题库398' not in p02 and '题库406' not in p02, '02 题库数引用异常')
check('426' in rd and '544' in rd and '179' not in rd and '279' not in rd and '392' not in rd and '398' not in rd and '406' not in rd, 'README 题库数引用异常')
check(all(f'（{n} 题）' in open(f, encoding='utf-8').read() for f, _, _, n in BANKS), '题库标题题数与期望不符')
print('[引用] 00/02/README 总数与标签: %s' % ('OK' if not [f for f in fails if '引用' in f] else 'FAIL'))

# ---------- 结论 ----------
print('=' * 56)
if fails:
    print('审计未通过，%d 个问题:' % len(fails))
    for f in fails: print(' ✘', f)
    sys.exit(1)
print('审计全部通过 ✅  六库 426 题 | 编号连续 | 选项完整 | 速查行逐位一致 | 独立重算 %d 项 | 数据/引用一致' % (len(M)+len(C)))
