// 构建 17-练习数据.js：从 09 HTML 抽取摸底卷75题 + 从 10-15 md 解析179题
const fs = require('fs');
const path = require('path');
const DIR = __dirname;

// ---------- 1. 摸底卷：从 09 HTML 抽取 Q 数组 ----------
let MOCK_HTML = '';
function extractMock() {
  const html = MOCK_HTML = fs.readFileSync(path.join(DIR, '09-摸底卷-基础知识-答题版.html'), 'utf8');
  const m = html.match(/const Q\s*=\s*\[([\s\S]*?)\];/);
  if (!m) throw new Error('09 HTML: Q array not found');
  let Q;
  try { Q = eval('[' + m[1] + ']'); } catch (e) { throw new Error('09 HTML eval fail: ' + e.message); }
  if (Q.length !== 75) throw new Error('09 HTML: expect 75 questions, got ' + Q.length);
  return Q.map((it, i) => ({
    id: i + 1, mod: it.m, q: it.q, o: it.o, ans: 'ABCD'[it.a], exp: it.e
  }));
}

// ---------- 2. 讲义题库：解析 md ----------
const BANKS = [
  { f: '10-讲义题库-软件工程.md', id: 'sw', name: '软件工程' },
  { f: '11-讲义题库-数据结构与算法.md', id: 'ds', name: '数据结构与算法' },
  { f: '12-讲义题库-数据库.md', id: 'db', name: '数据库' },
  { f: '13-讲义题库-操作系统.md', id: 'os', name: '操作系统' },
  { f: '14-讲义题库-组成原理与网络.md', id: 'hw', name: '组成原理与网络' },
  { f: '15-讲义题库-程序语言与背诵类.md', id: 'pl', name: '程序语言与背诵类' },
  { f: '23-网络真题风格专项卷.md', id: 'nt', name: '网络真题专项' },
];

function parseBank(file, modId, modName) {
  const text = fs.readFileSync(path.join(DIR, file), 'utf8');
  const lines = text.split(/\r?\n/);
  const qs = [];
  let cur = null, inAnswer = false;
  const startQ = /^\*\*(\d+)\.\*\*\s*(.*)$/;
  const ansLine = /^>\s*\*\*答案：([A-D])\*\*\s*\.?\s*(.*)$/;

  for (let ln of lines) {
    let m;
    if ((m = ln.match(startQ))) {
      if (cur) qs.push(cur);
      cur = { id: +m[1], mod: modName, q: m[2].trim(), o: [], ans: '', exp: '' };
      inAnswer = false;
      continue;
    }
    if (!cur) continue;
    if ((m = ln.match(ansLine))) {
      cur.ans = m[1]; cur.exp = m[2].replace(/^。/, '').trim(); inAnswer = true;
      // 答案行之后的续行并入解析
      continue;
    }
    if (inAnswer) {
      if (/^> /.test(ln)) cur.exp += ' ' + ln.replace(/^>\s*/, '').trim();
      else if (ln.trim() === '') { /* 空行：题结束 */ if (cur.o.length === 4 && cur.ans) { qs.push(cur); cur = null; inAnswer = false; } }
      continue;
    }
    // 一行含多个选项：A. x  B. y  C. z  D. w（优先判断，避免单选项正则吞掉整行）
    if (/^[AB][.、．]\s/.test(ln) && /[CD][.、．]\s/.test(ln)) {
      const parts = ln.split(/\s+(?=[BCD][.、．]\s)/);
      for (const p of parts) {
        const pm = p.match(/^([A-D])[.、．]\s*(.*)$/);
        if (pm && cur.o.length === 'ABCD'.indexOf(pm[1])) cur.o.push(pm[2].trim());
      }
      continue;
    }
    // 选项行：分行形式
    const om = ln.match(/^(A|B|C|D)[.、．]\s*(.*)$/);
    if (om && cur.o.length === 'ABCD'.indexOf(om[1])) {
      cur.o.push(om[2].trim());
      continue;
    }
    // 普通行并入题干
    if (ln.trim() !== '' && cur.o.length === 0) cur.q += '\n' + ln.trim();
  }
  if (cur) qs.push(cur);

  // 校验
  const bad = qs.filter(x => x.o.length !== 4 || !x.ans || !x.exp);
  if (bad.length) throw new Error(`${file}: ${bad.length} 题解析异常: ` + bad.map(b => b.id + `(选项${b.o.length},答${b.ans||'无'})`).join(','));
  const ids = qs.map(x => x.id);
  for (let i = 0; i < ids.length; i++) if (ids[i] !== i + 1) throw new Error(`${file}: 题号不连续 at ${ids[i]}`);
  return qs.map(x => ({ id: x.id, mod: modName, q: x.q, o: x.o, ans: x.ans, exp: x.exp }));
}

// ---------- 2b. 应用技术大题（16 md）----------
function esc(t){ return t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function md2html(t){
  // ```代码块→<pre>；其余行→<br>拼接；**x**→<b>
  const parts = t.split(/```/);
  let html='';
  parts.forEach((p,i)=>{
    if(i%2===1){ html+='<pre>'+esc(p.replace(/\s+$/,''))+'</pre>'; }
    else{
      let lines = p.split(/\r?\n/).map(l=>l.replace(/^>\s?/,'')).filter((l,idx,arr)=> !(l.trim()==='' && (idx===0||idx===arr.length-1)));
      html += esc(lines.join('\n')).replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>').replace(/\n/g,'<br>');
    }
  });
  return html;
}
function parseBigQ(){
  const text = fs.readFileSync(path.join(DIR,'16-应用技术大题自编卷.md'),'utf8');
  const lines = text.split(/\r?\n/);
  const qs=[]; let cur=null;
  const qHead=/^## (①|②|③|④|⑤)-\d+\s*(.*)$/;
  const catHead=/^# (①|②|③|④|⑤)\s*(.*)$/;
  let cat='';
  for(let i=0;i<lines.length;i++){
    let m;
    if((m=lines[i].match(catHead))){ cat=m[1]+m[2].replace(/（.*$/,''); if(/^自编卷/.test(m[2]))cat=''; continue; }
    if((m=lines[i].match(qHead))){
      if(cur) qs.push(cur);
      cur={cat, title:m[0].replace(/^## /,''), q:[], ans:[]};
      continue;
    }
    if(/^## 自编卷使用排期/.test(lines[i])) break;
    if(!cur) continue;
    if(/^\*\*参考答案\*\*/.test(lines[i])) { cur.inAns=true; continue; }
    (cur.inAns?cur.ans:cur.q).push(lines[i]);
  }
  if(cur) qs.push(cur);
  if(qs.length!==11) throw new Error('16: expect 11 大题, got '+qs.length);
  return qs.map((x,i)=>({ id:i+1, mod:x.cat, title:x.title,
    q: md2html(x.q.join('\n')), ans: md2html(x.ans.join('\n')) }));
}

// ---------- 2c. 英语挖空（19 md，选项构建期轮转）----------
function parseEng(){
  const text = fs.readFileSync(path.join(DIR,'19-专业英语-AI阅读20篇.md'),'utf8');
  const lines = text.split(/\r?\n/);
  const qs=[]; let stem=null;
  for(const ln of lines){
    let m;
    if((m=ln.match(/\*\*挖空自测\*\*：(.*)$/))){ stem=m[1].trim(); continue; }
    if(stem && (m=ln.match(/^A\..*D\./))){
      const parts=ln.split(/\s+(?=[BCD]\.\s)/).map(s=>s.replace(/^[A-D]\.\s*/,'').trim());
      if(parts.length===4){
        const r=qs.length%4;                     // 轮转打乱（md里全排A）
        const ro=[0,1,2,3].map(j=>parts[(j+r)%4]);
        qs.push({id:qs.length+1, mod:'英语挖空', q:stem, o:ro, ans:'ABCD'[(4-r)%4],
          exp:'见19号文件对应篇目的注释表'});
        stem=null;
      }
    }
  }
  if(qs.length!==20) throw new Error('19: expect 20 题, got '+qs.length);
  return qs;
}

// ---------- 2d. 网络自测（22 md 答案要点，手录）----------
const NET12=[
  ['OSI 中负责路由选择的是哪一层？路由器工作在哪层？','网络层；路由器=网络层'],
  ['以太网交换机、集线器分别工作在 OSI 哪层？','交换机=数据链路层；集线器=物理层'],
  ['/28 子网的可用主机数？','14 台（块长16，2⁴−2）'],
  ['203.110.5.68/28 的网络地址？','203.110.5.64（块长16，68 落在 64~79 块）'],
  ['IPv6 地址长度多少位？','128 位（IPv4 为 32 位）'],
  ['TCP 三次握手的目的是什么？','确认双方收发能力 + 防止失效的旧连接请求到达造成资源浪费'],
  ['UDP 首部固定多少字节？TCP 首部最小多少？','UDP 8 字节；TCP 最小 20 字节（可变到 60）'],
  ['发送/接收邮件各用什么协议和端口？','发：SMTP 25；收：POP3 110（或 IMAP 143）'],
  ['带宽 4kHz、信噪比 30dB 的信道容量约多少？','≈40kbps（香农：30dB→S/N=1000，4000×log₂1001）'],
  ['信息 1010、生成多项式 1001，CRC 校验码？','011（发送帧 1010011）'],
  ['RIP 最大跳数？OSPF 基于什么算法？','15 跳；链路状态，用 Dijkstra 求最短路'],
  ['HTTPS 默认端口？如何加密？','443；对称加密传数据 + 非对称加密协商密钥 + 证书验身份'],
].map((x,i)=>({id:i+1, mod:'网络自测', q:x[0], ans:x[1]}));

// ---------- 3. 汇总输出 ----------
const mock = extractMock();
const banks = BANKS.map(b => {
  const qs = parseBank(b.f, b.id, b.name);
  return { id: b.id, name: b.name, qs };
});
const expect = { '软件工程': 61, '数据结构与算法': 52, '数据库': 43, '操作系统': 55, '组成原理与网络': 51, '程序语言与背诵类': 44, '网络真题专项': 100 };
for (const b of banks) if (expect[b.name] !== b.qs.length) throw new Error(`${b.name}: 期望${expect[b.name]}题，实得${b.qs.length}`);

const at = parseBigQ(), eng = parseEng(), net = NET12;
const engAns = eng.map(q=>q.ans).join('');
console.log('at='+at.length, 'eng='+eng.length+' ('+engAns+')', 'net='+net.length);
const out = `// 自动生成：勿手改。由 .build_practice.js 从 09 HTML + 10~15 md + 16/19/22 生成
window.RK_DATA = {
  mock: ${JSON.stringify(mock)},
  banks: ${JSON.stringify(banks)},
  at: ${JSON.stringify(at)},
  eng: ${JSON.stringify(eng)},
  net: ${JSON.stringify(net)},
  passage: ${JSON.stringify((MOCK_HTML.match(/passage:"([\s\S]*?)"\s*\}/) || [])[1] || '')}
};`;
fs.writeFileSync(path.join(DIR, '17-练习数据.js'), out, 'utf8');
console.log('TOTAL banks =', banks.reduce((s, b) => s + b.qs.length, 0), '+ mock 75 + at', at.length, '+ eng', eng.length, '+ net', net.length);
console.log('written 17-练习数据.js, size =', (fs.statSync(path.join(DIR, '17-练习数据.js')).size / 1024).toFixed(1), 'KB');
