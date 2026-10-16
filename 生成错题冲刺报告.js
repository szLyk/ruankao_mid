// 生成错题冲刺报告.js —— 读练习记录 + 题库，输出 错题冲刺报告.md
// 用法：node 生成错题冲刺报告.js   （每次同步练习记录后重跑）
const fs = require('fs'), vm = require('vm');

const rec = JSON.parse(fs.readFileSync('软考-练习记录.json', 'utf8'));
const sb = { window: {} };
vm.createContext(sb);
vm.runInContext(fs.readFileSync('17-练习数据.js', 'utf8'), sb);
const D = sb.window.RK_DATA;

const BANK_NAME = { sw: '软件工程', ds: '数据结构与算法', db: '数据库', os: '操作系统', hw: '组成原理与网络', pl: '程序语言与背诵类', nt: '网络真题专项', mock: '摸底卷(09)', eng: '专业英语(19)', at: '应用技术大题(16)' };
const GO_TO = {
  sw: '25号软件工程课件（对应页签+知识图谱定位）',
  ds: '28号数据结构课件（线性/树/图/查找/排序页签）',
  db: '27号数据库课件（范式/事务/SQL 页签）',
  os: '26号操作系统课件（PV/死锁/页式/置换页签）',
  hw: '29号组成原理课件（网络题→24号网络课件）',
  pl: '30号程序语言与背诵课件（编译/文法/产权/安全页签）',
  nt: '24号网络课件速查与背诵页签 + 22号网络详解对应节',
  mock: '按模块归属看上表（摸底题覆盖全科目）',
  eng: '19号专业英语（20 篇阅读 + 3 篇五空完形）',
  at: '04号答题模板 + 16号自编卷'
};
const questions = {};   // key → 题目对象
(function collect(){
  (D.mock || []).forEach(q => questions['mock-' + q.id] = { ...q, bank: 'mock', mod: q.mod });
  (D.eng || []).forEach(q => questions['eng-' + q.id] = { ...q, bank: 'eng' });
  for(const b of (D.banks || [])) b.qs.forEach(q => questions[b.id + '-' + q.id] = { ...q, bank: b.id });
  (D.net || []).forEach(q => questions['net-' + q.id] = { ...q, bank: 'net' });
  (D.at || []).forEach(q => questions['at-' + q.id] = { ...q, bank: 'at' });
})();

const wrongs = {};
for(const [k, v] of Object.entries(rec.answers || {})){
  if(v.correct === false || v.correct === true) { if(!v.correct) wrongs[k] = v; }
  else if(v.ok === false) wrongs[k] = v;
}
// 汇总
const stat = {};
for(const [k, v] of Object.entries(rec.answers || {})){
  const b = k.split('-')[0];
  stat[b] = stat[b] || { n: 0, w: 0 };
  stat[b].n++;
  if(v.correct === false || v.ok === false) stat[b].w++;
}
const pct = (w, n) => n ? Math.round((n - w) / n * 100) + '%' : '—';

const byBankWrong = {};
for(const k of Object.keys(wrongs)){
  const b = k.split('-')[0];
  (byBankWrong[b] = byBankWrong[b] || []).push(k);
}
const order = ['nt', 'hw', 'sw', 'os', 'pl', 'db', 'mock', 'eng', 'at', 'net'];
const W = [];
W.push('# 错题冲刺报告（自动生成：' + new Date().toLocaleString('zh-CN') + '）');
W.push('');
W.push('> 用法：按下面清单逐题重做——先盖住答案自己再答一遍，错了就点"去哪补"回课件对应页签。每同步一次练习记录后，重跑 `node 生成错题冲刺报告.js` 本报告自动更新。');
W.push('');
W.push('## 一、总览');
W.push('');
W.push('| 题库 | 已答 | 错 | 正确率 | 去哪补 |');
W.push('|---|---|---|---|---|');
for(const b of order){
  if(!stat[b]) continue;
  const rate = b === 'mock' ? '—（摸底卷只收录错题；实考 27/75）' : pct(stat[b].w, stat[b].n);
  W.push('| ' + (BANK_NAME[b] || b) + ' | ' + stat[b].n + ' | ' + stat[b].w + ' | ' + rate + ' | ' + (GO_TO[b] || '') + ' |');
}
const noAns = ['sw','ds','db','os','hw','pl'].filter(b => !stat[b] || stat[b].n === 0);
if(noAns.length) W.push('| **' + noAns.map(b => BANK_NAME[b]).join('、') + '（' + noAns.map(b => (D.banks.find(x => x.id === b) || {qs:[]}).qs.length) + ' 题）** | 0 | — | — | ⚠ **从未作答，排进本周！** |');
W.push('');
const totalW = Object.keys(wrongs).length, totalN = Object.keys(rec.answers || {}).length;
W.push('**总作答 ' + totalN + ' 题，错 ' + totalW + ' 题**。错题优先级：错题多且分值高的库先清（上面的排序已按此排）。');
W.push('');
W.push('## 二、错题明细（按库）');
for(const b of order){
  const list = (byBankWrong[b] || []).sort((a, c) => (parseInt(a.split('-')[1]) || 0) - (parseInt(c.split('-')[1]) || 0));
  if(!list.length) continue;
  W.push('');
  W.push('### ' + (BANK_NAME[b] || b) + '（' + list.length + ' 错）');
  for(const k of list){
    const q = questions[k];
    const v = wrongs[k];
    if(!q){ W.push('- [' + k + '] （题库快照中未找到，可能是旧编号）'); continue; }
    const stem = q.q.replace(/\s+/g, ' ').slice(0, 80);
    const myAns = v.chosen || v.ans || '?';
    W.push('- **[' + k + ']** ' + stem + '…');
    W.push('  - 我答 **' + myAns + '** ✘ ｜ 正确 **' + q.ans + '** ｜ ' + (q.exp || '').replace(/\s+/g, ' ').slice(0, 90));
    W.push('  - 去哪补：' + (GO_TO[q.bank] || GO_TO[b] || '对应讲义'));
  }
}
W.push('');
W.push('## 三、行动建议（按剩余天数自动给）');
const days = Math.max(0, Math.ceil((new Date('2026-10-24T09:00:00') - new Date()) / 86400000));
W.push('');
if(days > 0){
  W.push('- 距考试约 **' + days + ' 天**。错题 ' + totalW + ' 道，按每天清 ' + Math.ceil(totalW / Math.max(days - 2, 1)) + ' 道的节奏，考前 2 天留给定卷重做。');
  W.push('- 顺序建议：先清 **正确率最低的库**（见上表），再做 33 号全真模拟卷检验。');
  W.push('- 10/23 晚只看 `32-考前24小时清单.html`，不再刷新题。');
}else{
  W.push('- 已进入考试窗口（10/24 起）：只看 `32-考前24小时清单.html` 和上面的错题速览，不做新题。准考证打印窗口 10/20 9:00—10/23 17:00。');
}
W.push('');
fs.writeFileSync('错题冲刺报告.md', W.join('\n'), 'utf8');
console.log('生成 错题冲刺报告.md：总作答 ' + totalN + '，错题 ' + totalW + '，明细 ' + Object.keys(byBankWrong).length + ' 个库');
