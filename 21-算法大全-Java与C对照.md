# 21 · 算法大全（按考纲全算法 · Java 与 C 对照 · 大题④ 8分 + 选择题 6 分）

> **用法**：
> 1. **先用 Java 看懂逻辑**（你会 Java），再对照右边的 C 版——两者逐行等价，看懂 Java 就能读懂 C。
> 2. `▶` 标出**大题④真题最爱挖的空**（循环边界 / 状态转移 / 交换 / 递归出口 / 初始化）。
> 3. 学到 W2（数据结构周）开始用；大题④在 W4 算法专项集中练（配合 `16-应用技术大题自编卷` ④ 的 LIS/压缩/背包三题）。
> 4. 每个算法都给了复杂度——选择题直接考。
>
> **考纲对应**：排序、查找、递归、分治、贪心、动态规划、回溯、图算法、字符串匹配、概率/近似/NP（考纲列出的全部在本文）。

---

## 〇、考频地图（先知道哪些最重要）

| 考频 | 算法 | 出现场 |
|---|---|---|
| ⭐⭐⭐ | 0-1背包、LCS、LIS、编辑距离、快排/归并、二分、DFS/BFS、Dijkstra | 大题④真题反复考 |
| ⭐⭐ | 拓扑排序、Prim/Kruskal、KMP、活动选择(贪心)、数字三角形、哈希 | 大题④偶考+选择题常考 |
| ⭐ | 其余排序、汉诺塔、N皇后、最大子段和、关键路径 | 主要选择题 |

---

# 一、排序算法（考纲：插入/希尔/选择/堆/冒泡/快排/归并/基数）

## 1.1 冒泡排序

思路：相邻两两比较，大的往后沉；每一轮把最大值"冒"到末尾。

```java
static void bubbleSort(int[] a) {
    for (int i = 0; i < a.length - 1; i++)            // ▶ n-1 轮
        for (int j = 0; j < a.length - 1 - i; j++)    // ▶ 每轮少比一个（-i 常挖）
            if (a[j] > a[j + 1]) {                    // ▶ 比较方向决定升/降序
                int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t;   // ▶ 三行交换（必挖，与C版一致）
            }
}
```

```c
void bubbleSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - 1 - i; j++)
            if (a[j] > a[j + 1]) {
                int t = a[j]; a[j] = a[j+1]; a[j+1] = t;   // ▶ 三行交换（必挖）
            }
}
```

O(n²)，**稳定**。特征：每一轮固定出一个最大值在末尾。

## 1.2 选择排序

思路：每轮从未排序区选**最小**值，与未排序区第一个元素交换。

```java
static void selectSort(int[] a) {
    for (int i = 0; i < a.length - 1; i++) {
        int k = i;                                  // ▶ 记录最小值下标
        for (int j = i + 1; j < a.length; j++)      // ▶ 从 i+1 开始（常挖）
            if (a[j] < a[k]) k = j;                 // ▶ 比较对象是 a[k]
        int t = a[i]; a[i] = a[k]; a[k] = t;        // ▶ 每轮只交换一次（区别于冒泡）
    }
}
```

```c
void selectSort(int a[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int k = i;
        for (int j = i + 1; j < n; j++)
            if (a[j] < a[k]) k = j;
        int t = a[i]; a[i] = a[k]; a[k] = t;
    }
}
```

O(n²)，**不稳定**（如 5 8 5 2 9）。

## 1.3 直接插入排序

思路：像摸扑克牌——把新牌插进左边的有序区，从右往左腾位置。

```java
static void insertSort(int[] a) {
    for (int i = 1; i < a.length; i++) {            // ▶ 从 1 开始（a[0] 天然有序）
        int t = a[i], j = i - 1;                    // ▶ 待插牌
        while (j >= 0 && a[j] > t) {                // ▶ j>=0（常挖）
            a[j + 1] = a[j];                        // ▶ 大于它的右移
            j--;
        }
        a[j + 1] = t;                               // ▶ 落位（必挖）
    }
}
```

```c
void insertSort(int a[], int n) {
    for (int i = 1; i < n; i++) {
        int t = a[i], j = i - 1;
        while (j >= 0 && a[j] > t) { a[j + 1] = a[j]; j--; }
        a[j + 1] = t;
    }
}
```

O(n²)，**稳定**。优点：**基本有序时接近 O(n)**——选择题常考"哪种排序对基本有序数据最快"。

## 1.4 希尔排序

思路：按增量 gap 分组做插入排序，gap 逐渐减到 1（先粗排后精排）。

```java
static void shellSort(int[] a) {
    for (int gap = a.length / 2; gap > 0; gap /= 2)      // ▶ 增量减半（常挖）
        for (int i = gap; i < a.length; i++) {           // ▶ 从 gap 开始
            int t = a[i], j = i - gap;
            while (j >= 0 && a[j] > t) { a[j + gap] = a[j]; j -= gap; }   // ▶ 步长是 gap 不是 1
            a[j + gap] = t;
        }
}
```

```c
void shellSort(int a[], int n) {
    for (int gap = n / 2; gap > 0; gap /= 2)
        for (int i = gap; i < n; i++) {
            int t = a[i], j = i - gap;
            while (j >= 0 && a[j] > t) { a[j + gap] = a[j]; j -= gap; }
            a[j + gap] = t;
        }
}
```

约 O(n^1.3)，**不稳定**。选择题：希尔是"分组插入"，最后一趟 gap=1 等同插入排序。

## 1.5 快速排序（大题④高频）

思路：选基准 pivot，小的放左大的放右（partition），两边递归。

```java
static void quickSort(int[] a, int lo, int hi) {
    if (lo >= hi) return;                             // ▶ 递归出口（必挖）
    int p = partition(a, lo, hi);
    quickSort(a, lo, p - 1);                          // ▶ 左半 [lo, p-1]
    quickSort(a, p + 1, hi);                          // ▶ 右半 [p+1, hi]
}
static int partition(int[] a, int lo, int hi) {
    int pivot = a[lo], i = lo, j = hi;                // ▶ 首元素做基准
    while (i < j) {
        while (i < j && a[j] > pivot) j--;            // ▶ 从右找小的
        a[i] = a[j];
        while (i < j && a[i] <= pivot) i++;           // ▶ 从左找大的
        a[j] = a[i];
    }
    a[i] = pivot;                                     // ▶ 基准落位（必挖）
    return i;
}
```

```c
void quickSort(int a[], int lo, int hi) {
    if (lo >= hi) return;
    int pivot = a[lo], i = lo, j = hi;
    while (i < j) {
        while (i < j && a[j] > pivot) j--;
        a[i] = a[j];
        while (i < j && a[i] <= pivot) i++;
        a[j] = a[i];
    }
    a[i] = pivot;
    quickSort(a, lo, i - 1);
    quickSort(a, i + 1, hi);
}
```

平均 O(nlogn)，**最坏 O(n²)（已有序+取首元素做基准）**，不稳定。选择题：n 大且随机→快排平均最快；一趟排序后基准必在最终位置。

## 1.6 归并排序

思路：递归二分到单元素，再两两合并（合并时两边各取小的）。

```java
static void mergeSort(int[] a, int lo, int hi) {
    if (lo >= hi) return;
    int mid = (lo + hi) / 2;                    // ▶ 从中间切
    mergeSort(a, lo, mid);                      // ▶ 注意与快排区别：mid 参与左半
    mergeSort(a, mid + 1, hi);
    merge(a, lo, mid, hi);
}
static void merge(int[] a, int lo, int mid, int hi) {
    int[] t = new int[hi - lo + 1];
    int i = lo, j = mid + 1, k = 0;
    while (i <= mid && j <= hi)                 // ▶ 两段都没取完
        t[k++] = (a[i] <= a[j]) ? a[i++] : a[j++];   // ▶ 谁小取谁（相等取左=稳定）
    while (i <= mid) t[k++] = a[i++];           // ▶ 剩余直接接上（必挖）
    while (j <= hi) t[k++] = a[j++];
    for (k = 0; k < t.length; k++) a[lo + k] = t[k];
}
```

```c
void merge(int a[], int lo, int mid, int hi, int t[]) {
    int i = lo, j = mid + 1, k = 0;
    while (i <= mid && j <= hi)
        t[k++] = (a[i] <= a[j]) ? a[i++] : a[j++];
    while (i <= mid) t[k++] = a[i++];
    while (j <= hi)  t[k++] = a[j++];
    for (k = 0; k < hi - lo + 1; k++) a[lo + k] = t[k];
}
void mergeSort(int a[], int lo, int hi, int t[]) {
    if (lo >= hi) return;
    int mid = (lo + hi) / 2;
    mergeSort(a, lo, mid, t);
    mergeSort(a, mid + 1, hi, t);
    merge(a, lo, mid, hi, t);
}
```

O(nlogn) 恒定，**稳定**。选择题：归并需要 O(n) 辅助空间。

## 1.7 堆排序

思路：建成大根堆，堆顶（最大）与末尾交换，剩下的重新下沉调整。

```java
static void heapSort(int[] a) {
    int n = a.length;
    for (int i = n / 2 - 1; i >= 0; i--) sift(a, i, n);   // ▶ 从最后一个非叶结点起建堆
    for (int i = n - 1; i > 0; i--) {
        int t = a[0]; a[0] = a[i]; a[i] = t;              // ▶ 堆顶换到末尾
        sift(a, 0, i);                                    // ▶ 对剩余 i 个元素调整
    }
}
static void sift(int[] a, int p, int n) {                 // 下沉调整（大根堆）
    while (2 * p + 1 < n) {
        int s = 2 * p + 1;                                // ▶ 左孩子下标（必背）
        if (s + 1 < n && a[s + 1] > a[s]) s++;            // ▶ 右孩子更大选右
        if (a[s] <= a[p]) break;                          // ▶ 孩子都不大于父：停
        int t = a[p]; a[p] = a[s]; a[s] = t;
        p = s;                                            // ▶ 继续向下
    }
}
```

```c
void sift(int a[], int p, int n) {
    while (2 * p + 1 < n) {
        int s = 2 * p + 1;
        if (s + 1 < n && a[s + 1] > a[s]) s++;
        if (a[s] <= a[p]) break;
        int t = a[p]; a[p] = a[s]; a[s] = t;
        p = s;
    }
}
void heapSort(int a[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--) sift(a, i, n);
    for (int i = n - 1; i > 0; i--) {
        int t = a[0]; a[0] = a[i]; a[i] = t;
        sift(a, 0, i);
    }
}
```

O(nlogn)，不稳定。选择题：**建堆 O(n)**；优先队列=堆；数组 `i` 的孩子 `2i+1 / 2i+2`、父亲 `(i-1)/2`（下标从 0）。

## 1.8 基数排序（选择题考点，不考实现）

思路：按位分配-收集（先个位装桶再倒出，再十位……）。
复杂度 O(d·(n+r))，d=位数 r=基数（10 个桶），**稳定**。
选择题特征："不比较元素大小也能排序"=基数。

## 1.9 排序总表（选择题直接考，必背）

| 算法 | 平均 | 最坏 | 空间 | 稳定 |
|---|---|---|---|---|
| 冒泡 | O(n²) | O(n²) | O(1) | ✔ |
| 选择 | O(n²) | O(n²) | O(1) | ✘ |
| 插入 | O(n²) | O(n²) | O(1) | ✔ |
| 希尔 | O(n^1.3) | — | O(1) | ✘ |
| 快排 | O(nlogn) | **O(n²)** | O(logn) | ✘ |
| 归并 | O(nlogn) | O(nlogn) | **O(n)** | ✔ |
| 堆 | O(nlogn) | O(nlogn) | O(1) | ✘ |
| 基数 | O(d(n+r)) | O(d(n+r)) | O(n+r) | ✔ |

速记：**"心情不好(不稳定)：选些(希尔)快(快排)堆(堆)"**；最坏会退化到 O(n²) 的：快排（还有基本有序时冒泡/插入本来就是 n²）。

---

# 二、查找

## 2.1 顺序查找 O(n)：挨个比。技巧：n+1 个元素放满（哨兵）可少判一次边界。

## 2.2 二分查找（大题④高频）

```java
static int binSearch(int[] a, int key) {
    int lo = 0, hi = a.length - 1;
    while (lo <= hi) {                       // ▶ <=（漏 = 是经典错）
        int mid = (lo + hi) / 2;             // ▶ 折半
        if (a[mid] == key) return mid;       // ▶ 命中
        else if (a[mid] < key) lo = mid + 1; // ▶ 右半（+1 常挖）
        else hi = mid - 1;                   // ▶ 左半
    }
    return -1;
}
```

```c
int binSearch(int a[], int n, int key) {
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (a[mid] == key) return mid;
        else if (a[mid] < key) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}
```

O(logn)。**最多比较 ⌈log₂(n+1)⌉ 次**（1000 个元素 → 10 次）。前提：**有序+顺序存储**（链表不能二分）。

## 2.3 哈希查找

```java
// 除留余数法 + 链地址法解决冲突
static final int M = 13;
static java.util.ArrayList<Integer>[] h = new java.util.ArrayList[M];
static void insert(int key) {
    int i = key % M;                          // ▶ 哈希函数（常挖：取模）
    if (h[i] == null) h[i] = new java.util.ArrayList<>();
    h[i].add(key);
}
static boolean find(int key) {
    int i = key % M;
    return h[i] != null && h[i].contains(key);
}
```

```c
#define M 13
struct Node { int key; struct Node *next; };
struct Node *ht[M] = {0};
void insert(int key) {
    int i = key % M;
    struct Node *p = (struct Node*)malloc(sizeof(struct Node));
    p->key = key; p->next = ht[i]; ht[i] = p;      // ▶ 头插进第 i 条链
}
int find(int key) {
    for (struct Node *p = ht[key % M]; p; p = p->next)
        if (p->key == key) return 1;
    return 0;
}
```

要点（选择题）：装填因子 α=表中元素/表长，**α 越大冲突越多**；冲突处理：开放定址（线性探测/二次探测）、链地址、再哈希。**同义词冲突不可避免**。

---

# 三、递归与分治

## 3.1 递归三要素：①出口（base case）②递归调用 ③规模缩小。挖空永远挖①和③。

```java
static long fib(int n) {
    if (n <= 1) return n;                    // ▶ 出口
    return fib(n - 1) + fib(n - 2);          // ▶ 递推式（常挖）
}
static void hanoi(int n, char a, char b, char c) {   // a→c 借助 b
    if (n == 1) { System.out.println(a + "->" + c); return; }
    hanoi(n - 1, a, c, b);                   // ▶ 上面 n-1 个 a→b
    System.out.println(a + "->" + c);        // ▶ 最大盘 a→c（必挖）
    hanoi(n - 1, b, a, c);                   // ▶ n-1 个 b→c
}
```

```c
long fib(int n) { if (n <= 1) return n; return fib(n-1) + fib(n-2); }
void hanoi(int n, char a, char b, char c) {
    if (n == 1) { printf("%c->%c\n", a, c); return; }
    hanoi(n - 1, a, c, b);
    printf("%c->%c\n", a, c);
    hanoi(n - 1, b, a, c);
}
```

汉诺塔移动次数 = 2ⁿ−1（选择题常考）。fib 递归复杂度 O(2ⁿ)（重复子问题→引出 DP）。

## 3.2 分治：分解→求解→合并。代表：归并/快排/二分/汉诺塔。选择题：分治的子问题**相互独立**（子问题重叠的是 DP）。

---

# 四、贪心算法

## 4.1 活动选择 / 区间调度（大题④考过）

思路：按**结束时间**升序，每次选结束最早且与已选不冲突的。

```java
static int maxActivities(int[] s, int[] e) {   // s[]开始 e[]结束（e 已升序）
    int cnt = 1, last = 0;                      // ▶ 先选第 0 个
    for (int i = 1; i < s.length; i++)
        if (s[i] >= e[last]) {                  // ▶ 不冲突条件（必挖）
            cnt++;
            last = i;                           // ▶ 更新最后选中
        }
    return cnt;
}
```

```c
int maxActivities(int s[], int e[], int n) {
    int cnt = 1, last = 0;
    for (int i = 1; i < n; i++)
        if (s[i] >= e[last]) { cnt++; last = i; }
    return cnt;
}
```

## 4.2 部分背包（可分割）

策略：按**单位重量价值**降序，尽量装性价比最高的。
选择题：部分背包贪心可得最优解；**0-1 背包贪心不一定最优→用 DP**（两者对比是高频考点）。

## 4.3 哈夫曼（贪心构造）：每次取两棵权最小的树合并。n 个叶结点 → 总结点 2n−1，WPL=Σ(权×深度)。构造过程就是贪心。

---

# 五、动态规划（大题④第一热）

## 5.1 数字三角形（DP 入门）

```java
static int maxPath(int[][] d) {                    // d[i][j] 第 i 行第 j 个
    int n = d.length;
    int[][] f = new int[n + 1][n + 1];             // ▶ f: 从底向上的最大和
    for (int j = 0; j < n; j++) f[n - 1][j] = d[n - 1][j];   // ▶ 底行初始化
    for (int i = n - 2; i >= 0; i--)
        for (int j = 0; j <= i; j++)
            f[i][j] = d[i][j] + Math.max(f[i + 1][j], f[i + 1][j + 1]);   // ▶ 转移方程（必挖）
    return f[0][0];
}
```

```c
int maxPath(int d[][100], int n) {
    int f[100][100];
    for (int j = 0; j < n; j++) f[n-1][j] = d[n-1][j];
    for (int i = n - 2; i >= 0; i--)
        for (int j = 0; j <= i; j++) {
            int m = f[i+1][j] > f[i+1][j+1] ? f[i+1][j] : f[i+1][j+1];
            f[i][j] = d[i][j] + m;
        }
    return f[0][0];
}
```

## 5.2 0-1 背包（大题④真题多次）

`f[i][j]` = 只考虑前 i 件、容量 j 的最大价值。

```java
static int knapsack(int[] w, int[] v, int W) {
    int n = w.length;
    int[][] f = new int[n + 1][W + 1];
    for (int i = 1; i <= n; i++)
        for (int j = 0; j <= W; j++) {
            f[i][j] = f[i - 1][j];                          // ▶ 不选第 i 件
            if (j >= w[i - 1])                              // ▶ 装得下才考虑选
                f[i][j] = Math.max(f[i][j],
                    f[i - 1][j - w[i - 1]] + v[i - 1]);     // ▶ 转移方程（必挖）
        }
    return f[n][W];
}
```

```c
int knapsack(int w[], int v[], int n, int W) {
    int f[100][100] = {0};
    for (int i = 1; i <= n; i++)
        for (int j = 0; j <= W; j++) {
            f[i][j] = f[i-1][j];
            if (j >= w[i-1]) {
                int t = f[i-1][j - w[i-1]] + v[i-1];
                if (t > f[i][j]) f[i][j] = t;
            }
        }
    return f[n][W];
}
```

一维滚动数组版（考过）：`for j = W downto w[i]: f[j] = max(f[j], f[j-w[i]] + v[i])`——**必须倒序**（正序会重复选取，变成完全背包）。

## 5.3 最长公共子序列 LCS

```java
static int lcs(String x, String y) {
    int m = x.length(), n = y.length();
    int[][] f = new int[m + 1][n + 1];
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            if (x.charAt(i - 1) == y.charAt(j - 1))
                f[i][j] = f[i - 1][j - 1] + 1;              // ▶ 相等：左上+1（必挖）
            else
                f[i][j] = Math.max(f[i - 1][j], f[i][j - 1]);   // ▶ 不等：取大
    return f[m][n];
}
```

```c
int lcs(char x[], char y[]) {
    int m = strlen(x), n = strlen(y);
    int f[100][100] = {0};
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            if (x[i-1] == y[j-1]) f[i][j] = f[i-1][j-1] + 1;
            else f[i][j] = f[i-1][j] > f[i][j-1] ? f[i-1][j] : f[i][j-1];
    return f[m][n];
}
```

## 5.4 最长递增子序列 LIS

```java
static int lis(int[] a) {
    int n = a.length, ans = 0;
    int[] f = new int[n];
    for (int i = 0; i < n; i++) {
        f[i] = 1;                                   // ▶ 至少含自己
        for (int j = 0; j < i; j++)
            if (a[j] < a[i] && f[j] + 1 > f[i])     // ▶ 转移条件（必挖）
                f[i] = f[j] + 1;
        if (f[i] > ans) ans = f[i];
    }
    return ans;
}
```

```c
int lis(int a[], int n) {
    int f[1000], ans = 0;
    for (int i = 0; i < n; i++) {
        f[i] = 1;
        for (int j = 0; j < i; j++)
            if (a[j] < a[i] && f[j] + 1 > f[i]) f[i] = f[j] + 1;
        if (f[i] > ans) ans = f[i];
    }
    return ans;
}
```

O(n²)；进阶 O(nlogn)：维护一个递增数组，每次二分替换（了解）。

## 5.5 编辑距离

```java
static int editDist(String x, String y) {
    int m = x.length(), n = y.length();
    int[][] f = new int[m + 1][n + 1];
    for (int i = 0; i <= m; i++) f[i][0] = i;       // ▶ 删成空串
    for (int j = 0; j <= n; j++) f[0][j] = j;
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++)
            if (x.charAt(i - 1) == y.charAt(j - 1))
                f[i][j] = f[i - 1][j - 1];
            else
                f[i][j] = 1 + Math.min(f[i - 1][j - 1],     // 替换
                        Math.min(f[i - 1][j], f[i][j - 1])); // 删、插（必挖）
    return f[m][n];
}
```

```c
int editDist(char x[], char y[]) {
    int m = strlen(x), n = strlen(y), f[100][100];
    for (int i = 0; i <= m; i++) f[i][0] = i;
    for (int j = 0; j <= n; j++) f[0][j] = j;
    for (int i = 1; i <= m; i++)
        for (int j = 1; j <= n; j++) {
            if (x[i-1] == y[j-1]) f[i][j] = f[i-1][j-1];
            else {
                int t = f[i-1][j] < f[i][j-1] ? f[i-1][j] : f[i][j-1];
                if (f[i-1][j-1] < t) t = f[i-1][j-1];
                f[i][j] = t + 1;
            }
        }
    return f[m][n];
}
```

## 5.6 最大子段和

```java
static int maxSum(int[] a) {
    int best = a[0], cur = a[0];
    for (int i = 1; i < a.length; i++) {
        cur = cur > 0 ? cur + a[i] : a[i];          // ▶ 前面是负担就重新开始（必挖）
        if (cur > best) best = cur;
    }
    return best;
}
```

```c
int maxSum(int a[], int n) {
    int best = a[0], cur = a[0];
    for (int i = 1; i < n; i++) {
        cur = cur > 0 ? cur + a[i] : a[i];
        if (cur > best) best = cur;
    }
    return best;
}
```

DP 判定（选择题）：**最优子结构 + 子问题重叠**；与分治区别=分治子问题独立、DP 子问题重叠且记表。

---

# 六、图算法

## 6.1 存储（选择题）

- 邻接矩阵：n² 空间，查边 O(1)，**适合稠密图**
- 邻接表：n+e 空间，查邻边 O(度)，**适合稀疏图**

## 6.2 DFS（栈/递归）与 BFS（队列）

```java
static void dfs(int[][] g, boolean[] vis, int u) {
    vis[u] = true;                                  // ▶ 先标记再访问（必挖）
    System.out.print(u + " ");
    for (int v = 0; v < g.length; v++)
        if (g[u][v] == 1 && !vis[v])                // ▶ 有边且未访问
            dfs(g, vis, v);
}
static void bfs(int[][] g, int start) {
    boolean[] vis = new boolean[g.length];
    java.util.Queue<Integer> q = new java.util.LinkedList<>();
    vis[start] = true; q.offer(start);              // ▶ 入队即标记
    while (!q.isEmpty()) {
        int u = q.poll();
        System.out.print(u + " ");
        for (int v = 0; v < g.length; v++)
            if (g[u][v] == 1 && !vis[v]) {
                vis[v] = true;                      // ▶ 标记后入队（必挖）
                q.offer(v);
            }
    }
}
```

```c
void dfs(int g[][100], int vis[], int n, int u) {
    vis[u] = 1;
    printf("%d ", u);
    for (int v = 0; v < n; v++)
        if (g[u][v] == 1 && !vis[v]) dfs(g, vis, n, v);
}
void bfs(int g[][100], int n, int start) {
    int vis[100] = {0}, q[100], head = 0, tail = 0;
    vis[start] = 1; q[tail++] = start;
    while (head < tail) {
        int u = q[head++];
        printf("%d ", u);
        for (int v = 0; v < n; v++)
            if (g[u][v] == 1 && !vis[v]) { vis[v] = 1; q[tail++] = v; }
    }
}
```

选择题：DFS 借助**栈**，BFS 借助**队列**；非连通图需要多次启动才能访问全部（森林）。

## 6.3 拓扑排序（AOV 网）

思路：反复①挑入度为 0 的点输出 ②删掉它及其出边。

```java
static void topoSort(int[][] g, int[] in, int n) {
    java.util.LinkedList<Integer> s = new java.util.LinkedList<>();
    for (int i = 0; i < n; i++) if (in[i] == 0) s.add(i);   // ▶ 入度0入队
    int cnt = 0;
    while (!s.isEmpty()) {
        int u = s.poll();
        System.out.print(u + " "); cnt++;
        for (int v = 0; v < n; v++)
            if (g[u][v] == 1 && --in[v] == 0)       // ▶ 删边：入度减到0就入队（必挖）
                s.add(v);
    }
    if (cnt < n) System.out.print("(有环)");
}
```

```c
void topoSort(int g[][100], int in[], int n) {
    int q[100], head = 0, tail = 0, cnt = 0;
    for (int i = 0; i < n; i++) if (in[i] == 0) q[tail++] = i;
    while (head < tail) {
        int u = q[head++]; cnt++;
        printf("%d ", u);
        for (int v = 0; v < n; v++)
            if (g[u][v] == 1 && --in[v] == 0) q[tail++] = v;
    }
    if (cnt < n) printf("(you huan)");
}
```

选择题：拓扑序列不唯一；**有环则无拓扑序列**；n 个顶点的有向无环图拓扑序列长度恰为 n。

## 6.4 Dijkstra（单源最短路，边权非负）

```java
static int[] dijkstra(int[][] g, int n, int src) {
    int[] dist = new int[n]; boolean[] done = new boolean[n];
    for (int i = 0; i < n; i++) dist[i] = g[src][i];        // ▶ 初始化为直达距离
    dist[src] = 0; done[src] = true;
    for (int k = 1; k < n; k++) {
        int u = -1, min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++)
            if (!done[i] && dist[i] < min) { min = dist[i]; u = i; }   // ▶ 挑最近的未确定点
        if (u < 0) break;
        done[u] = true;
            for (int v = 0; v < n; v++)
            if (!done[v] && g[u][v] < Integer.MAX_VALUE
                && dist[u] + g[u][v] < dist[v])              // ▶ 松弛（必挖）
                dist[v] = dist[u] + g[u][v];
    }
    return dist;
}
```

```c
#define INF 10000
void dijkstra(int g[][100], int n, int src) {
    int dist[100], done[100] = {0};
    for (int i = 0; i < n; i++) dist[i] = g[src][i];
    dist[src] = 0; done[src] = 1;
    for (int k = 1; k < n; k++) {
        int u = -1, min = INF;
        for (int i = 0; i < n; i++)
            if (!done[i] && dist[i] < min) { min = dist[i]; u = i; }
        if (u < 0) break;
        done[u] = 1;
        for (int v = 0; v < n; v++)
            if (!done[v] && dist[u] + g[u][v] < dist[v])
                dist[v] = dist[u] + g[u][v];
    }
}
```

O(n²)。选择题：**不能处理负权边**；全源最短路用 Floyd O(n³)。

## 6.5 Prim（点集合扩张，适合稠密）与 Kruskal（边集排序+并查集，适合稀疏）

```java
static int prim(int[][] g, int n) {          // g 用 INF 表示无边
    int[] low = new int[n]; boolean[] in = new boolean[n];
    int cost = 0;
    for (int i = 0; i < n; i++) low[i] = g[0][i];    // ▶ 从 0 号点开始
    in[0] = true;
    for (int k = 1; k < n; k++) {
        int u = -1, min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++)
            if (!in[i] && low[i] < min) { min = low[i]; u = i; }   // ▶ 离树最近的点
        in[u] = true; cost += min;
        for (int v = 0; v < n; v++)
            if (!in[v] && g[u][v] < low[v]) low[v] = g[u][v];      // ▶ 更新（必挖）
    }
    return cost;
}
```

```c
#define INF 10000
int prim(int g[][100], int n) {
    int low[100], in[100] = {0}, cost = 0;
    for (int i = 0; i < n; i++) low[i] = g[0][i];
    in[0] = 1;
    for (int k = 1; k < n; k++) {
        int u = -1, min = INF;
        for (int i = 0; i < n; i++)
            if (!in[i] && low[i] < min) { min = low[i]; u = i; }
        in[u] = 1; cost += min;
        for (int v = 0; v < n; v++)
            if (!in[v] && g[u][v] < low[v]) low[v] = g[u][v];
    }
    return cost;
}
```

Kruskal：边按权升序，逐条尝试加入，**不成环（并查集判）就要**，直到 n−1 条。
选择题：MST 可能不唯一（权有重复时）；**Prim=加点，Kruskal=加边**；都基于贪心。

## 6.6 关键路径（AOE 网，选择题）

- 顶点=事件，边=活动；**关键路径=最长路径**（决定总工期）
- 最早开始 ve：从源点往后推 ve[j]=max{ve[i]+w(i,j)}；最迟开始 vl：从汇点往前推 vl[i]=min{vl[j]−w(i,j)}
- 活动 e(i)=ve[起点]；l(i)=vl[终点]−w；**e=l 的活动是关键活动**
- 缩短工期只能压**关键路径**上的活动；关键路径可能不止一条

---

# 七、字符串匹配

## 7.1 朴素匹配 BF：O(n×m)。逐位对齐逐字比较，失配整体右移一位。

## 7.2 KMP

```java
static int[] getNext(String p) {                 // next[j] = p[0..j-1] 的最长相等前后缀
    int[] next = new int[p.length()];
    next[0] = -1;
    int k = -1, j = 0;
    while (j < p.length() - 1) {
        if (k == -1 || p.charAt(j) == p.charAt(k)) {
            k++; j++;
            next[j] = k;                          // ▶ 求next（必挖）
        } else k = next[k];                       // ▶ 失配回退（必挖）
    }
    return next;
}
static int kmp(String s, String p) {
    int[] next = getNext(p);
    int i = 0, j = 0;
    while (i < s.length() && j < p.length()) {
        if (j == -1 || s.charAt(i) == p.charAt(j)) { i++; j++; }
        else j = next[j];                         // ▶ 主串 i 不回退（KMP灵魂）
    }
    return j == p.length() ? i - j : -1;
}
```

```c
void getNext(char p[], int next[]) {
    int k = -1, j = 0, m = strlen(p);
    next[0] = -1;
    while (j < m - 1) {
        if (k == -1 || p[j] == p[k]) { k++; j++; next[j] = k; }
        else k = next[k];
    }
}
int kmp(char s[], char p[]) {
    int next[100], i = 0, j = 0, n = strlen(s), m = strlen(p);
    getNext(p, next);
    while (i < n && j < m) {
        if (j == -1 || s[i] == p[j]) { i++; j++; }
        else j = next[j];
    }
    return j == m ? i - j : -1;
}
```

O(n+m)。选择题：失配时**主串指针不回退**，模式串按 next 回退。

---

# 八、回溯法

```java
static void perm(int[] a, int k) {               // 全排列
    if (k == a.length - 1) {                     // ▶ 出口：排到最后一位
        System.out.println(java.util.Arrays.toString(a));
        return;
    }
    for (int i = k; i < a.length; i++) {
        int t = a[k]; a[k] = a[i]; a[i] = t;     // ▶ 换到第 k 位
        perm(a, k + 1);                          // ▶ 递归排后面
        t = a[k]; a[k] = a[i]; a[i] = t;         // ▶ 回溯：换回去（必挖）
    }
}
static boolean queens(int[] q, int row, int n) { // N皇后：q[r]=第r行放的列
    if (row == n) return true;
    for (int col = 0; col < n; col++) {
        boolean ok = true;
        for (int r = 0; r < row; r++)
            if (q[r] == col || Math.abs(q[r] - col) == row - r) {   // ▶ 同列/同对角线（必挖）
                ok = false; break;
            }
        if (ok) { q[row] = col; if (queens(q, row + 1, n)) return true; }
    }
    return false;
}
```

```c
void perm(int a[], int k, int n) {
    if (k == n - 1) { for (int i = 0; i < n; i++) printf("%d ", a[i]); printf("\n"); return; }
    for (int i = k; i < n; i++) {
        int t = a[k]; a[k] = a[i]; a[i] = t;
        perm(a, k + 1, n);
        t = a[k]; a[k] = a[i]; a[i] = t;
    }
}
int queens(int q[], int row, int n) {
    if (row == n) return 1;
    for (int col = 0; col < n; col++) {
        int ok = 1;
        for (int r = 0; r < row; r++)
            if (q[r] == col || abs(q[r] - col) == row - r) { ok = 0; break; }
        if (ok) { q[row] = col; if (queens(q, row + 1, n)) return 1; }
    }
    return 0;
}
```

要点：回溯=深度优先+**撤销选择**（状态恢复）；解空间树=排列树/子集树；N皇后 8 皇后有 92 解。

---

# 九、概率算法 / 近似算法 / NP（选择题摘要）

- **概率算法**：蒙特卡洛（结果带概率，可能错，如随机投点算 π）、拉斯维加斯（可能不返回但返回必对，如随机快排选基准）、舍伍德（消最坏输入影响，结果必对）。特征词："随机""投点""概率"。
- **近似算法**：NP 难问题求近似解，**性能比=近似解/最优解**（≥1），越接近 1 越好。
- **P/NP**：P=多项式时间**可求解**；NP=多项式时间**可验证**；NP 完全=NP 里最难的一类（SAT 是第一个 NPC 问题，货郎问题/背包都是 NPC）；P=是否等于 NP 未证明。
- 选择题口诀："**能解的 P、能验的 NP、最难 NPC**"。

---

# 十、大题④答题套路（C 算法填空 15 分怎么拿 8+）

**填空永远挖这几类（对照本文 ▶ 记位置）**：
1. **递归出口**：`if (n <= 1) return ...` / `if (lo >= hi) return`
2. **循环边界**：`i < n-1` 还是 `i <= n`、`j = i+1` 还是 `j = i`
3. **转移方程**：`f[i][j] = f[i-1][j-1] + 1`、`max(...)` 里三项
4. **交换三行**：`t=a[i]; a[i]=a[j]; a[j]=t`
5. **条件符号**：`<` / `<=` / `>=`（决定升序还是稳定）
6. **更新/回溯**：`last = i`、换回去的两行

**做题流程**：①先看题目标题和注释判断算法类型（本文 〇 节考频表）②手动模拟小样例（n=3、4）③空必与前后代码对称——**答案格式照抄邻行**（前一行是 `f[i-1][j-1]`，空处大概率同款下标运算）④填完整体读一遍当人肉编译器。

**练习路线（W4）**：16 卷④三题（LIS→字符串压缩→0-1背包）→ 本文 DP 节遮空重写 → 历年真题④两三套。目标 8+/15：5 个空拿 3 个稳、4 个正常、5 个超常。
