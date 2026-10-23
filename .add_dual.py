# -*- coding: utf-8 -*-
"""35号新增「📖 Java/C 对照」页签：T0五板块+回溯的双语代码示例，注入 s-dual 区块"""
import html, io, sys

JAVA = {}
C = {}

JAVA['pack'] = '''public class Pack {
    public static void main(String[] args){
        int[] w = {2,3,4,5};
        int[] v = {3,4,5,6};
        int C = 8, n = 4;
        int[][] dp = new int[n+1][C+1];
        for(int i = 1; i <= n; i++)
            for(int j = 0; j <= C; j++){
                dp[i][j] = dp[i-1][j];
                if(j >= w[i-1] && dp[i-1][j-w[i-1]] + v[i-1] > dp[i][j])
                    dp[i][j] = dp[i-1][j-w[i-1]] + v[i-1];
            }
        System.out.println(dp[n][C]);
    }
}'''

C['pack'] = '''#include <stdio.h>
int main(void){
    int w[4] = {2,3,4,5}, v[4] = {3,4,5,6};
    int C = 8, n = 4;
    int dp[5][9];                                /* dp[i][j] = 前i件、容量j的最大价值 */
    for(int j = 0; j <= C; j++) dp[0][j] = 0;
    for(int i = 1; i <= n; i++)
        for(int j = 0; j <= C; j++){
            dp[i][j] = dp[i-1][j];               /* 不放第 i 件 */
            if(j >= w[i-1] && dp[i-1][j-w[i-1]] + v[i-1] > dp[i][j])
                dp[i][j] = dp[i-1][j-w[i-1]] + v[i-1];   /* 放得下且更优才放 */
        }
    printf("%d\\n", dp[n][C]);
    return 0;
}'''

JAVA['bs'] = '''public class BSearch {
    public static void main(String[] args){
        int[] a = {1,3,5,7,9,11};
        int key = 7, lo = 0, hi = a.length - 1;
        while(lo <= hi){                         /* 循环继续的条件 */
            int mid = (lo + hi) / 2;
            if(a[mid] == key){ System.out.println("下标=" + mid); return; }
            else if(a[mid] < key) lo = mid + 1;
            else hi = mid - 1;
        }
        System.out.println("未找到");
    }
}'''
JAVA['bs'] = JAVA['bs'].replace('/* 循环继续的条件 */', '// ★热区：<= 而不是 <')

C['bs'] = '''#include <stdio.h>
int main(void){
    int a[6] = {1,3,5,7,9,11}, key = 7;
    int lo = 0, hi = 5;
    while(lo <= hi){                     /* ★热区：<= 而不是 < */
        int mid = (lo + hi) / 2;
        if(a[mid] == key){ printf("下标=%d\\n", mid); return 0; }
        else if(a[mid] < key) lo = mid + 1;   /* ★往右半 */
        else hi = mid - 1;                    /* ★往左半 */
    }
    printf("未找到\\n");
    return 0;
}'''

JAVA['act'] = '''public class Act {
    public static void main(String[] args){
        int[] s = {1, 3, 2, 5, 8};   /* 开始时间 */
        int[] f = {4, 5, 6, 7, 9};   /* 结束时间（已按 f 升序排列） */
        int count = 1, last = 0;     /* 先选第一个活动 */
        for(int i = 1; i < f.length; i++){
            if(s[i] >= f[last]){ count++; last = i; }
        }
        System.out.println("最多活动数=" + count);
    }
}'''
JAVA['act'] = JAVA['act'].replace('/* 开始时间 */', '// 开始时间').replace('/* 结束时间（已按 f 升序排列） */', '// 结束时间（已按 f 升序排列）').replace('/* 先选第一个活动 */', '// 先选第一个活动').replace('{ count++; last = i; }', '{ count++; last = i; }   // ★热区：>= 才不重叠')

C['act'] = '''#include <stdio.h>
int main(void){
    int s[5] = {1,3,2,5,8}, f[5] = {4,5,6,7,9};   /* 已按结束时间 f 升序 */
    int count = 1, last = 0;                       /* 先选第一个活动 */
    for(int i = 1; i < 5; i++)
        if(s[i] >= f[last]){ count++; last = i; }  /* ★热区：>= 才不重叠 */
    printf("最多活动数=%d\\n", count);
    return 0;
}'''

JAVA['fib'] = '''public class Fib {
    static long fibRec(int n){          // 递归 O(2^n)：出口 + 自调用
        if(n <= 1) return n;            // ★热区：出口
        return fibRec(n-1) + fibRec(n-2);
    }
    static long fibDp(int n){           // 递推 O(n)：打表
        long[] f = new long[n+2];
        f[0] = 0; f[1] = 1;
        for(int i = 2; i <= n; i++) f[i] = f[i-1] + f[i-2];
        return f[n];
    }
    public static void main(String[] args){
        System.out.println(fibRec(10) + " " + fibDp(10));
    }
}'''

C['fib'] = '''#include <stdio.h>
long fibRec(int n){                     /* 递归 O(2^n)：出口 + 自调用 */
    if(n <= 1) return n;                /* ★热区：出口 */
    return fibRec(n-1) + fibRec(n-2);
}
long fibDp(int n){                      /* 递推 O(n)：打表 */
    long f[25];
    f[0] = 0; f[1] = 1;
    for(int i = 2; i <= n; i++) f[i] = f[i-1] + f[i-2];
    return f[n];
}
int main(void){
    printf("%ld %ld\\n", fibRec(10), fibDp(10));
    return 0;
}'''

JAVA['rev'] = '''public class Rev {
    public static void main(String[] args){
        int[] a = {1,2,3,4,5};
        for(int i = 0, j = a.length - 1; i < j; i++, j--){
            int t = a[i]; a[i] = a[j]; a[j] = t;
        }
        for(int x : a) System.out.print(x + " ");
        System.out.println();
    }
}'''

C['rev'] = '''#include <stdio.h>
int main(void){
    int a[5] = {1,2,3,4,5};
    for(int i = 0, j = 4; i < j; i++, j--){    /* ★热区：i < j 双向逼近 */
        int t = a[i]; a[i] = a[j]; a[j] = t;   /* ★热区：交换三行 */
    }
    for(int i = 0; i < 5; i++) printf("%d ", a[i]);
    printf("\\n");
    return 0;
}'''

JAVA['nq'] = '''public class NQ {
    static int n = 4, count = 0;
    static int[] pos = new int[n];          /* pos[i] = 第 i 行皇后放的列 */
    static boolean ok(int row, int col){    /* ★热区：约束检查（同列/对角线） */
        for(int i = 0; i < row; i++)
            if(pos[i] == col || Math.abs(pos[i] - col) == row - i) return false;
        return true;
    }
    static void place(int row){             /* ★热区：逐行递归尝试 */
        if(row == n){ count++; return; }    /* 出口：放满 n 行 */
        for(int col = 0; col < n; col++)
            if(ok(row, col)){ pos[row] = col; place(row + 1); }
    }                                       /* for 循环结束即隐式回溯 */
    public static void main(String[] args){
        place(0);
        System.out.println("4皇后解数=" + count);
    }
}'''
JAVA['nq'] = JAVA['nq'].replace('/* pos[i] = 第 i 行皇后放的列 */', '// pos[i] = 第 i 行皇后放的列').replace('/* ★热区：约束检查（同列/对角线） */', '// ★热区：约束检查（同列/对角线）').replace('/* ★热区：逐行递归尝试 */', '// ★热区：逐行递归尝试').replace('/* 出口：放满 n 行 */', '// 出口：放满 n 行').replace('/* for 循环结束即隐式回溯 */', '// for 循环结束即隐式回溯')

C['nq'] = '''#include <stdio.h>
#include <stdlib.h>
int n = 4, count = 0, pos[4];               /* pos[i] = 第 i 行皇后放的列 */
int ok(int row, int col){                   /* ★热区：约束检查（同列/对角线） */
    for(int i = 0; i < row; i++)
        if(pos[i] == col || abs(pos[i] - col) == row - i) return 0;
    return 1;
}
void place(int row){                        /* ★热区：逐行递归尝试 */
    if(row == n){ count++; return; }        /* 出口：放满 n 行 */
    for(int col = 0; col < n; col++)
        if(ok(row, col)){ pos[row] = col; place(row + 1); }
}                                           /* for 循环结束即隐式回溯 */
int main(void){
    place(0);
    printf("4皇后解数=%d\\n", count);
    return 0;
}'''

BLOCKS = [
    ('1️⃣ 0-1 背包（动态规划 · T0 头牌）',
     '转移方程 dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)　★热区：不放/放两分支、j>=w[i-1] 边界　数据：4 件（重 2/3/4/5，值 3/4/5/6），容量 8',
     '10', 'pack'),
    ('2️⃣ 二分查找（分治与二分）',
     '前提：数组<b>有序</b>　★热区：lo<=hi、lo=mid+1、hi=mid-1 三处，填空最固定　复杂度 O(logn)',
     '下标=3', 'bs'),
    ('3️⃣ 活动安排（贪心 · 出镜率并列最高）',
     '按<b>结束时间升序</b>排好后，从头贪心：下一个的开始 ≥ 上一个的结束就选　★热区：s[i] >= f[last]　复杂度 O(n)（排序 O(nlogn)）',
     '最多活动数=3', 'act'),
    ('4️⃣ 斐波那契（递归递推 · 送分板块）',
     '同一算法两副面孔：递归 O(2ⁿ)（出口+自调用）vs 递推 O(n)（打表）　★热区：出口 n<=1、递推项 f[i-1]+f[i-2]',
     '55 55', 'fib'),
    ('5️⃣ 数组逆置（简单数据操作 · 双指针）',
     '首尾双指针向中间走，边走边交换　★热区：i<j、交换三行　复杂度 O(n)、空间 O(1)',
     '5 4 3 2 1', 'rev'),
    ('6️⃣ 4 皇后（回溯 · T1）',
     '三要素落地：逐行<b>递归尝试</b> → ok() <b>约束检查</b>（同列/对角线）→ for 走完自动<b>隐式回溯</b>　★热区：ok() 与 place() 递归行',
     '4皇后解数=2', 'nq'),
]

esc = lambda s: html.escape(s, quote=False)
parts = ['''<!-- ============ Tab1 Java/C 对照 ============ -->
<section id="s-dual">
 <div class="tip">T0 五板块 + 回溯的<b>双语对照示例</b>，★ = 大题④填空热区。<b>验证口径</b>：Java 版全部本机 javac 编译并运行实测（输出即页面标注值）；C 版本机无编译器，按 C99 语法人工精核，算法逻辑经同数据 Java 孪生程序实测一致。<b>对照读法</b>：先读 Java 理解算法，再看 C 熟悉语法皮（数组/循环/printf）——考试考的是"能读能填"，不是默写。</div>''']
for idx, (title, desc, out, key) in enumerate(BLOCKS):
    parts.append(f'''
 <div class="card">
  <h2>{title}</h2>
  <div class="tip">{desc}　→ <b>输出 {out}</b></div>
  <div style="font-size:12px;font-weight:700;margin:6px 0 2px;color:var(--acc)">Java 版（已实测）</div>
  <div class="code">{esc(JAVA[key])}</div>
  <div style="font-size:12px;font-weight:700;margin:8px 0 2px;color:var(--acc)">C 版</div>
  <div class="code">{esc(C[key])}</div>
 </div>''')
parts.append('\n</section>\n')
section = '\n'.join(parts)

p = '35-算法可视化.html'
src = io.open(p, encoding='utf-8').read()

anchor_sec = '<!-- ============ Tab1 考纲地图 ============ -->'
assert src.count(anchor_sec) == 1, '地图注释锚点异常'
src = src.replace(anchor_sec, section + '\n' + anchor_sec)

anchor_tab = "const SECTIONS = [['hot','🎯 考频重点'],['map','📋 考纲地图']"
new_tab = "const SECTIONS = [['hot','🎯 考频重点'],['dual','📖 Java/C 对照'],['map','📋 考纲地图']"
assert src.count(anchor_tab) == 1, 'SECTIONS 锚点异常'
src = src.replace(anchor_tab, new_tab)

io.open(p, 'w', encoding='utf-8', newline='\n').write(src)
print('s-dual 注入完成：6 个双语块')
