# -*- coding: utf-8 -*-
"""add_more_at.py —— 16号: 全部大题标注考点 + 新增③-3类图(配SVG)/④-4链表/⑤-3状态模式"""
import io

P = '16-应用技术大题自编卷.md'
t = io.open(P, encoding='utf-8').read()

# ---------- 1. 每道既有大题标注考点 ----------
KP = {
    '①-1': '数据流图元素识别、补数据流（对照说明找缺失流）、父子图平衡',
    '①-2': '分层 DFD 阅读顺序、加工命名规范（动宾结构）、数据流方向',
    '①-3': '补数据流（说明原词口径）、存储直连错误识别、DFD 改错（新增加工中转）',
    '②-1': 'E-R 联系类型判定（1:1/1:n/m:n）、关系模式主键外键、SQL 多表连接',
    '②-2': 'm:n 联系转换（独立成表）、SQL 聚合 GROUP BY、UPDATE 语句',
    '②-3': 'E-R 联系类型、联系属性挂靠（菱形）、关系模式转换（并入 n 端）、SQL 分组统计',
    '③-1': '用例图参与者识别、include/extend 箭头方向与语义、参与者-用例关联',
    '③-2': '类图聚合 vs 组合、泛化符号、多重度标注、继承的 Java 实现',
    '④-1': '动态规划入门：LIS 状态定义与转移方程、双层循环边界',
    '④-2': '双指针遍历字符串、边界条件（末组不足 k 个）',
    '④-3': '0-1 背包二维状态转移、逆序/正序含义、初始化',
    '⑤-1': '策略模式=动态换算法、上下文类委托、多态消除 if-else',
    '⑤-2': '观察者=订阅-通知、Subject 持有 observer 列表、push 模型参数',
}
for k, v in KP.items():
    import re
    m = re.search(r'(## ' + re.escape(k) + r' [^\n]*\n)', t)
    assert m, '未找到标题: ' + k
    t = t.replace(m.group(1), m.group(1) + '\n**考点**：' + v + '\n', 1)

# ---------- 2. 新增 ③-3 类图（配SVG） ----------
Q33 = '''## ③-3 电商会员体系（类图·真题形态）

**考点**：类图组合 vs 聚合、泛化符号与多重度、弱实体（组合主键）、多态的 Java 实现

**说明**：电商系统：一个**会员**可下多个**订单**（也可还没下过单），每个订单只属于一个会员；每个**订单**由若干**订单明细**构成，明细不能脱离订单单独存在（记录商品与数量）；**普通会员**与**金牌会员**都是会员的一种，金牌会员额外具有"折扣计算"能力；每个会员可登记多个**收货地址**，地址必须属于某个会员。

类图如下（关系符号与多重度留白）：

```svg
<svg viewBox="0 0 860 380" width="100%" style="max-width:860px" xmlns="http://www.w3.org/2000/svg">
  <g fill="#eff6ff" stroke="#2563eb" stroke-width="1.5">
    <rect x="80" y="40" width="120" height="54" rx="4"/>
    <rect x="400" y="40" width="120" height="54" rx="4"/>
    <rect x="700" y="40" width="120" height="54" rx="4"/>
    <rect x="60" y="270" width="120" height="54" rx="4"/>
    <rect x="280" y="270" width="120" height="54" rx="4"/>
    <rect x="660" y="270" width="120" height="54" rx="4"/>
  </g>
  <g text-anchor="middle" font-size="14" fill="#0f172a">
    <text x="140" y="62">会员</text><text x="140" y="84" font-size="11.5" fill="#475569">会员号；姓名</text>
    <text x="460" y="62">订单</text><text x="460" y="84" font-size="11.5" fill="#475569">订单号；金额</text>
    <text x="760" y="62">订单明细</text><text x="760" y="84" font-size="11.5" fill="#475569">商品；数量</text>
    <text x="120" y="292">普通会员</text><text x="120" y="314" font-size="11.5" fill="#475569">积分</text>
    <text x="340" y="292">金牌会员</text><text x="340" y="314" font-size="11.5" fill="#475569">折扣率</text>
    <text x="720" y="292">收货地址</text><text x="720" y="314" font-size="11.5" fill="#475569">地址；收件人</text>
  </g>
  <g stroke="#0f172a" stroke-width="1.5" fill="none">
    <line x1="200" y1="67" x2="400" y2="67"/>
    <line x1="520" y1="67" x2="700" y2="67"/>
    <polyline points="140,270 140,150 340,150 340,270"/>
    <polyline points="140,94 140,120 760,120 760,270"/>
  </g>
  <text x="430" y="352" text-anchor="middle" font-size="12" fill="#64748b">题目简图：只有类和连线——符号（三角/菱形）与多重度请你补全（答案见完整图）</text>
</svg>```

**问题**（15 分）：
1. "会员—订单"、"订单—订单明细"分别用什么关系？多重度各是多少？（6 分）
2. "普通会员/金牌会员—会员"是什么关系？符号怎么画、箭头指向谁？（4 分）
3. "订单明细"没有自己的独立主键，它的主键怎么定？这叫什么实体？（3 分）
4. 用 Java 写出金牌会员"折扣计算"的实现要点（与普通会员多态区分）。（2 分）

**参考答案**：
1. 会员—订单：**关联（1 对 0..\*）**——会员端 1、订单端 0..\*（"可还没下过单"所以是 0..\* 不是 1..\*）；订单—订单明细：**组合（实心菱形在订单端）**，订单端 1、明细端 1..\*。明细"不能脱离订单存在"→组合；会员与订单可分离→普通关联。（6 分）
2. **泛化**（继承）：实线+空心三角，三角指向父类"会员"。普通会员、金牌会员各画一条指向会员。（4 分）
3. 订单明细是**弱实体**（依赖实体）：主键 = 订单号 + 商品号（所属订单的主键 + 自身区分属性）组合而成。转关系模式时并入订单端或独立成表都须带上"订单号"外键。（3 分）
4. 会员类声明 `double 折扣()` 抽象/默认方法（普通会员返回 1.0），金牌会员 `@Override` 覆盖为 `金额×折扣率`；调用处 `o.getMember().折扣()` 多态分发，不用 if-else 判会员等级。（2 分）

```svg
<svg viewBox="0 0 860 380" width="100%" style="max-width:860px" xmlns="http://www.w3.org/2000/svg">
  <g fill="#eff6ff" stroke="#2563eb" stroke-width="1.5">
    <rect x="80" y="40" width="120" height="54" rx="4"/>
    <rect x="400" y="40" width="120" height="54" rx="4"/>
    <rect x="700" y="40" width="120" height="54" rx="4"/>
    <rect x="60" y="270" width="120" height="54" rx="4"/>
    <rect x="280" y="270" width="120" height="54" rx="4"/>
    <rect x="660" y="270" width="120" height="54" rx="4"/>
  </g>
  <g text-anchor="middle" font-size="14" fill="#0f172a">
    <text x="140" y="62">会员</text><text x="140" y="84" font-size="11.5" fill="#475569">会员号（主键）</text>
    <text x="460" y="62">订单</text><text x="460" y="84" font-size="11.5" fill="#475569">订单号（主键）</text>
    <text x="760" y="62">订单明细</text><text x="760" y="84" font-size="11.5" fill="#475569">订单号+商品号（主键）</text>
    <text x="120" y="292">普通会员</text><text x="120" y="314" font-size="11.5" fill="#475569">积分</text>
    <text x="340" y="292">金牌会员</text><text x="340" y="314" font-size="11.5" fill="#475569">折扣率</text>
    <text x="720" y="292">收货地址</text><text x="720" y="314" font-size="11.5" fill="#475569">地址；收件人</text>
  </g>
  <g stroke="#0f172a" stroke-width="1.5" fill="none">
    <line x1="200" y1="67" x2="394" y2="67"/>
    <line x1="520" y1="67" x2="694" y2="67"/>
    <line x1="140" y1="270" x2="140" y2="100"/>
    <line x1="340" y1="270" x2="340" y2="150"/>
    <line x1="340" y1="150" x2="134" y2="150"/>
    <polyline points="140,94 140,120 760,120 760,270"/>
  </g>
  <polygon points="406,67 394,61 394,73" fill="#fff" stroke="#0f172a" stroke-width="1.5"/>
  <path d="M140,100 L131,114 L149,114 Z" fill="#fff" stroke="#0f172a" stroke-width="1.5"/>
  <path d="M340,150 L331,164 L349,164 Z" fill="#fff" stroke="#0f172a" stroke-width="1.5"/>
  <rect x="488" y="61" width="12" height="12" fill="#0f172a" transform="rotate(45 494 67)"/>
  <g font-size="12.5" font-weight="bold" fill="#dc2626">
    <text x="212" y="56">1</text><text x="368" y="56">0..*</text>
    <text x="534" y="56">1</text><text x="672" y="56">1..*</text>
    <text x="150" y="140">0..*</text><text x="676" y="112">0..*</text><text x="768" y="140">1</text>
  </g>
  <g font-size="11.5" fill="#4f46e5">
    <text x="272" y="140">泛化（三角指父类）</text>
    <text x="560" y="56" fill="#dc2626">组合：实心菱形在订单端</text>
  </g>
  <text x="430" y="352" text-anchor="middle" font-size="12" fill="#15803d">完整图：多重度红字、泛化三角指向会员、组合实心菱形在订单端、明细主键=订单号+商品号（弱实体）</text>
</svg>```
'''

# ---------- 3. 新增 ④-4 链表 ----------
Q44 = '''## ④-4 单链表逆置（三指针）

**考点**：链表指针操作、三指针反转套路、循环边界与返回值

**问题**（15 分）：函数 `reverse` 将不带头结点的单链表原地逆置，返回新表头。补齐 (1)~(5) 空。

```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;

Node *reverse(Node *head) {
    Node *p, *q, *r;
    p = head;          /* p：当前待处理结点 */
    q = NULL;          /* q：已逆置部分的表头 */
    while (p != __(1)__) {
        r = __(2)__;   /* 先暂存后继，防断链 */
        p->next = __(3)__;  /* 当前结点指向前一段 */
        q = __(4)__;   /* q 前移到已逆置头 */
        p = __(5)__;   /* p 后移到原后继 */
    }
    return __(6)__;    /* 循环结束时 q 即新表头 */
}
```

**参考答案**：
(1) **NULL**　(2) **p->next**　(3) **q**　(4) **p**　(5) **r**　(6) **q**
口诀："**暂存后继、回头指 q、q p 依次跟上来**"。考点三连：为什么先暂存（改 next 后找不到后继）、为什么返回 q（p 已是 NULL）、边界（空表/单结点直接返回自身）。
'''

# ---------- 4. 新增 ⑤-3 状态模式 ----------
Q53 = '''## ⑤-3 订单状态流转（状态模式）

**考点**：状态模式=状态决定行为、Context 委托当前状态对象、与 if-else 方案对比

**说明**：订单有"待支付→已支付→已发货→已完成"四种状态，处于不同状态时"推进"操作的行为不同。现用**状态模式**实现：环境类 Order 持有一个状态对象，推进操作委托给当前状态。

**问题**（15 分）：
1. 写出状态模式的三个角色及本题对应。（6 分）
2. 补全代码 (1)~(3)。（6 分）
3. 相比在 Order 里写 if-else 判断状态，状态模式的好处是什么？（3 分）

```java
interface OrderState {
    void next(Order o);                 // 推进到下一状态
}
class PaidState implements OrderState {
    public void next(Order o) { o.setState(new __(1)__()); }
}
class ShippedState implements OrderState {
    public void next(Order o) { o.setState(new CompletedState()); }
}
class CompletedState implements OrderState {
    public void next(Order o) { /* 终态：不再推进 */ }
}
class Order {                            // 环境类
    private OrderState state = new PendingState();
    void setState(OrderState s) { this.state = s; }
    void next() { __(2)__.next(__(3)__); }   // 委托给当前状态对象
}
```

**参考答案**：
1. **State**（抽象状态）= OrderState 接口；**ConcreteState**（具体状态）= PaidState/ShippedState/CompletedState；**Context**（环境）= Order——持有当前状态、把行为委托出去。（6 分）
2. (1) **ShippedState**　(2) **state**　(3) **this**（把环境自己传给状态，状态才能回调 `o.setState(...)`）。（6 分）
3. 每个状态的逻辑收敛到自己的类里，**新增状态只加类不改环境**（对扩展开放）；消除大片 if-else；状态转换规则一目了然。代价是类数量增多——状态多且转换复杂时才值得。（3 分）
'''

# ---------- 插入新题与改节标题 ----------
a3 = '\n# ④ C 算法填空（3 道）'
assert a3 in t
t = t.replace(a3, '\n' + Q33 + '\n# ④ C 算法填空（4 道）', 1)
a4 = '\n# ⑤ 设计模式 Java 填空（2 道）'
assert a4 in t
t = t.replace(a4, '\n' + Q44 + '\n# ⑤ 设计模式 Java 填空（3 道）', 1)
a5 = '\n## 自编卷使用排期'
assert a5 in t
t = t.replace(a5, '\n' + Q53 + a5, 1)

io.open(P, 'w', encoding='utf-8', newline='').write(t)
import re
print('大题标题数:', len(re.findall(r'^## [①②③④⑤]-\d+', t, re.M)), '(应16)')
print('考点标注数:', t.count('**考点**：'), '(应16)')
