// 23 号网络专项卷 · 计算题自动验证器
// 原则：每道计算题用独立实现的公式复算，与题目标称答案比对
const NEW_Q = require('./.net_extra.js');
const assert = (c, m) => { if (!c) { console.error('VERIFY FAIL: ' + m); process.exitCode = 1; } };

// ---- 工具 ----
function blocks(maskLast, prefix) { // 块长法：返回块大小
  return 256 - maskLast;
}
function netAddr(ip, prefix) { // 返回网络地址的第四段数值
  const [a,b,c,d] = ip.split('.').map(Number);
  const block = 256 >> (prefix - 24 > 0 ? 0 : 0); // 未用
  const hostBits = 32 - prefix;
  const size = 2 ** (hostBits % 8 || 8); // 第四段内的块大小
  return d - (d % (hostBits <= 8 ? (2 ** (8 - (prefix - 24))) : 256));
}
function subnet(ip, prefix) { // 通用：返回 {net, bcast, hosts}（按第四段/第三段均支持）
  const p = ip.split('.').map(Number);
  const hostBits = 32 - prefix;
  const total = 2 ** hostBits;
  const ipInt = ((p[0]<<24)>>>0) + (p[1]<<16) + (p[2]<<8) + p[3];
  const maskInt = hostBits === 0 ? 0xFFFFFFFF : (0xFFFFFFFF << hostBits) >>> 0;
  const netInt = (ipInt & maskInt) >>> 0;
  const bcastInt = (netInt | (~maskInt >>> 0)) >>> 0;
  const fmt = n => [(n>>>24)&255,(n>>>16)&255,(n>>>8)&255,n&255].join('.');
  return { net: fmt(netInt), bcast: fmt(bcastInt), hosts: total - 2, size: total };
}

// ---- 逐题验证（新题编号 = 36 + 数组下标 + 1）----
const V = [];
function v(id, name, calc, expect) {
  const got = calc();
  V.push({id, name, got, expect, ok: got === expect});
  assert(got === expect, `Q${id} ${name}: 计算得 ${got} ≠ 标称 ${expect}`);
}

// Q37 20dB/3k 香农
v(37, '香农20dB/3kHz', () => Math.round(3 * Math.log2(101)), 20); // kbps ≈19.97→20
// Q38 6k波特×8状态
v(38, '6000波特×3bit', () => 6000 * 3 / 1000, 18);
// Q39 QAM 4×4
v(39, 'QAM状态数', () => Math.log2(4 * 4), 4);
// Q44 /27 前缀：224
v(44, '224→/27', () => 32 - Math.log2(256 - 224), 27);
// Q45 172.16.100.20/25 广播
v(45, '/25广播', () => subnet('172.16.100.20', 25).bcast, '172.16.100.127');
// Q46 /28 主机
v(46, '/28主机数', () => subnet('192.168.1.65', 28).hosts, 14);
// Q47 /24 分 8 子网第 3 块范围
v(47, '8子网第3块起点', () => subnet('192.168.4.64', 27).net, '192.168.4.64');
// Q48 10.1.8.130 与 64/26 不同子网
v(48, '130不在64/26块', () => subnet('10.1.8.130', 26).net !== subnet('10.1.8.64', 26).net, true);
v('48b', '65/100/126都在块内', () => ['65','100','126'].every(x => subnet('10.1.8.' + x, 26).net === '10.1.8.64'), true);
// Q49 聚合 64~67 → /22
v(49, '64-67聚合/22', () => subnet('10.1.67.0', 22).net, '10.1.64.0');
v('49b', '聚合不吞68', () => subnet('10.1.68.0', 22).net !== '10.1.64.0', true);
// Q57 /26 主机范围题(原36题卷 Q15 复算对照)
v(57, '192.168.15.70/26', () => [subnet('192.168.15.70', 26).net, subnet('192.168.15.70', 26).bcast].join('|'), '192.168.15.64|192.168.15.127');
// Q71 /21 = 255.255.248.0
v(71, '248→/21', () => (8 + 8 + (8 - Math.log2(256 - 248))), 21);
v('71b', '/21主机', () => subnet('10.1.8.200', 21).hosts, 2046);
// Q72 193.6.7.98/27 可用范围
v(72, '98/27块', () => [subnet('193.6.7.98', 27).net, subnet('193.6.7.98', 27).bcast].join('|'), '193.6.7.96|193.6.7.127');
v('72b', '98/27可用97~126', () => subnet('193.6.7.98', 27).net.endsWith('.96') && subnet('193.6.7.98', 27).bcast.endsWith('.127'), true);
// Q73 100.10.6.5/16
v(73, '/16网络地址', () => subnet('100.10.6.5', 16).net, '100.10.0.0');
// Q74 min(4000,8000)
v(74, '发送窗=min', () => Math.min(4000, 8000), 4000);
// 原36题卷的计算题也复算（编号按原卷）
v('o14', '200.16.9.0/24 需60台→/26', () => subnet('200.16.9.0', 26).hosts >= 60 && subnet('200.16.9.0', 27).hosts < 60, true);
v('o15', '70/26 块', () => subnet('192.168.15.70', 26).net, '192.168.15.64');
v('o16', 'B类借4位主机', () => subnet('150.100.0.1', 20).hosts, 4094);
v('o17', '8~11聚合/22', () => subnet('192.168.11.255', 22).net, '192.168.8.0');
v('o27', '30dB/4kHz≈40k', () => Math.round(4 * Math.log2(1001)), 40);
v('o28', '奈奎斯特16电平/4k', () => 2 * 4 * Math.log2(16), 32);
v('o30', 'GBN n=3窗口', () => 2 ** 3 - 1, 7);

// CRC 验证（原29题 + 相关）
function crc(msgBits, genBits) {
  const msg = msgBits.split('').map(Number);
  const gen = genBits.split('').map(Number);
  const len = gen.length;
  const work = msg.concat(Array(len - 1).fill(0));
  for (let i = 0; i <= work.length - len; i++) {
    if (work[i] === 1) for (let j = 0; j < len; j++) work[i + j] ^= gen[j];
  }
  return work.slice(-(len - 1)).join('');
}
v('o29', 'CRC 1010/1011→011', () => crc('1010', '1011'), '011');
v('c1', 'CRC 10110/10011→1111', () => crc('10110', '10011'), '1111');
v('c2', 'CRC 1010/1001→011(22号自测10)', () => crc('1010', '1001'), '011');
v('c2b', 'CRC 10100/1001→110', () => crc('10100', '1001'), '110');
// 汉明码 n=4 → r=3
v('h1', '海明 2^3>=4+3+1', () => 2 ** 3 >= 4 + 3 + 1, true);
// 22§四 例1: 192.168.10.130/26
v('c3', '130/26块', () => [subnet('192.168.10.130', 26).net, subnet('192.168.10.130', 26).bcast].join('|'), '192.168.10.128|192.168.10.191');
// 22§九 自测4: 203.110.5.68/28
v('c4', '68/28块', () => subnet('203.110.5.68', 28).net, '203.110.5.64');

// 新题数据结构校验
assert(NEW_Q.length===64, 'NEW_Q 应为64题，实际'+NEW_Q.length);
NEW_Q.forEach((q, i) => {
  const id = 37 + i;
  assert(q.o.length === 4, `Q${id} 选项数=${q.o.length}`);
  assert(q.a >= 0 && q.a < 4, `Q${id} 答案下标非法`);
  assert(q.e && q.e.length > 5, `Q${id} 解析缺失`);
  assert(new Set(q.o).size === 4, `Q${id} 选项重复`);
});
// 答案分布
const dist = {0:0,1:0,2:0,3:0};
NEW_Q.forEach(q => dist[q.a]++);
console.log('新题(37~100)答案分布:', JSON.stringify(dist));
assert(Math.max(...Object.values(dist)) - Math.min(...Object.values(dist)) <= 4, '答案分布过于集中');

// 汇总
const bad = V.filter(x => !x.ok);
console.log(`计算验证: ${V.length - bad.length}/${V.length} 通过`);
if (bad.length) { bad.forEach(b => console.log('  ✘', b.id, b.name)); process.exit(1); }
console.log('ALL VERIFIED ✅');
