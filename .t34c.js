const fs = require('fs'), vm = require('vm');
const html = fs.readFileSync('34-设计模式可视化.html', 'utf8');
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
function makeEl(){ return { value: '', innerHTML: '', textContent: '', style: {}, dataset: {},
  classList: { toggle(){}, add(){}, remove(){}, contains(){ return false; } }, setAttribute(){}, appendChild(){},
  addEventListener(){}, getBoundingClientRect(){ return {left:0,top:0,width:1200,height:800}; },
  querySelector(){ return null; }, querySelectorAll(){ return []; }, scrollIntoView(){} }; }
const els = {};
const document = { getElementById(id){ if(!els[id]) els[id] = makeEl(); return els[id]; },
  querySelectorAll(){ return []; }, createElement(){ return makeEl(); } };
const sb = { document, console, Math, isFinite, parseInt, parseFloat, String, Number, Array, Object, Set, RegExp, JSON,
  setInterval(){ return 0; }, clearInterval(){} };
sb.window = sb; sb.window.addEventListener = () => {}; sb.window.scrollTo = () => {};
vm.createContext(sb);
scripts.forEach((s, i) => vm.runInContext(s + (i === scripts.length-1 ? String.fromCharCode(10)+';globalThis.P=P; globalThis.PFULL=PFULL;' : ''), sb));
let pass = 0, fail = 0;
const ok = (c, m) => { if(c) pass++; else { fail++; console.log('  X', m); } };
ok(sb.P.length === 23, '23 模式');
// 全部有骨架 code 且含换行（\n 转义已生效）
ok(sb.P.every(p => p.code && p.code.indexOf('\n') >= 0), '骨架代码多行化');
// PFULL 覆盖 23 模式且每个含 main
const pids = new Set(sb.P.map(p => p.id));
ok(Object.keys(sb.PFULL).length === 23 && sb.P.every(p => sb.PFULL[p.id]), 'PFULL 覆盖 23 模式');
ok(Object.values(sb.PFULL).every(c => c.indexOf('main') >= 0), '每个样例含 main');
// 每个模式点开：详情面板含骨架 + 完整样例
let allRender = true;
for(const p of sb.P){
  sb.pPick(p.id);
  const h = els['pdetail'].innerHTML;
  if(h.indexOf('详细样例') < 0 || h.indexOf('code') < 0){ console.log('  X 渲染缺失:', p.id); allRender = false; break; }
}
ok(allRender, '23 模式详情均渲染骨架+完整样例');
// 抽样：工厂方法详情面板含换行后的 interface Product { 独占一行
sb.pPick('fm');
const fmHtml = els['pdetail'].innerHTML;
ok(fmHtml.indexOf('interface Product {') >= 0 && fmHtml.indexOf('return new ConcreteProduct();') >= 0, '工厂方法样例内容正确');
// 场景/填空/易混/原则 quiz 回归
for(const pfx of ['sc','f5','vs','pq']){ sb[pfx+'New'](); }
try { sb.f5Show(); sb.f5Check(); sb.vsShow(); sb.vsCheck(); sb.pqShow(); sb.pqCheck(); ok(true, 'quiz 回归'); } catch(e){ ok(false, 'quiz ' + e.message); }
console.log('\n=34号卡代码升级= pass ' + pass + ' / fail ' + fail);
process.exit(fail ? 1 : 0);
