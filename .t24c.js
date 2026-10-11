const fs = require('fs'), vm = require('vm');
const html = fs.readFileSync('24-网络架构可视化.html', 'utf8');
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
function makeEl(){ return { value: '', innerHTML: '', textContent: '', style: {}, dataset: {},
  classList: { toggle(){}, add(){}, remove(){} }, setAttribute(){}, appendChild(){},
  addEventListener(){}, getBoundingClientRect(){ return { left: 0, top: 0, width: 1200, height: 800 }; },
  querySelector(){ return null; }, querySelectorAll(){ return []; } }; }
const els = {};
const document = { getElementById(id){ if(!els[id]) els[id] = makeEl(); return els[id]; },
  querySelectorAll(){ return []; }, createElement(){ return makeEl(); } };
const sb = { document, console, Math, isFinite, parseInt, parseFloat, String, Number, Array, Object, Set, RegExp, JSON };
sb.window = sb; sb.window.addEventListener = () => {};
vm.createContext(sb);
scripts.forEach(s => vm.runInContext(s, sb));
let pass = 0, fail = 0;
const ok = (c, m) => { if(c) pass++; else { fail++; console.log('  ✘', m); } };
try { sb.showTab('cong'); sb.showTab('memo'); sb.showTab('cong'); ok(true, '两页签切换'); }
catch(e){ ok(false, 'showTab ' + e.message); }
ok(html.indexOf('<section id="s-cong">') > 0 && html.indexOf('<section id="s-memo">') > html.indexOf('<section id="s-cong">'), 'DOM 两节顺序正确');
ok(html.indexOf('cwSteps') < html.indexOf('id="s-memo"'), '推演器在拥塞页签内');
ok(html.indexOf('四张背诵表') > html.indexOf('id="s-memo"'), '背诵表在背诵页签内');
ok(/'cong', '📈 TCP 拥塞'|'cong','📈 TCP 拥塞'/.test(html.replace(/ /g, ' ').replace(", ", ",").replace(/'cong',\s*'📈 TCP 拥塞'/), "'cong','📈 TCP 拥塞'"), 'SECTIONS 含 cong');
try { sb.cwCalc(); sb.swCalc(); sb.ccqNew(); sb.bcqNew(); ok(true, '四个 handler 正常'); }
catch(e){ ok(false, 'handlers ' + e.message); }
console.log('\n=拆分校验= pass ' + pass + ' / fail ' + fail);
process.exit(fail ? 1 : 0);
