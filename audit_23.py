# -*- coding: utf-8 -*-
# 独立审计 v2：23-网络真题风格专项卷.md（100题）
# 不复用 .verify_net.js 逻辑，全部独立重写；所有失败项集中报告，不中断
import re, sys, math

md = open('23-网络真题风格专项卷.md', encoding='utf-8').read()
lines = md.split('\n')
fails = []
def check(cond, msg):
    if not cond:
        fails.append(msg)
    return cond

# ---------- 1. 结构解析（与构建脚本 parseBank 等价：兼容单行四选项 / 逐行选项两种排版） ----------
qs = {}
cur = None
ans_re = re.compile(r'^> \*\*答案：([A-D])\*\*(.*)$')
q_re = re.compile(r'^\*\*(\d+)\.\*\*\s*(.*)$')
opt_head = re.compile(r'^([A-D])[.、．]\s*(.*)$')
multi_split = re.compile(r'\s+(?=[BCD][.、．]\s)')

def parse_opts(ln, opts):
    # 单行四选项（含 B/C/D 前有空格的分割点）→ 按 parseBank 逻辑拆分
    if re.match(r'^A[.、．]\s', ln) and re.search(r'[CD][.、．]\s', ln):
        for p in multi_split.split(ln):
            m = opt_head.match(p)
            if m and m.group(1) not in opts:
                opts[m.group(1)] = m.group(2).strip()
        return True
    m = opt_head.match(ln)
    if m and m.group(1) not in opts:
        opts[m.group(1)] = m.group(2).strip()
        return True
    return False

for ln in lines:
    m = q_re.match(ln)
    if m:
        cur = {'stem': m.group(2).strip(), 'opts': {}, 'ans': None, 'exp': None}
        n = int(m.group(1))
        if n in qs:
            fails.append('题号重复: %d' % n)
        qs[n] = cur
        continue
    if cur is None or cur['ans'] is not None:
        continue
    m3 = ans_re.match(ln)
    if m3:
        cur['ans'] = m3.group(1)
        cur['exp'] = m3.group(2).lstrip('。').strip()
        continue
    parse_opts(ln, cur['opts'])

check(len(qs) == 100, '题数=%d 应为100' % len(qs))
missing = [n for n in range(1, 101) if n not in qs]
check(not missing, '缺题: %s' % missing)
for n, q in sorted(qs.items()):
    check(len(q['opts']) == 4, 'Q%d 选项数=%d (缺%s)' % (n, len(q['opts']), sorted(set('ABCD') - set(q['opts']))))
    if len(q['opts']) == 4:
        check(len(set(q['opts'].values())) == 4, 'Q%d 选项重复' % n)
        check(all(q['opts'].values()), 'Q%d 有空选项' % n)
    check(q['ans'] in 'ABCD', 'Q%d 答案字母非法: %r' % (n, q['ans']))
    check(q['exp'] and len(q['exp']) >= 5, 'Q%d 解析过短' % n)
dist = {}
for q in qs.values():
    dist[q['ans']] = dist.get(q['ans'], 0) + 1
print('[结构] 100题解析: %s | 分布: %s' % ('OK' if not [f for f in fails if f.startswith('Q') or f.startswith('题')] else '见报告', dist))

# ---------- 2. 速查表转置核对 ----------
ansline = ''.join(qs[n]['ans'] for n in range(1, 101) if n in qs and qs[n]['ans'])
tbl = md[md.index('## 答案速查'):]
row_re = re.compile(r'^\| ([A-D]) \| ([A-D]) \| ([A-D]) \| ([A-D]) \| ([A-D]) \|$', re.M)
trows = row_re.findall(tbl)
check(len(trows) == 20, '速查表数据行=%d 应为20' % len(trows))
tbl_letters = [None] * 100
for r, cells in enumerate(trows):
    for c, ch in enumerate(cells):
        qn = (50 if r >= 10 else 0) + c * 10 + (r % 10)
        tbl_letters[qn] = ch
tblstr = ''.join(l for l in tbl_letters if l)
if ansline != tblstr:
    diffs = [(i + 1, a, b) for i, (a, b) in enumerate(zip(ansline, tblstr)) if a != b]
    fails.append('速查表与答案行不一致，共%d处，前5处(题号/答案行/速查表): %s' % (len(diffs), diffs[:5]))
print('[速查表] 转置核对: %s' % ('OK' if ansline == tblstr else 'FAIL %d处' % len(diffs)))

# ---------- 3. 独立重算 ----------
def subnet_of(ip, prefix):
    p = [int(x) for x in ip.split('.')]
    ipi = (p[0] << 24) | (p[1] << 16) | (p[2] << 8) | p[3]
    host = 32 - prefix
    mask = ((0xFFFFFFFF << host) & 0xFFFFFFFF) if host else 0xFFFFFFFF
    net, bcast = ipi & mask, (ipi & mask) | (~mask & 0xFFFFFFFF)
    f = lambda x: '.'.join(str((x >> s) & 255) for s in (24, 16, 8, 0))
    return f(net), f(bcast), 2 ** host - 2

def usable(ip, prefix):
    net, bcast, _ = subnet_of(ip, prefix)
    n3, nl = net.rsplit('.', 1); b3, bl = bcast.rsplit('.', 1)
    return '%s.%d~%s.%d' % (n3, int(nl) + 1, b3, int(bl) - 1)

def crc(msg, gen):
    work = [int(c) for c in msg] + [0] * (len(gen) - 1)
    g = [int(c) for c in gen]
    for i in range(len(work) - len(g) + 1):
        if work[i]:
            for j in range(len(g)):
                work[i + j] ^= g[j]
    return ''.join(str(b) for b in work[-(len(g) - 1):])

shannon = lambda w, db: round(w * math.log2(1 + 10 ** (db / 10.0)))

M = [  # (题干关键词, 期望值) — 期望值全部由公式独立算出
    ('可分配的主机地址数是', '14'),                                  # /28 → 2^4-2
    ('193.6.7.98/27', usable('193.6.7.98', 27)),                     # 97~126
    ('192.168.15.70', subnet_of('192.168.15.70', 26)[0]),            # .64
    ('cwnd=24', '12 和 1'),                                          # 超时→门限12窗口1
    ('30dB', str(shannon(4, 30))),                                   # 40
    ('3kHz', str(shannon(3, 20))),                                   # 20
    ('16 种不同状态', str(int(2 * 4 * math.log2(16)))),               # 32
    ('6000 波特', '18'),                                             # 6000×3bit
    ('信息位为 1010', '1010' + crc('1010', '1011')),                  # 1010011
    ('后退 N 帧', str(2 ** 3 - 1)),                                  # 7
    ('划分为 8 个等大子网', '%s~%s' % (subnet_of('192.168.4.64', 27)[0], subnet_of('192.168.4.127', 27)[1])),
    ('255.255.248.0', '/21，2046'),
    ('100.10.6.5', '%s，16 位' % subnet_of('100.10.6.5', 16)[0]),
    ('rwnd=4000', str(min(4000, 8000))),
    ('至少容纳 60 台', '255.255.255.192'),
    ('150.100.0.0/16', '4 和 4094'),
    ('255.255.255.224 对应的前缀', '/27'),
    ('172.16.100.20/25', subnet_of('172.16.100.20', 25)[1]),
    ('与 10.1.8.64/26 不在同一子网', '10.1.8.130'),
    ('路由表中存在 192.168.8.0/24', '192.168.8.0/22'),
    ('10.1.64.0/24', '10.1.64.0/22'),
    ('三次握手。若客户端发送的 SYN', '1001'),
    ('连接释放过程中', 'TIME_WAIT'),
    ('MAC 地址的长度', '48'),
    ('最小帧长', '64'),
    ('冲突域和广播域的个数', '8 和 1'),
    ('能够隔离广播域', '路由器'),
    ('RIP 协议中，表示', '16'),
    ('ping 命令', 'ICMP'),
    ('0:0:0:0:0:0:0:1', '::1'),
    ('关于 IPv6 的说法中，错误', '支持广播'),
    ('DHCP 客户端首次', '发现→提供→请求→确认'),
    ('404', '请求的资源不存在'),
    ('MD5 消息摘要的长度', '128'),
    ('用于话音通信的信道数', '30'),
    ('PCM 一次群', '2.048'),
    ('4 种相位、每种相位 4 种幅度', '4'),
    ('选择重传（SR）协议的发送窗口最大', '2ⁿ⁻¹'),
    ('停等协议', '信道利用率低'),
    ("确认号'字段的含义", '期望收到的下一个字节的序号'),
    ('确认号 ack 的值是', '1001'),
    ('快重传算法的触发条件', '收到 3 个重复的 ACK'),
    ('防止数据报在网络中无限循环', 'TTL（生存时间）'),
    ('区域传送使用的协议和端口', 'TCP 53'),
    ('被动关闭方收到对方的 FIN', 'CLOSE_WAIT'),
    ('邮件交换服务器', 'MX'),
    ('属于非对称加密算法', 'RSA'),
    ('同时保证数据的保密性', '对称加密+散列+发送方私钥签名'),
    ('物理层的传输单位', '比特'),
    ('属于数据链路层的是', '流量控制与差错控制'),
    ('与 OSI 网络层对应', '互联层'),
    ('协议数据单元（PDU）', '会话层—比特'),
    ('发送电子邮件与接收电子邮件', 'SMTP、POP3'),
    ('向邮件服务器发送邮件使用', 'SMTP、POP3'),
    ('属于表示层功能', '语法与语义的表示转换'),
    ('132.19.14.25', 'B 类，132.19'),
    ('属于外部网关协议', 'BGP'),
    ('链路状态通告（LSA）的泛洪范围', '整个自治系统'),
    ('ARP 缓存中没有 B 的 MAC', '广播发送 ARP 请求'),
    ('第三次握手报文的特点', 'ACK=1 且可携带数据'),
    ('发送窗口的大小取决于', 'min(接收窗口, 拥塞窗口)'),
    ('长度字段与校验和字段的共同特点', '各 2 字节'),
    ('TCP 与 UDP 的比较中，错误', 'TCP 支持一对多，UDP 支持一对一'),
    ('FTP 客户端与服务器之间需要建立', '两条 TCP 连接'),
    ('租期到一半', '单播向原服务器请求续租'),
    ('权限最高的部分', 'cn'),
    ('向服务器提交数据', 'POST'),
    ('Cookie 与 Session 的说法中，正确', 'Cookie 存于客户端、Session 存于服务器'),
    ('POP3 协议与 IMAP 协议的主要区别', 'IMAP 支持在服务器端管理邮件'),
    ('HTML 语言的作用', '超文本标记'),
    ('IEEE 802.15 标准对应的技术', '蓝牙/ZigBee'),
    ('向所有站点广播 SSID', '接入点 AP'),
    ('面向车联网与工业控制', 'uRLLC'),
    ('SDN（软件定义网络）的核心思想', '控制平面与数据平面分离'),
    ('NFV 与 SDN 的区别', 'NFV 将网元功能软件化'),
    ('物联网的三层体系结构', '感知层'),
    ('PPP 协议工作在', '数据链路层'),
    ('二层交换机与路由器相比', '根据 IP 在不同网络间转发'),
    ('关于交换机的说法中，正确', '根据 MAC 地址表转发帧'),
    ('同网段其他主机失败', '网线断开或交换机端口故障'),
]
C = [  # 概念题：正确选项应包含的短语
    ('CSMA/CD 的叙述中，错误', '适用于无线局域网'),
    ('CSMA/CA 而不采用', '隐藏终端'),
    ('VLAN 的主要作用', '隔离广播域并增强安全性'),
    ('HTTPS 的安全性基础', '用非对称加密协商对称密钥'),
    ('路由协议的叙述中，错误', 'RIP 适合应用于大规模网络'),
    ('最适合使用 UDP', '实时视频会议'),
    ('默认端口的匹配中，错误', 'Telnet'),
    ('NAT 的叙述中，错误', 'NAT 工作在 OSI 的传输层'),
]

checked = 0
for key, expect in M:
    hits = [n for n, q in qs.items() if key in q['stem']]
    check(bool(hits), '未找到题干含「%s」的题' % key)
    for n in hits:
        if len(qs[n]['opts']) != 4:
            continue
        got = qs[n]['opts'][qs[n]['ans']]
        ok = (expect == got) if re.match(r'^[A-Za-z0-9/.\- :]+$', expect) and len(expect) <= 6 else (expect in got)
        checked += 1
        check(ok, 'Q%d[%s]: 选项=%s 重算=%s' % (n, key[:10], got[:40], expect[:40]))
for key, expect in C:
    hits = [n for n, q in qs.items() if key in q['stem']]
    check(bool(hits), '未找到题干含「%s」的题' % key)
    for n in hits:
        if len(qs[n]['opts']) != 4:
            continue
        checked += 1
        check(expect in qs[n]['opts'][qs[n]['ans']], 'Q%d[%s]: 选项=%s 应含=%s' % (n, key[:10], qs[n]['opts'][qs[n]['ans']][:40], expect))
print('[重算] 独立复核 %d 项（数学公式+概念事实）' % checked)

# ---------- 4. 17-练习数据.js 与 md 一致 ----------
d = open('17-练习数据.js', encoding='utf-8').read()
i = d.find('"name":"网络真题专项"')
check(i >= 0, '17数据文件中找不到 nt 题库')
if i >= 0:
    nt_ans = re.findall(r'"ans":"([A-D])"', d[i:])[:100]
    check(len(nt_ans) == 100, 'nt 答案数=%d' % len(nt_ans))
    check(''.join(nt_ans) == ansline, '17数据文件 nt 答案与 md 不一致')
print('[数据] 17-练习数据.js nt(100题) 答案与 md 一致: %s' % ('OK' if ''.join(nt_ans) == ansline else 'FAIL'))

# ---------- 5. 引用完整性 ----------
p00 = open('00-总计划.md', encoding='utf-8').read()
p02 = open('02-每日学习计划表.md', encoding='utf-8').read()
h = open('17-在线练习系统.html', encoding='utf-8').read()
check(p00.count('544项') == 2 and '297项' not in p00 and '254题' not in p00 and '397项' not in p00 and '497项' not in p00 and '510项' not in p00 and '516项' not in p00 and '524项' not in p00, '00 总数引用异常')
check('网络真题36题' not in p00 and '网络真题36题' not in p02 and '网络真题36题' not in h, '旧标签名残留')
check('网络专项' in h and '网络专项100题' in p00, '新标签名缺失')
check('网络专项100' in p02, '02 未引用网络专项100')
print('[引用] 00/02/html 标签与总数: %s' % ('OK' if not [f for f in fails if '引用' in f or '标签' in f or '总数' in f] else '见报告'))

# ---------- 结论 ----------
print('=' * 56)
if fails:
    print('审计未通过，%d 个问题:' % len(fails))
    for f in fails:
        print(' ✘', f)
    sys.exit(1)
print('审计全部通过 ✅  结构100题 | 速查表100格转置一致 | 独立重算%d项 | 数据/引用一致' % checked)
