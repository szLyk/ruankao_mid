# -*- coding: utf-8 -*-
"""add_gaps.py —— 31号补四个缺口：④DP手算 / ⑤策略类图 / ③序列图 / ②SQL速览"""
import io

P = '31-应用技术大题可视化.html'
t = io.open(P, encoding='utf-8').read()

# ---------- ④：0-1背包手算 + LIS 状态转移（插在链表/二分范例卡后） ----------
dp_card = ''' <div class="card">
  <h2>📖 完整范例②：0-1 背包手算 + LIS 状态转移（16号④-3/④-1 同源，真题④最爱）</h2>
  <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:13.5px;line-height:1.7">
   <b>【手算演示】</b>容量 C=4；物品：1号(重1,值15)、2号(重3,值20)、3号(重4,值30)。问最大价值？<span style="color:#2563eb">→ 逐行填表：每行=考虑第 i 个物品"放/不放"取大。</span>
  </div>
  <table style="border-collapse:collapse;font-size:13px;margin:0 auto">
   <tr style="background:#eff6ff"><th style="border:1px solid #cbd5e1;padding:4px 14px">dp[i][j]</th><th style="border:1px solid #cbd5e1;padding:4px 10px">j=0</th><th style="border:1px solid #cbd5e1;padding:4px 10px">j=1</th><th style="border:1px solid #cbd5e1;padding:4px 10px">j=2</th><th style="border:1px solid #cbd5e1;padding:4px 10px">j=3</th><th style="border:1px solid #cbd5e1;padding:4px 10px">j=4</th></tr>
   <tr><td style="border:1px solid #cbd5e1;padding:4px 14px">i=1（重1值15）</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">0</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">15</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">15</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">15</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">15</td></tr>
   <tr><td style="border:1px solid #cbd5e1;padding:4px 14px">i=2（重3值20）</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">0</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">15</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">15</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center;background:#fef08a">20</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center;background:#fef08a">35</td></tr>
   <tr><td style="border:1px solid #cbd5e1;padding:4px 14px">i=3（重4值30）</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">0</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">15</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">15</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">20</td><td style="border:1px solid #cbd5e1;padding:4px 10px;text-align:center">35</td></tr>
  </table>
  <div style="text-align:center;font-size:12.5px;color:#475569;margin-top:4px">黄格=放得下第2件后的更优解：max(不放=15, 放=20)→20；j=4 时 max(15, 15+20)=35 → 答案 35（选物品1+2）</div>
  <div class="grid2" style="margin-top:10px">
   <div class="fcard"><b>状态转移方程（必默）</b>dp[i][j] = max( dp[i-1][j] , dp[i-1][j-w[i]] + v[i] )；一维滚动数组时 <b>j 从大到小</b>循环</div>
   <div class="fcard"><b>LIS 一句话</b>dp[i] = 以 a[i] 结尾的最长递增子序列长；转移 dp[i] = max(dp[j]+1)，j&lt;i 且 a[j]&lt;a[i]；答案=max(dp)</div>
  </div>
 </div>
'''
a1 = ' <div class="card">\n  <h2>🎯 填空位模式随机出题</h2>'
assert a1 in t
t = t.replace(a1, dp_card + a1, 1)

# ---------- ⑤：策略模式类图（真题形态，插在策略 Java 全套卡之前） ----------
uml_strategy = ''' <div class="card">
  <h2>🖼 真题形态：策略模式类图（真题⑤=类图+代码填空双拼）</h2>
  <svg viewBox="0 0 760 300" width="100%" style="max-width:740px" xmlns="http://www.w3.org/2000/svg">
    <defs><marker id="stg" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0,0 L9,4 L0,8 Z" fill="#0f172a"/></marker></defs>
    <rect x="280" y="20" width="220" height="70" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="390" y="40" text-anchor="middle" font-size="12.5" fill="#475569">«interface»</text>
    <text x="390" y="60" text-anchor="middle" font-size="14" font-weight="bold" fill="#0f172a">PaymentStrategy</text>
    <text x="390" y="80" text-anchor="middle" font-size="12" fill="#475569">+ pay(amount)</text>
    <rect x="60" y="200" width="180" height="60" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="150" y="226" text-anchor="middle" font-size="14" fill="#0f172a">PaymentContext</text>
    <text x="150" y="248" text-anchor="middle" font-size="12" fill="#475569">strategy: PaymentStrategy</text>
    <rect x="450" y="200" width="130" height="56" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="515" y="233" text-anchor="middle" font-size="13.5" fill="#0f172a">WechatPay</text>
    <rect x="620" y="200" width="120" height="56" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="680" y="233" text-anchor="middle" font-size="13.5" fill="#0f172a">AliPay</text>
    <line x1="240" y1="200" x2="240" y2="130"/>
    <line x1="240" y1="130" x2="336" y2="130"/>
    <line x1="336" y1="130" x2="336" y2="90" marker-end="url(#stg)"/>
    <polygon points="240,200 234,189 246,189" fill="#0f172a" transform="rotate(0)"/>
    <line x1="515" y1="200" x2="515" y2="150"/>
    <line x1="515" y1="150" x2="382" y2="150"/>
    <line x1="382" y1="150" x2="382" y2="96" stroke-dasharray="6 4"/>
    <path d="M382,90 L375,102 L389,102 Z" fill="#fff" stroke="#0f172a" stroke-width="1.5"/>
    <line x1="680" y1="200" x2="680" y2="165"/>
    <line x1="680" y1="165" x2="398" y2="165"/>
    <line x1="398" y1="165" x2="398" y2="96" stroke-dasharray="6 4"/>
    <path d="M398,90 L391,102 L405,102 Z" fill="#fff" stroke="#0f172a" stroke-width="1.5"/>
    <g font-size="12" fill="#dc2626" font-weight="bold">
      <text x="250" y="122">聚合◇在环境端</text>
      <text x="398" y="143">虚线三角=实现</text>
    </g>
    <text x="380" y="288" text-anchor="middle" font-size="12" fill="#64748b">真题⑤题形态：给这张图挖空类名/方法名/关系，再给 Java 代码填 (1)(2)(3)——两半都要会</text>
  </svg>
 </div>
'''
a2 = ' <div class="card">\n  <h2>📖 完整范例：策略模式 Java 全套（16号⑤-1 同源，真题⑤高频）</h2>'
assert a2 in t
t = t.replace(a2, uml_strategy + a2, 1)

# ---------- ③：序列图 mini 范例（插在快递状态图范例卡之后） ----------
seq_card = ''' <div class="card">
  <h2>📖 完整范例：网购支付序列图（九图之顺序图，真题考过消息填空）</h2>
  <svg viewBox="0 0 860 300" width="100%" style="max-width:860px" xmlns="http://www.w3.org/2000/svg">
    <defs><marker id="sg1" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0,0 L9,4 L0,8 Z" fill="#0f172a"/></marker>
    <marker id="sg2" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0,0 L9,4 L0,8 Z" fill="#64748b"/></marker></defs>
    <g fill="#eff6ff" stroke="#2563eb" stroke-width="1.5">
      <rect x="90" y="20" width="140" height="36" rx="4"/>
      <rect x="360" y="20" width="140" height="36" rx="4"/>
      <rect x="630" y="20" width="140" height="36" rx="4"/>
    </g>
    <g text-anchor="middle" font-size="13.5" fill="#0f172a">
      <text x="160" y="43">:顾客界面</text>
      <text x="430" y="43">:订单系统</text>
      <text x="700" y="43">:支付系统</text>
    </g>
    <g stroke="#94a3b8" stroke-width="1.2" stroke-dasharray="5 4">
      <line x1="160" y1="56" x2="160" y2="270"/>
      <line x1="430" y1="56" x2="430" y2="270"/>
      <line x1="700" y1="56" x2="700" y2="270"/>
    </g>
    <g fill="#fde68a" stroke="#0f172a">
      <rect x="152" y="76" width="16" height="150"/>
      <rect x="422" y="96" width="16" height="130"/>
      <rect x="692" y="116" width="16" height="60"/>
    </g>
    <g stroke="#0f172a" stroke-width="1.5" fill="none">
      <line x1="168" y1="90" x2="422" y2="90" marker-end="url(#sg1)"/>
      <line x1="438" y1="116" x2="692" y2="116" marker-end="url(#sg1)"/>
      <line x1="692" y1="160" x2="440" y2="160" stroke-dasharray="6 4" marker-end="url(#sg2)"/>
      <line x1="422" y1="204" x2="170" y2="204" stroke-dasharray="6 4" marker-end="url(#sg2)"/>
    </g>
    <g font-size="12.5" fill="#0f172a">
      <text x="295" y="82" text-anchor="middle">提交订单</text>
      <text x="565" y="108" text-anchor="middle">发起支付</text>
      <text x="565" y="150" text-anchor="middle" fill="#dc2626">返回支付结果</text>
      <text x="295" y="196" text-anchor="middle" fill="#dc2626">返回下单结果</text>
    </g>
    <g font-size="12" fill="#64748b" text-anchor="middle">
      <text x="430" y="292">实线箭头=同步消息　虚线箭头=返回消息　竖虚线=生命线　窄矩形=激活期——顺序图强调<b>时间顺序</b>，与通信图（按结构组织+顺序号）同构</text>
    </g>
  </svg>
 </div>
'''
a3 = ' <div class="card">\n  <h2>🎲 情景选图随机出题</h2>'
assert a3 in t
t = t.replace(a3, seq_card + a3, 1)

# ---------- ②：SQL 三连速览（插在 m:n 范例卡之后、Tab3 注释前） ----------
sql_card = ''' <div class="card">
  <h2>📖 SQL 三连速览（16号②-4 同源，真题②必考写法）</h2>
  <pre style="background:#0f172a;color:#e2e8f0;padding:12px;border-radius:8px;font-size:12.5px;overflow-x:auto">-- 1. 三表连接查"借书未还"（NULL 判断必须 IS NULL，不能 = NULL）
SELECT r.Name, b.Title
FROM Borrow br
JOIN Reader r ON br.ReaderID = r.ReaderID
JOIN Book b   ON br.BookID   = b.BookID
WHERE br.ReturnDate IS NULL;

-- 2. 分组统计 + 条件过滤（过滤聚合结果用 HAVING，不是 WHERE）
SELECT b.Title, COUNT(*) AS 次数
FROM Borrow br JOIN Book b ON br.BookID = b.BookID
GROUP BY b.Title
HAVING COUNT(*) &gt;= 2;

-- 3. 更新
UPDATE Book SET Stock = Stock + 10 WHERE Title = '软件工程';</pre>
  <div class="grid2" style="margin-top:8px">
   <div class="fcard"><b>三大易错</b>NULL 只能 <b>IS NULL / IS NOT NULL</b>；过滤聚合用 <b>HAVING</b>；多表同名字段要<b>表名前缀</b></div>
   <div class="fcard"><b>配套自测</b>17号大题②-4（图书 SQL 四连：DDL+查询+统计+更新），完整踩分点在里面</div>
  </div>
 </div>
'''
a4 = '</section>\n\n<!-- ============ Tab3 UML ============ -->'
assert a4 in t
t = t.replace(a4, sql_card + '</section>\n\n<!-- ============ Tab3 UML ============ -->', 1)

io.open(P, 'w', encoding='utf-8', newline='').write(t)
print('四个缺口已补齐')
print('svg配对:', t.count('<svg'), '/', t.count('</svg>'))
PYEOF