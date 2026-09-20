# C 语言速成手册（Java 程序员对照版）

> **定位**：为应用技术④题（C 算法填空）服务。④题是"读代码 + 补 5 个空"，**不需要会写完整 C 程序**，只需要：能读懂指针/数组/字符串/结构体代码、能推断空缺处该填什么。
> **用法**：W1 学第 1-6 节，W2 学第 7-10 节，练习题分两轮做。每节先看差异点，再看代码，最后对照 Java 理解。
> **不学**：union、位域、复杂声明（返回函数指针的函数等）、高级宏——④题用不到。

---

## 一、Java ↔ C 总对照表（先建立全局印象）

| 主题 | Java | C | 关键差异 |
|---|---|---|---|
| 程序入口 | `public static void main(String[] args)` | `int main()` 或 `int main(void)` | C 无类，函数即顶层 |
| 头文件 | `import java.util.*` | `#include <stdio.h>` | C 用头文件声明库函数 |
| 输出 | `System.out.println(x)` | `printf("%d\n", x)` | 需格式符 |
| 输入 | `Scanner` | `scanf("%d", &x)` | **必须加 & 取地址** |
| 布尔 | `boolean` | `int`（0 假，非 0 真） | C99 才有 `bool`，考题常用 int |
| 字符串 | `String`（对象） | `char[]` + `'\0'`（**数组**） | 无 length()，靠 '\0' 判结尾 |
| 字符串长度 | `s.length()` | `strlen(s)` | 不含 '\0' |
| 数组 | `int[] a = new int[n]` | `int a[n]` 或 `malloc` | 无 `.length`，长度自己记 |
| 引用语义 | 对象天然按引用传 | 传指针 `f(&x)` / `f(int *p)` | C 一律值传递，指针模拟引用 |
| 结构体 | `class` | `struct` | struct 只是数据打包，无方法 |
| 内存 | GC 自动回收 | `malloc`/`free` 手动 | 考题一般不纠结释放 |
| 比较 | `equals` / `==` | `strcmp(a,b)==0` | 字符串不能用 == |
| null | `null` | `NULL`（即 0） | 一样用 |

---

## 二、第 1 节：程序骨架

```c
#include <stdio.h>      /* 标准输入输出：printf/scanf */
#include <string.h>     /* 字符串函数：strlen/strcpy/strcmp/strcat */
#include <stdlib.h>     /* malloc/free/abs */

int max(int a, int b) {          /* 函数定义在前 */
    return a > b ? a : b;
}

int main() {                     /* 程序入口，返回 int */
    int x = 3;
    printf("%d\n", max(x, 5));   /* 输出 5 */
    return 0;                    /* 0 表示正常结束 */
}
```

**与 Java 差异**：
- 没有 class，函数直接写在文件里；`main` 是入口
- 注释 `/* */` 或 `//` 都可以
- 变量声明习惯放在块的开头（真题代码都是这个风格，阅读时别不适应）

---

## 三、第 2 节：数据类型与 printf / scanf

| 类型 | 格式符 | 说明 |
|---|---|---|
| `int` | `%d` | 32 位整型 |
| `long` | `%ld` | 长整型 |
| `float` | `%f` | 单精度（输入用 `%f`） |
| `double` | `%lf`(输入) / `%f`(输出) | 双精度 |
| `char` | `%c` | 单字符，本质是小整数 |
| `char *`(字符串) | `%s` | 遇 '\0' 停止 |

```c
int age;  double score;  char name[20];
scanf("%d %lf %s", &age, &score, name);   /* name 是数组名，天然是地址，不加 & */
printf("age=%d, score=%.2f, name=%s\n", age, score, name);
```

**易错点（真题爱考）**：
1. `scanf` 普通变量必须加 `&`，数组名不加
2. `char c = 'A'; printf("%d", c);` 输出 **65**（字符即 ASCII 码）
3. `'0'` 是字符 0（ASCII 48），`0` 是数字 0 —— `'9'-'0'=9` 是数字转换套路

---

## 四、第 3 节：运算符与控制流（和 Java 90% 相同，只看差异）

```c
/* 相同：if/else、switch、while、do-while、for、break、continue、三目 ?: */
/* 逻辑结果：C 没有 boolean，用 int 表示，0=假、非0=真 */
int found = 0;            /* 0 表示 false */
while (!found) { ... }    /* !0 = 1，循环继续 */
```

**差异与高频点**：
- 整数除法：`7/2 = 3`（同 Java）；取余 `%` 只能用于整数
- 自增自增前缀后缀语义同 Java：`a++` 先用后加
- 位运算 `& | ^ ~ << >>` 同 Java，④题偶尔用（如用 `x & 1` 判奇偶）
- **短路求值**：`&&` `||` 同 Java，真题爱考 `if (p != NULL && p->next != NULL)` 这种顺序（先判空再用，防崩溃）

---

## 五、第 4 节：指针基础（④题第一块硬骨头）

### 5.1 指针是什么：存"地址"的变量

```java
/* Java 里你天天用，只是看不见： */
Node p = new Node(...);   /* p 里存的就是对象的引用(地址) */
```

```c
int x = 10;
int *p = &x;      /* p 是"指向 int 的指针"；& 取 x 的地址 */
printf("%d\n", *p);   /* * 解引用：顺着地址取内容 → 输出 10 */
*p = 20;              /* 通过地址改写 x → x 变成 20 */
```

**一句话**：`&` 取地址，`*` 按地址取内容。Java 的 `p.next` ≈ C 的 `(*p).next` ≡ `p->next`。

### 5.2 指针做函数参数 = 模拟 Java 的引用传递

```c
/* ❌ 值传递：改不了外面的 x（真题经典陷阱） */
void change(int a) { a = 100; }
/* ✔ 传地址：能改 */
void change(int *a) { *a = 100; }

int main() {
    int x = 1;
    change(x);      printf("%d\n", x);   /* 输出 1 */
    change(&x);     printf("%d\n", x);   /* 输出 100 */
}
```

**理解**：Java 方法改对象字段能生效、改基本类型不生效——C 里"想让函数改我的变量，就传它的地址"。④题里 `swap(&a, &b)`、`f(int *len)` 都是这个目的。

### 5.3 二级指针只需认识

`int **pp` 是"指向指针的指针"，④题偶尔出现（如链表头插法 `insert(Node **head)`）。知道 `**pp` 是 int、`*pp` 是 `int*` 即可，不必深究。

---

## 六、第 5 节：指针与数组（一体两面）

```c
int a[5] = {10, 20, 30, 40, 50};
int *p = a;            /* 数组名 a 就是首元素地址，等价 &a[0]，不加 & */

p[2]      /* 等价 *(p+2) → 30 */
*(a + 2)  /* 等价 a[2]  → 30 */
*p++      /* 先取 *p 再 p=p+1（后缀自增） */
```

**核心规则**：`p + 1` 移动"一个元素"（int 指针加 1 = 地址加 4 字节），编译器自动按类型换算——所以指针算术永远以元素为单位，不用乘 sizeof。

```c
/* 遍历数组的标准 C 写法（真题风格） */
int i;
for (i = 0; i < n; i++)
    printf("%d ", a[i]);
/* 或指针版 */
int *p;
for (p = a; p < a + n; p++)
    printf("%d ", *p);
```

**易错点**：
- 数组越界 C 不报错（不像 Java 抛异常），真题用 `-1`、`n-1` 边界考你
- `sizeof(a)/sizeof(a[0])` 才是元素个数（仅数组名可用，指针上用 sizeof 得到的是指针大小 8）

---

## 七、第 6 节：字符串（与 Java String 本质不同）

```c
char s[] = "hello";     /* 实际是 {'h','e','l','l','o','\0'} 六个字符 */
```

| string.h 函数 | 对应 Java | 注意 |
|---|---|---|
| `strlen(s)` | `s.length()` | 不含 '\0'，**返回 5** |
| `strcpy(dst, src)` | `dst = src` | 复制内容包括 '\0'，dst 要够大 |
| `strcat(dst, src)` | `dst += src` | 拼接到 dst 尾部 |
| `strcmp(a, b)` | `a.compareTo(b)` | **相等返回 0**；a<b 返回负数；判等必须写 `strcmp(a,b)==0` |
| `strchr(s, ch)` | `indexOf` | 返回指针（位置或 NULL） |

```c
/* 遍历字符串的标准写法（④题高频骨架） */
char s[100];  int i, cnt = 0;
for (i = 0; s[i] != '\0'; i++)      /* 条件是 != '\0'，不是 i < strlen(s) */
    if (s[i] >= '0' && s[i] <= '9')
        cnt++;
```

**真题陷阱**：
- `sizeof("hello") = 6`，`strlen("hello") = 5`（一个含 '\0' 一个不含）
- 字符串字面量不能 `s1 == s2` 比较，也不能 `s1 = s2` 赋值（要 strcpy）
- `'a'` 是字符（97），`"a"` 是字符串（'a','\0' 两个字符）——选择题常考

---

## 八、第 7 节：结构体（C 的"只有字段的类"）

```c
struct Student {
    int id;
    char name[20];
    double score;
};                              /* 注意这个分号！ */

struct Student s1 = {1001, "Zhang", 88.5};
s1.score = 90;                  /* 点号访问 */

struct Student *p = &s1;        /* 指针访问 */
p->score = 95;                  /* 箭头访问，等价 (*p).score */

typedef struct Student Stu;     /* typedef 起别名，之后可写 Stu s2; */
/* 真题更常见的合并写法： */
typedef struct Node {
    int data;
    struct Node *next;          /* 自引用：链表节点 */
} Node;
```

**对照 Java**：
```java
class Node { int data; Node next; }   // C 的 struct Node* next ≈ Java 的 Node next
p.next.data                            // C 写成 p->next->data
```

结构体数组（排序题常用）：
```c
Stu arr[100];
/* 按分数冒泡排序 */
for (i = 0; i < n - 1; i++)
    for (j = 0; j < n - 1 - i; j++)
        if (arr[j].score < arr[j+1].score) {   /* 降序 */
            Stu t = arr[j]; arr[j] = arr[j+1]; arr[j+1] = t;
        }
```

---

## 九、第 8 节：链表与二叉树的 C 实现（④题最常考的两张图）

### 9.1 单链表

```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;

/* 头插法建表：读入 n 个数 */
Node *create(int a[], int n) {
    Node *head = NULL, *p;
    int i;
    for (i = 0; i < n; i++) {
        p = (Node *)malloc(sizeof(Node));   /* 新节点 */
        p->data = a[i];
        p->next = head;                     /* 新节点指向原首元 */
        head = p;                           /* 头指针前移 */
    }
    return head;
}

/* 遍历求和 */
int sumList(Node *head) {
    int sum = 0;
    Node *p = head;
    while (p != NULL) {       /* 或 while (p) */
        sum += p->data;
        p = p->next;          /* 走一步 */
    }
    return sum;
}
```

**读链表代码的口诀**：`p = p->next` 是"往后走"；`p->next = q` 是"接线"；改链顺序错了会丢后半段——真题让你填的往往是接线顺序。

### 9.2 二叉树（递归三件套）

```c
typedef struct BNode {
    int data;
    struct BNode *left, *right;
} BNode;

/* 中序遍历：左-根-右（先序/后序只是 printf 位置换） */
void inorder(BNode *t) {
    if (t != NULL) {          /* 递归出口：空树返回 */
        inorder(t->left);
        printf("%d ", t->data);
        inorder(t->right);
    }
}

/* 求结点总数 */
int count(BNode *t) {
    if (t == NULL) return 0;
    return count(t->left) + count(t->right) + 1;
}
```

---

## 十、第 9 节：malloc / free 与常见错误

```c
int *a = (int *)malloc(n * sizeof(int));   /* 动态数组，≈ Java 的 new int[n] */
/* ... 用完 */
free(a);                                    /* Java 没有的手动回收 */
```

- `malloc(sizeof(Node))`：申请一个节点的空间，返回 `void*`，真题里通常强制转换 `(Node *)`
- 忘记 free 在考题里不算错误，**但野指针是错误**：`Node *p = NULL; p->data = 1;` 崩溃
- 常见错误清单（读代码挑错题用）：
  1. 数组下标从 1 开始用（C 从 0）
  2. 循环条件 `i <= n`（应为 `< n`）
  3. `scanf` 漏 `&`
  4. 字符串比较用 `==`
  5. `malloc` 后未判空就使用

---

## 十一、第 10 节：④题读题套路总结

1. **先读题干文字**（算法思路一定用中文描述了），给代码分块对应到每个步骤
2. 标出每个变量的含义（在草稿上写：`i 当前元素下标 / dp[i] 以 i 结尾的最长长度 / p 工作指针`）
3. 5 个空的高频位置与填法：
   - **初始化**：`dp[i]=1`、`low=0, high=n-1`、`max=a[0]`
   - **循环边界**：`i<n`、`j<i`、`low<=high`、`i<=n-1`
   - **条件判断**：`a[j]<a[i]`、`s[i]!='\0'`、`p!=NULL`
   - **转移/递推**：`dp[i]=dp[j]+1`、`num=num*10+s[i]-'0'`、`p=p->next`
   - **返回值**：`return best`、`return -1`（查找失败）、`return mid`
4. 拿题干样例**手动代入验证**你填的空（最稳的检查手段）
5. 填空拿不准时：结合对称性（上下文有类似代码）、常理（求最大值初始化应为最小）猜，**不留空**

---

# 二十道读程序练习（W1 做 1-8，W2 做 9-20）

> 全部先自己写出输出，再对答案。风格刻意模仿真题（变量声明在开头）。

**T1**
```c
void swap(int *a, int *b) {
    int t = *a; *a = *b; *b = t;
}
int main() {
    int x = 3, y = 5;
    swap(&x, &y);
    printf("%d %d\n", x, y);
    return 0;
}
```

**T2**
```c
void change(int a) { a = 100; }
int main() {
    int x = 1;
    change(x);
    printf("%d\n", x);
    return 0;
}
```

**T3**
```c
int main() {
    int a[5] = {10, 20, 30, 40, 50};
    int *p = a;
    printf("%d %d %d\n", *p, *(p + 2), p[4]);
    return 0;
}
```

**T4**
```c
int main() {
    int a[] = {1, 2, 3, 4};
    int *p = a;
    p++;
    printf("%d\n", *p);
    *p += 10;
    printf("%d\n", a[1]);
    return 0;
}
```

**T5**
```c
#include <string.h>
int main() {
    char s[] = "hello";
    printf("%d %d\n", (int)strlen(s), (int)sizeof(s));
    return 0;
}
```

**T6**
```c
int main() {
    char s[] = "abca";
    int i, cnt = 0;
    for (i = 0; s[i] != '\0'; i++)
        if (s[i] == 'a') cnt++;
    printf("%d\n", cnt);
    return 0;
}
```

**T7**
```c
#include <string.h>
int main() {
    char a[] = "abc", b[] = "abd";
    printf("%d\n", strcmp(a, b) < 0);
    return 0;
}
```

**T8**
```c
#include <string.h>
int main() {
    char s[10] = "AAAA";
    strcpy(s, "hi");
    printf("%s %d\n", s, (int)strlen(s));
    return 0;
}
```

**T9**
```c
int main() {
    int m[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int i, j, sum = 0;
    for (i = 0; i < 2; i++)
        for (j = 0; j < 3; j++)
            if ((i + j) % 2 == 0) sum += m[i][j];
    printf("%d\n", sum);
    return 0;
}
```

**T10**
```c
struct Point { int x, y; };
int main() {
    struct Point p = {3, 4};
    struct Point *q = &p;
    q->x = 10;
    printf("%d %d\n", p.x, p.y);
    return 0;
}
```

**T11**（链表，建链 1→2→3）
```c
#include <stdlib.h>
typedef struct Node { int data; struct Node *next; } Node;
int main() {
    Node *head = NULL, *p;
    int v[3] = {3, 2, 1}, i;
    for (i = 0; i < 3; i++) {          /* 头插法，依次插 3、2、1 */
        p = (Node *)malloc(sizeof(Node));
        p->data = v[i];
        p->next = head;
        head = p;
    }
    for (p = head; p != NULL; p = p->next)
        printf("%d", p->data);
    return 0;
}
```

**T12**
```c
int f(int n) {
    if (n <= 1) return 1;
    return n * f(n - 1);
}
int main() {
    printf("%d\n", f(5));
    return 0;
}
```

**T13**
```c
int fib(int n) {
    if (n == 1 || n == 2) return 1;
    return fib(n - 1) + fib(n - 2);
}
int main() {
    printf("%d\n", fib(6));
    return 0;
}
```

**T14**（写输出字符串）
```c
#include <string.h>
void reverse(char *s) {
    int i = 0, j = (int)strlen(s) - 1;
    while (i < j) {
        char t = s[i]; s[i] = s[j]; s[j] = t;
        i++; j--;
    }
}
int main() {
    char s[] = "hello";
    reverse(s);
    printf("%s\n", s);
    return 0;
}
```

**T15**（填空题：补全二分查找两处空，并在 a[]={2,4,6,8,10} 中找 8，写出返回值）
```c
int bsearch_(int a[], int n, int key) {
    int low = 0, high = n - 1, mid;
    while (low <= high) {
        mid = (low + high) / 2;
        if (a[mid] == key) return mid;
        else if (a[mid] < key) /*空1*/;
        else /*空2*/;
    }
    return -1;
}
```

**T16**（写返回值）
```c
int atoi_c(char *s) {
    int num = 0, i;
    for (i = 0; s[i] >= '0' && s[i] <= '9'; i++)
        num = num * 10 + (s[i] - '0');
    return num;
}
/* 调用 atoi_c("305") 返回？ */
```

**T17**（填空题：LIS 最长递增子序列，补两处空；求 a[]={3,1,4,1,5,9,2,6} 的返回值）
```c
int lis(int a[], int n) {
    int dp[100], i, j, best = 1;
    for (i = 0; i < n; i++) dp[i] = 1;
    for (i = 1; i < n; i++)
        for (j = 0; j < i; j++)
            if (a[j] < a[i] && /*空1*/)
                /*空2*/;
    for (i = 0; i < n; i++)
        if (dp[i] > best) best = dp[i];
    return best;
}
```

**T18**（数组循环右移 k 位，写移后数组）
```c
void rotate(int a[], int n, int k) {
    int tmp[100], i;
    for (i = 0; i < n; i++)
        tmp[(i + k) % n] = a[i];
    for (i = 0; i < n; i++)
        a[i] = tmp[i];
}
/* a[]={1,2,3,4,5}, n=5, k=2 移动后数组是？ */
```

**T19**
```c
int main() {
    int x = 12, y = 10;
    printf("%d %d %d\n", x & y, x | y, x ^ y);
    return 0;
}
```

**T20**（写输出字符串）
```c
void dedup(char *s) {
    int i, j, k = 0;
    for (i = 0; s[i] != '\0'; i++) {
        for (j = 0; j < k; j++)
            if (s[j] == s[i]) break;
        if (j == k) s[k++] = s[i];
    }
    s[k] = '\0';
}
/* 调用 dedup("abcbad") 后 s 是？ */
```

---

# 答案与解析

**T1**：`5 3`。传地址 → swap 生效。对照：Java 里 `swap(int,int)` 也改不了基本类型，但改对象字段可以——C 传指针就相当于传对象。

**T2**：`1`。值传递，函数内的 a 是副本。真题每年都考这个陷阱。

**T3**：`10 30 50`。`*p`=a[0]，`*(p+2)`=a[2]，`p[4]`=a[4]——三种写法等价。

**T4**：`2` 然后 `12`。p++ 后指向 a[1]；`*p += 10` 改的是 a[1] 本体。

**T5**：`5 6`。strlen 不含 '\0'，sizeof 含。**最高频陷阱之一**。

**T6**：`2`。标准字符串遍历，条件 `s[i] != '\0'`。

**T7**：`1`。"abc"<"abd"（逐字符比较到 c<d），返回负数，`负数<0` 为真（1）。

**T8**：`hi 2`。strcpy 整体覆盖（含 '\0'），原 "AAAA" 被截断。

**T9**：`9`。i+j 为偶数的位置：(0,0)=1、(0,2)=3、(1,1)=5。

**T10**：`10 4`。`q->x` 就是通过地址改 p.x；y 未动。

**T11**：`123`。头插法后进先出：插 3→[3]，插 2→[2,3]，插 1→[1,2,3]。**头插法=逆序**，④题高频。

**T12**：`120`。5!=120，注意出口 `n<=1` 返回 1。

**T13**：`8`。1 1 2 3 5 8，第 6 项是 8。

**T14**：`olleh`。双指针首尾交换，`i<j` 是循环条件（不能取等号，否则多交换一次还原）。

**T15**：空1 `low = mid + 1`；空2 `high = mid - 1`。返回值 `3`（a[3]=8）。经典：往右扔掉左半（low 右移），往左扔掉右半（high 左移）。

**T16**：`305`。`num*10 + (s[i]-'0')` 是字符串转数字的标准递推（④题真题原样考过）。

**T17**：空1 `dp[j] + 1 > dp[i]`；空2 `dp[i] = dp[j] + 1`。返回值 `4`（如 1,4,5,9）。LIS 状态转移：j 是 i 前面比 a[i] 小的位置，能接上才更新。

**T18**：`4 5 1 2 3`。tmp[(0+2)%5]=1→tmp[2]=1……最终 a={4,5,1,2,3}。取模映射是循环移位的标准手法。

**T19**：`8 14 6`。12=1100，10=1010：与=1000(8)、或=1110(14)、异或=0110(6)。

**T20**：`abcd`。内层循环查重：j==k 说明没找到重复才保留（`s[k++]=s[i]` 压缩写入）。j 跳出循环后等于 k 是"未找到"的标志——这个模式④题出现率极高。

---

## 自测标准

- W1 结束（9/27）：T1-T8 全对 + 能不看书写出 swap 和字符串反转
- W2 结束（10/4）：T9-T20 对 10 道以上 + 能默写链表节点定义与遍历
- W5（10/22）：重做当年错题，全对
