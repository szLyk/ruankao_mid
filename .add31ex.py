# -*- coding: utf-8 -*-
"""add_31_examples.py —— 31号五个页签补齐真题形态完整范例"""
import io, re

P = '31-应用技术大题可视化.html'
t = io.open(P, encoding='utf-8').read()

t16 = io.open('16-应用技术大题自编卷.md', encoding='utf-8').read()
blocks16 = re.findall(r'```svg\n([\s\S]*?)```', t16)
kd_ans = next(b for b in blocks16 if '一初多终' in b and '揽收成功' in b).strip()  # ③-4 状态图答案图

def esc(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

# ================= ① DFD 范例2：房屋租赁 =================
dfd2 = ''' <div class="card">
  <h2>📖 完整范例②：房屋租赁 0 层图（真题·房屋中介同型）</h2>
  <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:13.5px;line-height:1.7">
   <b>【题目描述】</b>房东发布房源信息（存入房源文件）；租客提交租赁申请，系统核对房源后生成租赁合同（存入合同文件）并通知租客；每月末系统根据合同文件生成租金账单发送给租客。<span style="color:#2563eb">→ 自己先画：2 实体 / 3 加工 / 2 存储，再对照。</span>
  </div>
  <svg viewBox="0 0 860 430" width="100%" style="max-width:860px" xmlns="http://www.w3.org/2000/svg">
    <defs><marker id="d2a" markerWidth="9" markerHeight="8" refX="8" refY="4" orient="auto"><path d="M0,0 L9,4 L0,8 Z" fill="#0f172a"/></marker></defs>
    <rect x="20" y="50" width="80" height="40" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
    <text x="60" y="75" text-anchor="middle" font-size="13.5" fill="#0f172a">房东</text>
    <rect x="20" y="250" width="80" height="40" fill="#fde68a" stroke="#0f172a" stroke-width="1.5"/>
    <text x="60" y="275" text-anchor="middle" font-size="13.5" fill="#0f172a">租客</text>
    <rect x="180" y="40" width="130" height="60" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
    <line x1="180" y1="62" x2="310" y2="62" stroke="#2563eb"/><text x="191" y="56" font-size="12" fill="#1e40af">1</text>
    <text x="245" y="83" text-anchor="middle" font-size="13" fill="#0f172a">发布房源</text>
    <rect x="180" y="230" width="130" height="60" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
    <line x1="180" y1="252" x2="310" y2="252" stroke="#2563eb"/><text x="191" y="246" font-size="12" fill="#1e40af">2</text>
    <text x="245" y="273" text-anchor="middle" font-size="13" fill="#0f172a">租赁处理</text>
    <rect x="650" y="170" width="130" height="60" rx="8" fill="#dbeafe" stroke="#2563eb" stroke-width="1.5"/>
    <line x1="650" y1="192" x2="780" y2="192" stroke="#2563eb"/><text x="661" y="186" font-size="12" fill="#1e40af">3</text>
    <text x="715" y="213" text-anchor="middle" font-size="13" fill="#0f172a">账单生成</text>
    <rect x="420" y="50" width="150" height="40" fill="#dcfce7" stroke="#0f172a" stroke-width="1.5"/>
    <line x1="432" y1="50" x2="432" y2="90" stroke="#0f172a" stroke-width="1.5"/>
    <text x="500" y="75" text-anchor="middle" font-size="13" fill="#0f172a">D1 房源文件</text>
    <rect x="430" y="300" width="150" height="40" fill="#dcfce7" stroke="#0f172a" stroke-width="1.5"/>
    <line x1="442" y1="300" x2="442" y2="340" stroke="#0f172a" stroke-width="1.5"/>
    <text x="510" y="325" text-anchor="middle" font-size="13" fill="#0f172a">D2 合同文件</text>
    <g stroke="#0f172a" stroke-width="1.5" fill="none">
      <line x1="100" y1="70" x2="180" y2="70" marker-end="url(#d2a)"/>
      <line x1="310" y1="70" x2="420" y2="70" marker-end="url(#d2a)"/>
      <line x1="100" y1="262" x2="180" y2="258" marker-end="url(#d2a)"/>
      <line x1="455" y1="90" x2="310" y2="228" marker-end="url(#d2a)"/>
      <line x1="310" y1="275" x2="430" y2="315" marker-end="url(#d2a)"/>
      <line x1="243" y1="290" x2="102" y2="278" marker-end="url(#d2a)"/>
      <polyline points="500,340 500,395 790,395 790,230 780,215" fill="none" marker-end="url(#d2a)"/>
      <line x1="650" y1="200" x2="520" y2="320" marker-end="url(#d2a)" opacity="0"/>
    </g>
    <g font-size="12" fill="#475569">
      <text x="106" y="60">房源信息</text>
      <text x="330" y="60">房源写入</text>
      <text x="102" y="246">租赁申请</text>
      <text x="352" y="150">房源核对</text>
      <text x="342" y="308">合同写入</text>
      <text x="118" y="302">租赁合同</text>
      <text x="528" y="384">合同数据</text>
      <text x="742" y="368" fill="#15803d" font-weight="bold">租金账单</text>
    </g>
    <text x="430" y="424" text-anchor="middle" font-size="12" fill="#64748b">同型真题：房产中介/医疗预约/图书借阅——实体数、加工数不同，画法口诀完全一致</text>
  </svg>
 </div>
'''
a1 = ' <div class="card">\n  <h2>🎲 找错随机出题</h2>'
assert a1 in t
t = t.replace(a1, dfd2 + a1, 1)

# ================= ② DB 范例2：学生选课 m:n =================
er2 = ''' <div class="card">
  <h2>📖 完整范例②：学生选课 m:n（必考陷阱：联系属性放联系表）</h2>
  <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:13.5px;line-height:1.7">
   <b>【题目描述】</b>学生可选修多门课程，每门课程可被多名学生选修（选课时登记成绩）。<span style="color:#2563eb">→ 两边都是"多"= m:n；成绩属于"选课这件事"，不放学生也不放课程。</span>
  </div>
  <svg viewBox="0 0 860 320" width="100%" style="max-width:860px" xmlns="http://www.w3.org/2000/svg">
    <rect x="80" y="120" width="120" height="60" fill="#fef3c7" stroke="#0f172a" stroke-width="1.5"/>
    <text x="140" y="146" text-anchor="middle" font-size="14" fill="#0f172a">学生</text>
    <text x="140" y="170" text-anchor="middle" font-size="12" fill="#7c2d12"><tspan text-decoration="underline">学号</tspan>（主键）；姓名</text>
    <rect x="660" y="120" width="120" height="60" fill="#fef3c7" stroke="#0f172a" stroke-width="1.5"/>
    <text x="720" y="146" text-anchor="middle" font-size="14" fill="#0f172a">课程</text>
    <text x="720" y="170" text-anchor="middle" font-size="12" fill="#7c2d12"><tspan text-decoration="underline">课程号</tspan>（主键）；课名；学分</text>
    <polygon points="430,90 490,120 430,150 370,120" fill="#e0e7ff" stroke="#4f46e5" stroke-width="1.5"/>
    <text x="430" y="125" text-anchor="middle" font-size="13.5" fill="#0f172a">选修</text>
    <ellipse cx="430" cy="230" rx="44" ry="20" fill="#fff" stroke="#4f46e5" stroke-width="1.2"/>
    <text x="430" y="235" text-anchor="middle" font-size="12" fill="#0f172a">成绩</text>
    <line x1="430" y1="150" x2="430" y2="210" stroke="#4f46e5" stroke-width="1.2"/>
    <g stroke="#0f172a" stroke-width="1.5">
      <line x1="200" y1="120" x2="370" y2="120"/>
      <line x1="490" y1="120" x2="660" y2="120"/>
    </g>
    <g font-size="13" font-weight="bold" fill="#dc2626">
      <text x="215" y="108">m</text><text x="638" y="108">n</text>
    </g>
    <text x="430" y="290" text-anchor="middle" font-size="12" fill="#64748b">m:n 联系转关系模式必须独立成表：选课(学号，课程号，成绩)，主键=(学号，课程号)组合</text>
  </svg>
  <div class="grid2" style="margin-top:8px">
   <div class="fcard"><b>判定口诀</b>两边各读一遍说明：学生"多门"课、课程"多名"学生 → <b>m:n</b>；只有一边多 → 1:n</div>
   <div class="fcard"><b>最大陷阱</b>m:n 的属性（成绩）放<b>联系表</b>，放实体表直接错（12号题24 同源）</div>
   <div class="fcard"><b>三张表结果</b>学生(学号,姓名)、课程(课程号,课名,学分)、选课(学号,课程号,成绩)——组合主键</div>
   <div class="fcard"><b>配套自测</b>17号大题②-1（选课）/②-2（订单 m:n）/②-4（SQL 四连）</div>
  </div>
 </div>
'''
a2 = '</section>\n\n<!-- ============ Tab3 UML ============ -->'
assert a2 in t
t = t.replace(a2, er2 + '</section>\n\n<!-- ============ Tab3 UML ============ -->', 1)

# ================= ③ UML：状态图范例卡（插在情景选图前） =================
uml3 = ''' <div class="card">
  <h2>📖 完整范例：快递运单状态图（16号③-4 同源）</h2>
  <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:13.5px;line-height:1.7">
   <b>【题目描述】</b>运单创建后处于待揽收；揽收成功进入运输中；到达末端网点转为派送中；若客户签收则发送签收短信并进入已签收（结束）；若拒收转入已退回（结束）。<span style="color:#2563eb">→ 先自己画：圈状态 → 每句"XX后/若XX"=一条转换，标"事件[监护]/动作"。</span>
  </div>
  ''' + kd_ans + '''
  <div class="grid2" style="margin-top:8px">
   <div class="fcard"><b>三连考点</b>一初多终；转换三要素=事件[监护条件]/动作；"签收/拒收"分支→两个终态</div>
   <div class="fcard"><b>选图信号</b>题干说"某对象的状态随事件变迁"→状态图；说"并行流程/泳道"→活动图</div>
  </div>
 </div>
'''
a3 = ' <div class="card">\n  <h2>🎲 情景选图随机出题</h2>'
assert a3 in t
t = t.replace(a3, uml3 + a3, 1)

# ================= ④ C 算法范例卡 =================
code1 = esc('''Node *reverse(Node *head) {
    Node *p = head, *q = NULL, *r;
    while (p != NULL) {
        r = p->next;      /* 1 暂存后继 */
        p->next = q;      /* 2 回头指向已逆置段 */
        q = p;            /* 3 q 前移 */
        p = r;            /* 4 p 后移 */
    }
    return q;             /* 5 新表头 */
}''')
code2 = esc('''int bfind(int a[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {              /* <= 才查边界 */
        int mid = (low + high) / 2;
        if (a[mid] == key) return mid;
        if (a[mid] < key) low = mid + 1;   /* 跳过 mid */
        else              high = mid - 1;
    }
    return -1;
}''')
c_card = ''' <div class="card">
  <h2>📖 完整范例：链表逆置 + 二分查找（16号④-4/④-5 同源）</h2>
  <div class="grid2">
   <div class="fcard"><b>例1 三指针逆置</b>口诀"暂存后继、回头指 q、qp 依次跟上来"；返回 q（p 已空）</div>
   <div class="fcard"><b>例2 二分查找</b>前提有序+顺序存储；mid 已比较故边界 ±1；最多比较 ⌈log₂(n+1)⌉ 次</div>
  </div>
  <pre style="background:#0f172a;color:#e2e8f0;padding:12px;border-radius:8px;font-size:12.5px;overflow-x:auto">''' + code1 + '''</pre>
  <pre style="background:#0f172a;color:#e2e8f0;padding:12px;border-radius:8px;font-size:12.5px;overflow-x:auto">''' + code2 + '''</pre>
  <div class="grid2" style="margin-top:8px">
   <div class="fcard"><b>配套自测</b>17号大题④-1 LIS（动态规划）/④-2 行程压缩（双指针）/④-3 背包/④-4 链表/④-5 二分——全是挖空版</div>
   <div class="fcard"><b>考场策略</b>④题目标 8 分：先读注释和函数头，只填有把握的空，15 分钟到点就走</div>
  </div>
 </div>
'''
a4 = ' <div class="card">\n  <h2>🎯 填空位模式随机出题</h2>'
assert a4 in t
t = t.replace(a4, c_card + a4, 1)

# ================= ⑤ 设计模式范例卡（插在六大设计原则后，section 尾） =================
code3 = esc('''interface PaymentStrategy { void pay(int amount); }        // 抽象策略
class WechatPay implements PaymentStrategy {                  // 具体策略A
    public void pay(int amount) { System.out.println("微信支付" + amount); }
}
class AliPay implements PaymentStrategy {                     // 具体策略B
    public void pay(int amount) { System.out.println("支付宝支付" + amount); }
}
class PaymentContext {                                        // 环境类
    private PaymentStrategy strategy;                         // 持有策略
    public void setStrategy(PaymentStrategy s) { this.strategy = s; }
    public void checkout(int amount) { strategy.pay(amount); }  // 委托
}
// 客户端：运行期换算法，消除 if-else
// ctx.setStrategy(new WechatPay()); ctx.checkout(100);''')
dp_card = ''' <div class="card">
  <h2>📖 完整范例：策略模式 Java 全套（16号⑤-1 同源，真题⑤高频）</h2>
  <div style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:13.5px;line-height:1.7">
   <b>【题目描述】</b>商城结算支持微信/支付宝等多种支付方式，结算时可在运行期切换。<span style="color:#2563eb">→ 三角色口诀：接口=策略、实现类=具体策略、持有者=环境；"可更换"三个字=策略模式。</span>
  </div>
  <pre style="background:#0f172a;color:#e2e8f0;padding:12px;border-radius:8px;font-size:12.5px;overflow-x:auto">''' + code3 + '''</pre>
  <div class="grid2" style="margin-top:8px">
   <div class="fcard"><b>填空高频位</b>环境类持有策略的字段类型=<b>接口名</b>；委托行=<b>strategy.pay(amount)</b>；客户端切换=<b>setStrategy(new XxxPay())</b></div>
   <div class="fcard"><b>真题变体</b>同一套骨架换皮：排序算法切换=策略、促销打折=策略、 Ducks 叫声飞行=策略——识别词"动态切换/可替换"</div>
   <div class="fcard"><b>配套自测</b>17号大题⑤-1（策略）/⑤-2（观察者）/⑤-3（状态）/⑤-4（适配器）</div>
  </div>
 </div>
'''
a5 = '</section>\n\n<!-- ============ 🕸 知识图谱 ============ -->\n<section id="s-kgmap">'
assert a5 in t
t = t.replace(a5, dp_card + '</section>\n\n<!-- ============ 🕸 知识图谱 ============ -->\n<section id="s-kgmap">', 1)

io.open(P, 'w', encoding='utf-8', newline='').write(t)
print('五个页签范例补齐')
print('svg配对:', t.count('<svg'), '/', t.count('</svg>'))
print('完整范例卡数:', t.count('📖 完整范例'))
PYEOF