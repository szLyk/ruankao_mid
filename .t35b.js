const fs = require('fs'), vm = require('vm');
const html = fs.readFileSync('35-算法可视化.html', 'utf8');
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
function makeEl(){ return { value: '', innerHTML: '', textContent: '', style: {}, dataset: {},
  classList: { toggle(){}, add(){}, remove(){}, contains(){ return false; } }, setAttribute(){}, appendChild(){},
  addEventListener(){}, getBoundingClientRect(){ return {left:0,top:0,width:1200,height:800}; },
  querySelector(){ return null; }, querySelectorAll(){ return []; }, scrollIntoView(){} }; }
const els = {};
const document = { getElementById(id){ if(!els[id]) els[id] = makeEl(); return els[id]; },
  querySelectorAll(){ return []; }, createElement(){ return makeEl(); } };
const sb = { document, console, Math, isFinite, parseInt, parseFloat, String, Number, Array, Object, Set, RegExp, JSON };
sb.window = sb; sb.window.addEventListener = () => {}; sb.window.scrollTo = () => {};
vm.createContext(sb);
scripts.forEach((s, i) => vm.runInContext(s + (i === scripts.length-1 ? String.fromCharCode(10)+';globalThis.KGD=KG_DATA;' : ''), sb));
let pass = 0, fail = 0;
const ok = (c, m) => { if(c) pass++; else { fail++; console.log('  X', m); } };
const ids = new Set(sb.KGD.NODES.map(n => n.id));
ok(sb.KGD.EDGES.every(e => ids.has(e[0]) && ids.has(e[1])), '图谱边完整');
const seen = new Set();
for(let i = 0; i < 60; i++){
  sb.c5New(); sb.c5Show(); sb.c5Check();
  seen.add(els['c5Kind'].textContent);
  if(els['c5Fb'].innerHTML.indexOf('全对') < 0){ console.log('  X 回填未全对:', els['c5Kind'].textContent); fail++; break; }
}
ok(seen.size === 5, 'C5 五程序全覆盖回填全对 got ' + seen.size);
// 简称判定
sb.cdNew();
let cdSeen = '';
for(let i = 0; i < 60; i++){
  sb.cdNew();
  if(/插入/.test(els['cdQ'].innerHTML) && /tmp/.test(els['cdQ'].innerHTML)){ sb.cdA().value; els['cdA'].value = '插入排序'; sb.cdCheck(); cdSeen = els['cdFb'].innerHTML; break; }
}
ok(cdSeen.indexOf('✔') >= 0, '简称「插入排序」判对 got ' + cdSeen);
console.log('\n=35号复验= pass ' + pass + ' / fail ' + fail);
process.exit(fail ? 1 : 0);
