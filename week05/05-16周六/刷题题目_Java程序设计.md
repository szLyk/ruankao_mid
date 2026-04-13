# 05-16 周六刷题题目

## 题目类型：Java程序设计（下午题5）⭐重点选做

---

## 下午题5 选择策略

| 题号 | 内容 | 语言 | 推荐 |
|------|------|------|------|
| 第4题 | 算法设计 | C语言 | 不推荐（算法较难） |
| 第5题 | 程序设计 | Java/C++ | ⭐推荐选Java |

**推荐理由**：你有Java基础，选Java更容易得分

---

## 一、类定义关键字（15题）⭐重点

### 第1题 ⭐重点
Java类定义用什么关键字？

**答案：class**

---

### 第2题 ⭐重点
Java继承用什么关键字？

**答案：extends**

---

### 第3题 ⭐重点
Java实现接口用什么关键字？

**答案：implements**

---

### 第4题 ⭐重点
Java抽象类用什么关键字？

**答案：abstract**

---

### 第5题 ⭐重点
Java接口用什么关键字定义？

**答案：interface**

---

### 第6题
Java创建对象用什么关键字？

**答案：new**

---

### 第7题 ⭐重点
类定义完整语法？

**答案：**
```java
public class ClassName {
    // 属性
    // 方法
}
```

---

### 第8题 ⭐重点
继承类完整语法？

**答案：**
```java
public class ChildClass extends ParentClass {
    // 子类内容
}
```

---

### 第9题 ⭐重点
实现接口完整语法？

**答案：**
```java
public class MyClass implements InterfaceName {
    // 实现接口方法
}
```

---

### 第10题 ⭐重点
同时继承和实现？

**答案：**
```java
public class Child extends Parent implements Interface {
    // 先extends后implements
}
```

---

### 第11题
抽象类定义语法？

**答案：**
```java
public abstract class AbstractClass {
    // 抽象方法
}
```

---

### 第12题
接口定义语法？

**答案：**
```java
public interface InterfaceName {
    // 方法声明
}
```

---

### 第13题
创建对象语法？

**答案：**
```java
ClassName obj = new ClassName();
```

---

### 第14题 ⭐重点
调用父类方法用什么关键字？

**答案：super**

---

### 第15题
调用当前对象用什么关键字？

**答案：this**

---

## 二、构造方法（10题）⭐重点

### 第16题 ⭐重点
构造方法特点？

**答案：与类同名，无返回类型**

---

### 第17题 ⭐重点
构造方法作用？

**答案：初始化对象**

---

### 第18题
无参构造方法？

**答案：**
```java
public ClassName() {
    // 初始化代码
}
```

---

### 第19题 ⭐重点
有参构造方法？

**答案：**
```java
public ClassName(String name, int age) {
    this.name = name;
    this.age = age;
}
```

---

### 第20题
构造方法可以重载吗？

**答案：可以，一个类可以有多个构造方法**

---

### 第21题 ⭐重点
子类调用父类构造方法？

**答案：super()，必须放在构造方法第一行**

---

### 第22题
默认构造方法？

**答案：如果没有显式定义，系统提供无参构造方法**

---

### 第23题
定义构造方法后还有默认构造吗？

**答案：没有，需要手动添加无参构造**

---

### 第24题
this()作用？

**答案：调用本类其他构造方法**

---

### 第25题 ⭐重点
构造方法代码填空常见形式？

**答案：**
```java
public Order(String orderId) {
    this.orderId = orderId;  // 常考
}
```

---

## 三、方法重写（10题）⭐重点必考

### 第26题 ⭐⭐⭐最重点
方法重写用什么注解？

**答案：@Override**

---

### 第27题 ⭐重点
重写方法要求？

**答案：方法名、参数、返回类型必须相同**

---

### 第28题 ⭐重点
重写方法访问权限？

**答案：不能比父类更严格**

---

### 第29题
重写和重载区别？

**答案：**
| 重写Override | 重载Overload |
|--------------|--------------|
| 子类重写父类方法 | 同类中多个同名方法 |
| 参数必须相同 | 参数必须不同 |
| 运行时多态 | 编译时多态 |

---

### 第30题 ⭐重点
重写方法代码形式？

**答案：**
```java
@Override
public void display() {
    // 重写内容
}
```

---

### 第31题
抽象方法必须重写吗？

**答案：是的，子类必须重写抽象方法**

---

### 第32题
接口方法必须实现吗？

**答案：是的，实现类必须实现接口方法**

---

### 第33题 ⭐重点
调用父类被重写方法？

**答案：super.methodName()**

---

### 第34题
final方法可以重写吗？

**答案：不可以，final方法不能被重写**

---

### 第35题 ⭐重点
下午题代码填空常见形式？

**答案：**
```java
@Override
public double calculate() {  // 常考补方法名
    return super.calculate() * 1.1;  // 常考补super
}
```

---

## 四、集合类（15题）⭐重点必考

### 第36题 ⭐重点
List接口特点？

**答案：有序、可重复、可索引访问**

---

### 第37题 ⭐重点
List常用实现类？

**答案：ArrayList、LinkedList**

---

### 第38题 ⭐重点
ArrayList特点？

**答案：动态数组，查询快，增删慢**

---

### 第39题
LinkedList特点？

**答案：链表结构，增删快，查询慢**

---

### 第40题 ⭐重点
创建ArrayList？

**答案：**
```java
List<String> list = new ArrayList<>();
```

---

### 第41题 ⭐重点
List添加元素？

**答案：list.add(element)**

---

### 第42题 ⭐重点
List获取元素？

**答案：list.get(index)**

---

### 第43题
List删除元素？

**答案：list.remove(index) 或 list.remove(element)**

---

### 第44题
List大小？

**答案：list.size()**

---

### 第45题 ⭐重点
Map接口特点？

**答案：键值对存储，键唯一**

---

### 第46题 ⭐重点
Map常用实现类？

**答案：HashMap、TreeMap**

---

### 第47题 ⭐重点
创建HashMap？

**答案：**
```java
Map<String, Integer> map = new HashMap<>();
```

---

### 第48题 ⭐重点
Map添加键值对？

**答案：map.put(key, value)**

---

### 第49题 ⭐重点
Map获取值？

**答案：map.get(key)**

---

### 第50题 ⭐⭐⭐最重点
下午题代码填空常见形式？

**答案：**
```java
List<Order> orders = new ArrayList<>();  // 常考补ArrayList
orders.add(order);  // 常考补add

Map<String, User> users = new HashMap<>();  // 常考补HashMap
users.put("id", user);  // 常考补put
User u = users.get("id");  // 常考补get
```

---

## 五、异常处理（10题）⭐重点

### 第51题 ⭐重点
Java异常处理关键字？

**答案：try、catch、finally、throw、throws**

---

### 第52题 ⭐重点
try-catch作用？

**答案：捕获并处理异常**

---

### 第53题 ⭐重点
try-catch语法？

**答案：**
```java
try {
    // 可能出错的代码
} catch (Exception e) {
    // 处理异常
}
```

---

### 第54题
finally作用？

**答案：无论是否异常都执行，用于释放资源**

---

### 第55题
throw作用？

**答案：抛出异常对象**

---

### 第56题
throws作用？

**答案：声明方法可能抛出的异常**

---

### 第57题
常见异常类？

**答案：NullPointerException、ArrayIndexOutOfBoundsException、IOException**

---

### 第58题 ⭐重点
下午题代码填空常见形式？

**答案：**
```java
try {
    // 代码
} catch (Exception e) {  // 常考补catch
    e.printStackTrace();
}
```

---

### 第59题
finally块语法？

**答案：**
```java
try {
    // 代码
} catch (Exception e) {
    // 处理
} finally {
    // 必执行
}
```

---

### 第60题
throws语法？

**答案：**
```java
public void method() throws IOException {
    // 可能抛异常
}
```

---

## 六、访问控制（8题）⭐重点

### 第61题 ⭐重点
Java访问修饰符？

**答案：public、protected、private、默认（包访问）**

---

### 第62题
public访问范围？

**答案：任何地方都可以访问**

---

### 第63题 ⭐重点
private访问范围？

**答案：只在本类内部可以访问**

---

### 第64题
protected访问范围？

**答案：本类、同包、子类可以访问**

---

### 第65题
默认（包）访问范围？

**答案：本类、同包可以访问**

---

### 第66题 ⭐重点
属性通常用什么修饰？

**答案：private（封装）**

---

### 第67题 ⭐重点
getter/setter用什么修饰？

**答案：public**

---

### 第68题
下午题常见形式？

**答案：**
```java
private String name;  // 属性私有
public String getName() { return name; }  // getter公有
public void setName(String name) { this.name = name; }  // setter公有
```

---

## 七、设计模式（5题）⭐常见

### 第69题 ⭐重点
单例模式特点？

**答案：只有一个实例，全局访问点**

---

### 第70题
工厂模式特点？

**答案：创建对象不暴露创建逻辑**

---

### 第71题
观察者模式特点？

**答案：一对多依赖，状态改变通知所有依赖**

---

### 第72题
策略模式特点？

**答案：定义一系列算法，可相互替换**

---

### 第73题
下午题常见设计模式？

**答案：单例、工厂、观察者、策略**

---

## 八、代码填空题型总结 ⭐重点必考

### 题型1：补类名/接口名

**技巧**：看继承关系，看implements

**例题答案**：
```java
public class Circle extends Shape {  // 补Shape（父类）
public class UserService implements IService {  // 补IService（接口）
```

---

### 题型2：补方法名 ⭐重点

**技巧**：看调用处，看返回类型，看参数

**例题答案**：
```java
public double calculateTotal() {  // 看返回类型double
public void display() {  // 看void返回
obj.calculate();  // 调用处补方法名
```

---

### 题型3：补属性名

**技巧**：看类描述，看getter/setter

**例题答案**：
```java
private String orderId;  // 看getter: getOrderId()
private double amount;  // 看setter: setAmount()
```

---

### 题型4：补关键字 ⭐重点

**技巧**：看语法结构

**例题答案**：
```java
extends ParentClass  // 继承补extends
implements Interface  // 实现补implements
@Override  // 重写补@Override
new ArrayList<>()  // 创建对象补new
super.method()  // 调父类补super
```

---

### 题型5：补集合操作 ⭐重点

**技巧**：看集合类型

**例题答案**：
```java
list.add(element)  // 添加补add
list.get(index)  // 获取补get
map.put(key, value)  // 添加补put
map.get(key)  // 获取补get
```

---

### 题型6：补异常处理

**技巧**：看try结构

**例题答案**：
```java
try { } catch (Exception e) { }  // 补catch
throw new Exception()  // 补throw
```

---

## 九、解题技巧总结 ⭐必背

### 1. 理解设计意图

- 看类名推测功能
- 看类间关系推测设计模式

### 2. 补类名/接口名

| 看什么 | 补什么 |
|--------|--------|
| extends后面 | 父类名 |
| implements后面 | 接口名 |
| new后面 | 类名 |

### 3. 补方法名

| 看什么 | 补什么 |
|--------|--------|
| 返回类型 | 方法名 |
| 调用处 | 被调用方法名 |
| 参数 | 方法参数 |

### 4. 补属性名

| 看什么 | 补什么 |
|--------|--------|
| getter | 去掉get |
| setter | 去掉set |
| 类描述 | 特征名词 |

### 5. 补关键字

| 语法结构 | 补关键字 |
|----------|----------|
| 继承 | extends |
| 实现接口 | implements |
| 方法重写 | @Override |
| 创建对象 | new |
| 调父类 | super |

### 6. 补集合操作

| 集合类型 | 常用方法 |
|----------|----------|
| List | add、get、remove、size |
| Map | put、get、containsKey |

---

## 关键结论 ⭐必考

| 问题 | 答案 |
|------|------|
| 继承关键字 | extends |
| 实现接口关键字 | implements |
| 重写注解 | @Override |
| 创建对象关键字 | new |
| 调父类关键字 | super |
| List添加 | add() |
| List获取 | get() |
| Map添加 | put() |
| Map获取 | get() |
| 异常捕获 | try-catch |
| 抛异常 | throw |
| 声明异常 | throws |

---

## 今日任务

1. 做3套Java程序设计真题
2. 重点练习类定义和方法重写
3. 熟悉集合类操作
4. 总结解题技巧

---

**Java有基础，选第5题更容易得分！加油！**