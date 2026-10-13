const fs = require('fs'), vm = require('vm');
const html = fs.readFileSync('30-程序语言与背诵可视化.html', 'utf8');
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]);
function makeEl(){ return { value: '', innerHTML: '', textContent: '', style: {}, dataset: {},
  classList: { toggle(){}, add(){}, remove(){} }, setAttribute(){}, appendChild(){},
  addEventListener(){}, getBoundingClientRect(){ return {left:0,top:0,width:1200,height:800}; },
  querySelector(){ return null; }, querySelectorAll(){ return []; } }; }
const els = {};
const document = { getElementById(id){ if(!els[id]) els[id] = makeEl(); return els[id]; },
  querySelectorAll(){ return []; }, createElement(){ return makeEl(); } };
const sb = { document, console, Math, isFinite, parseInt, parseFloat, String, Number, Array, Object, Set, RegExp, JSON };
sb.window = sb; sb.window.addEventListener = () => {};
vm.createContext(sb);
scripts.forEach(s => vm.runInContext(s, sb));
let imp = 0, bad = 0;
for(let i = 0; i < 400; i++){
  const q = sb.LTOOL.mqGen();
  if(/P→Q 的真值/.test(q.stem)){
    imp++;
    const m = q.stem.match(/P 为<b>(真|假)<\/b>、Q 为<b>(真|假)<\/b>/);
    const p = m[1] === '真', q2 = m[2] === '真';
    const expect = (!p || q2) ? '真' : '假';
    if(q.ans.mqA !== expect){ console.log('  ✘ 蕴含答案错', q.stem); bad++; }
    if(/<[a-z]/i.test(q.steps)){ console.log('  ✘ steps HTML'); bad++; }
  }
}
console.log(imp >= 80 && bad === 0 ? '✓ 蕴含题型出现 ' + imp + ' 次，答案全部正确' : '✘ imp=' + imp + ' bad=' + bad);
process.exit(imp >= 80 && bad === 0 ? 0 : 1);
