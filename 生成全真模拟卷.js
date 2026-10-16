// 生成全真模拟卷.js —— 按考纲分值结构从题库抽题，生成 33-全真模拟卷.html（3 套 × 75 题）
// 用法：node 生成全真模拟卷.js   （题库更新后重跑即可换新卷）
const fs = require('fs'), vm = require('vm');

const sb = { window: {} };
vm.createContext(sb);
vm.runInContext(fs.readFileSync('17-练习数据.js', 'utf8'), sb);
const D = sb.window.RK_DATA;
const bank = {};
for(const b of D.banks) bank[b.id] = b.qs;

const inRanges = (id, rs) => rs.some(([a, b]) => id >= a && id <= b);
function mulberry32(a){ return function(){ a |= 0; a = a + 0x6D2B79F5 | 0; let t = Math.imul(a ^ a >>> 15, 1 | a); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; }; }
function shuffle(arr, rnd){ const a = arr.slice(); for(let i = a.length - 1; i > 0; i--){ const j = Math.floor(rnd() * (i + 1)); [a[i], a[j]] = [a[j], a[i]]; } return a; }

const comp = bank.hw.filter(q => inRanges(q.id, [[1, 18], [34, 44], [52, 67]]));
const net  = bank.hw.filter(q => inRanges(q.id, [[19, 33], [45, 51]]));

function buildSet(seed){
  const rnd = mulberry32(seed);
  const push = (arr, mod, n) => shuffle(arr, rnd).slice(0, n).map(q => ({ mod, q: q.q, o: q.o, ans: q.ans, exp: q.exp }));
  const qs = [
    ...push(bank.sw, 'sw', 12),
    ...push(bank.ds, 'ds', 11),
    ...push(bank.db, 'db', 7),
    ...push(bank.os, 'os', 8),
    ...push(comp, 'comp', 8),
    ...push(net, 'net', 5),
    ...push(bank.pl, 'pl', 19),
    ...push(D.eng, 'eng', 5)
  ];
  if(qs.length !== 75) throw new Error('组卷数量 ' + qs.length + ' ≠ 75');
  const ids = new Set(qs.map(q => q.q));   // 粗查重（题干相同即重复）
  if(ids.size !== qs.length) throw new Error('套内出现重复题干');
  return shuffle(qs, rnd);
}

const SETS = [buildSet(20261024), buildSet(20261101), buildSet(20261108)];
const modCount = {};
SETS[0].forEach(q => modCount[q.mod] = (modCount[q.mod] || 0) + 1);

const tpl = fs.readFileSync('.mock_tpl.html', 'utf8');
const out = tpl.replace('/*__DATA__*/ []', () => JSON.stringify(SETS));
if(out === tpl) throw new Error('模板占位符未命中');
fs.writeFileSync('33-全真模拟卷.html', out, 'utf8');
console.log('生成 33-全真模拟卷.html：3 套 × 75 题；套一模块分布 =', JSON.stringify(modCount));
