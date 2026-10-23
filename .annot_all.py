# -*- coding: utf-8 -*-
"""35号 s-dual 其余 9 例升级为逐行人话注释版：定位区块内全部20个代码块，按位替换第3~20个"""
import html, io, re

N = {}
N['lcs_j'] = '''public class Lcs {
    public static void main(String[] args){
        char[] a = "ABCBDAB".toCharArray();   // 字符串 a：7 个字符
        char[] b = "BDCABA".toCharArray();    // 字符串 b：6 个字符
        int m = a.length, n = b.length;
        // ★灵魂一行：dp[i][j] = a 的前 i 个字符 与 b 的前 j 个字符 的最长公共子序列长度
        //   (子序列=可以跳着挑但顺序不变；默认第0行/第0列全0：跟空串的LCS自然是0)
        int[][] dp = new int[m+1][n+1];
        for(int i = 1; i <= m; i++)           // a的第i个字符 = a[i-1]（下标错位）
            for(int j = 1; j <= n; j++){      // b的第j个字符 = b[j-1]
                if(a[i-1] == b[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;                 // ①末位相同 → 接上这个字符
                else
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]); // ②末位不同 → 丢一个，取大
            }
        System.out.println(dp[m][n]);   // 右下角 = 4（比如 B C B A）
    }
}'''
N['lcs_c'] = '''#include <stdio.h>
int main(void){
    char a[] = "ABCBDAB", b[] = "BDCABA";
    int m = 7, n = 6;
    int dp[8][7];               /* ★灵魂一行：dp[i][j] = a前i个 与 b前j个 的最长公共子序列长度 */
    for(int i = 0; i <= m; i++) dp[i][0] = 0;   /* 边界：b为空串 → LCS=0 */
    for(int j = 0; j <= n; j++) dp[0][j] = 0;   /* 边界：a为空串 → LCS=0 */
    for(int i = 1; i <= m; i++)                 /* a的第i个字符是a[i-1]（下标错位） */
        for(int j = 1; j <= n; j++){            /* b的第j个字符是b[j-1] */
            if(a[i-1] == b[j-1])
                dp[i][j] = dp[i-1][j-1] + 1;     /* ①末位相同 → 接上这个字符 */
            else{
                dp[i][j] = dp[i-1][j];            /* ②末位不同：丢a的末位 */
                if(dp[i][j-1] > dp[i][j])         /*    或丢b的末位，谁大取谁 */
                    dp[i][j] = dp[i][j-1];
            }
        }
    printf("%d\\n", dp[m][n]);   /* 右下角 = 4（比如 B C B A） */
    return 0;
}'''
N['tri_j'] = '''public class Tri {
    public static void main(String[] args){
        int[][] t = { {2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3} };
        //     2
        //    3 4        每个数只能走到下一行的"左下或右下"
        //   6 5 7
        //  4 1 8 3
        int n = 4;
        // ★灵魂一行：f[i][j] = 从位置(i,j)一路走到塔底 能累计的最大和
        int[][] f = new int[n][n];
        for(int j = 0; j < n; j++) f[n-1][j] = t[n-1][j];   // 底边：人已在底，值=自己（递推起点）
        for(int i = n - 2; i >= 0; i--)                     // ★热区：自底向上填表（倒着推）
            for(int j = 0; j <= i; j++)                     // 第 i 行只有 i+1 个数
                // 站在(i,j)：下一脚要么左下 f[i+1][j]，要么右下 f[i+1][j+1]，挑大的踩
                f[i][j] = t[i][j] + Math.max(f[i+1][j], f[i+1][j+1]);
        System.out.println(f[0][0]);   // 塔尖 = 21（路径 2→4→7→8）
    }
}'''
N['tri_c'] = '''#include <stdio.h>
int main(void){
    int t[4][4] = {{2}, {3,4}, {6,5,7}, {4,1,8,3}};   /* 缺省元素自动补0 */
    int f[4][4], n = 4;
    /* ★灵魂一行：f[i][j] = 从位置(i,j)一路走到塔底能累计的最大和 */
    for(int j = 0; j < n; j++) f[n-1][j] = t[n-1][j];  /* 底边：人已在底，值=自己（递推起点） */
    for(int i = n - 2; i >= 0; i--)                    /* ★热区：自底向上填表（倒着推） */
        for(int j = 0; j <= i; j++){                   /* 第i行只有i+1个数 */
            int better = f[i+1][j] > f[i+1][j+1] ? f[i+1][j] : f[i+1][j+1];
            f[i][j] = t[i][j] + better;                /* ★左下/右下挑大的踩（C无max用三目） */
        }
    printf("%d\\n", f[0][0]);   /* 塔尖 = 21（路径 2→4→7→8） */
    return 0;
}'''
N['lis_j'] = '''public class Lis {
    public static void main(String[] args){
        int[] a = {3, 1, 4, 1, 5, 9, 2, 6};
        int n = a.length, best = 0;      // best = 全程见过的最大 f[i]
        // ★灵魂一行：f[i] = "以 a[i] 结尾"(必须选上a[i])的最长递增子序列长度
        //   为什么锁结尾？——只有锁定结尾，才能从前面"比它小"的位置接上去
        int[] f = new int[n];
        for(int i = 0; i < n; i++){
            f[i] = 1;                    // 保底：自己一个也算长度 1
            for(int j = 0; j < i; j++)   // 扫描 i 左边每个位置：看能接在谁后面
                if(a[j] < a[i] && f[j] + 1 > f[i])   // ★a[j]<a[i] 才可接；接上更长才更新
                    f[i] = f[j] + 1;
            if(f[i] > best) best = f[i]; // ★答案 = 所有 f[i] 的最大值（不一定在最后一位！）
        }
        System.out.println(best);        // 4（如 1 4 5 9 或 3 4 5 9）
    }
}'''
N['lis_c'] = '''#include <stdio.h>
int main(void){
    int a[8] = {3,1,4,1,5,9,2,6}, n = 8, best = 0;   /* best = 全程见过的最大f[i] */
    /* ★灵魂一行：f[i] = "以a[i]结尾"(必须选上a[i])的最长递增子序列长度 */
    int f[8];
    for(int i = 0; i < n; i++){
        f[i] = 1;                                /* 保底：自己一个也算长度1 */
        for(int j = 0; j < i; j++)               /* 扫描i左边每个位置：能接在谁后面 */
            if(a[j] < a[i] && f[j] + 1 > f[i])   /* ★a[j]<a[i]才可接；接上更长才更新 */
                f[i] = f[j] + 1;
        if(f[i] > best) best = f[i];             /* ★答案=所有f[i]的最大值（不一定在最后一位！） */
    }
    printf("%d\\n", best);        /* 4（如 1 4 5 9 或 3 4 5 9） */
    return 0;
}'''
N['ms_j'] = '''public class Ms {
    public static void main(String[] args){
        int[] a = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int n = a.length;
        // ★灵魂一行：f = "以当前元素 a[i] 结尾"(必须含a[i])的最大子段和
        //   ans = 全程出现过的最大 f（真正的答案要靠它保存）
        int f = a[0], ans = a[0];
        for(int i = 1; i < n; i++){
            // 决策：前面的积累 f 是正资产 → 接上(f+a[i])；是负资产 → 扔掉，从 a[i] 自立门户
            f = Math.max(a[i], f + a[i]);    // ★热区：一句话转移
            if(f > ans) ans = f;             // 每步看一眼，最大值可能出现在任何位置
        }
        System.out.println(ans);             // 6（子段 4,-1,2,1）
    }
}'''
N['ms_c'] = '''#include <stdio.h>
int main(void){
    int a[9] = {-2,1,-3,4,-1,2,1,-5,4}, n = 9;
    /* ★灵魂一行：f = "以当前元素a[i]结尾"(必须含a[i])的最大子段和；ans = 全程最大f */
    int f = a[0], ans = a[0];
    for(int i = 1; i < n; i++){
        /* 决策：前面是正资产就接上(f+a[i])；是负资产就扔掉，从a[i]自立门户 */
        f = f + a[i] > a[i] ? f + a[i] : a[i];   /* ★热区：一句话转移（C无max用三目） */
        if(f > ans) ans = f;                     /* 每步看一眼，最大值可能在任何位置 */
    }
    printf("%d\\n", ans);         /* 6（子段 4,-1,2,1） */
    return 0;
}'''
N['bs_j'] = '''public class Bs {
    public static void main(String[] args){
        int[] a = {1,3,5,7,9,11};        // ★前提：数组必须有序！乱序二分没有意义
        int key = 7;                     // 要找的数
        int lo = 0, hi = a.length - 1;   // lo/hi = 当前搜索范围的左右边界（闭区间）

        while(lo <= hi){                 // ★热区：范围还有东西（哪怕只剩1个）就继续
            int mid = (lo + hi) / 2;     // 砍一半，看中间那位
            if(a[mid] == key){           // 运气好：中间正好是它
                System.out.println("下标=" + mid);
                return;                  // 找到就收工
            }else if(a[mid] < key)
                lo = mid + 1;            // ★中间比目标小 → 目标只可能在右半，扔掉左半
            else
                hi = mid - 1;            // ★中间比目标大 → 扔掉右半
        }
        System.out.println("未找到");    // 走到这里 lo>hi：范围空了 → 不存在
    }
}'''
N['bs_c'] = '''#include <stdio.h>
int main(void){
    int a[6] = {1,3,5,7,9,11};       /* ★前提：数组必须有序！乱序二分没有意义 */
    int key = 7;                     /* 要找的数 */
    int lo = 0, hi = 5;              /* lo/hi = 当前搜索范围的左右边界（闭区间） */
    while(lo <= hi){                 /* ★热区：范围还有东西（哪怕只剩1个）就继续 */
        int mid = (lo + hi) / 2;     /* 砍一半，看中间那位 */
        if(a[mid] == key){           /* 运气好：中间正好是它 */
            printf("下标=%d\\n", mid);
            return 0;                /* 找到就收工 */
        }else if(a[mid] < key)
            lo = mid + 1;            /* ★中间比目标小 → 目标只可能在右半，扔掉左半 */
        else
            hi = mid - 1;            /* ★中间比目标大 → 扔掉右半 */
    }
    printf("未找到\\n");              /* 走到这里 lo>hi：范围空了 → 不存在 */
    return 0;
}'''
N['act_j'] = '''public class Act {
    public static void main(String[] args){
        int[] s = {1, 3, 2, 5, 8};   // 各活动的开始时间
        int[] f = {4, 5, 6, 7, 9};   // 各活动的结束时间 —— ★必须已按结束时间升序（贪心前提）
        // 贪心策略：结束越早的活动给后面留的空间越多 → 结束早的先选

        int count = 1, last = 0;     // 第一个(结束最早)无条件先选；last = 最后选中活动的下标
        for(int i = 1; i < f.length; i++){
            // ★热区：第 i 个活动的开始 ≥ 上一个选中活动的结束 → 不冲突，选它
            if(s[i] >= f[last]){ count++; last = i; }
        }
        System.out.println("最多活动数=" + count);   // 3（选了 (1,4)(5,7)(8,9)）
    }
}'''
N['act_c'] = '''#include <stdio.h>
int main(void){
    int s[5] = {1,3,2,5,8};      /* 各活动的开始时间 */
    int f[5] = {4,5,6,7,9};      /* 各活动的结束时间 —— ★必须已按结束时间升序（贪心前提） */
    /* 贪心策略：结束越早的活动给后面留的空间越多 → 结束早的先选 */
    int count = 1, last = 0;     /* 第一个(结束最早)无条件先选；last=最后选中活动的下标 */
    for(int i = 1; i < 5; i++)
        if(s[i] >= f[last]){ count++; last = i; }   /* ★热区：开始≥上一个的结束 → 不冲突，选它 */
    printf("最多活动数=%d\\n", count);   /* 3（选了 (1,4)(5,7)(8,9)） */
    return 0;
}'''
N['fib_j'] = '''public class Fib {
    static long fibRec(int n){               // 版本A：递归 —— 直接翻译定义 f(n)=f(n-1)+f(n-2)
        if(n <= 1) return n;                 // ★热区：出口（n=0返0，n=1返1）
        return fibRec(n-1) + fibRec(n-2);    // 自己调自己两次 → 大量重复计算，O(2^n)
    }

    static long fibDp(int n){                // 版本B：递推(DP) —— 从小到大打表，每个只算一次
        long[] f = new long[n+2];            // f[] 就是"表"：存中间结果避免重复算
        f[0] = 0; f[1] = 1;                  // 初始条件（=递归的出口）
        for(int i = 2; i <= n; i++)          // 从小到大：算 f[i] 时前两项已现成
            f[i] = f[i-1] + f[i-2];          // ★热区：递推式与递归式一模一样
        return f[n];                         // O(n)：快就快在"算过的不再算"
    }

    public static void main(String[] args){
        System.out.println(fibRec(10) + " " + fibDp(10));   // 两版答案相同：55 55
    }
}'''
N['fib_c'] = '''#include <stdio.h>
long fibRec(int n){                      /* 版本A：递归 —— 直接翻译定义 f(n)=f(n-1)+f(n-2) */
    if(n <= 1) return n;                 /* ★热区：出口（n=0返0，n=1返1） */
    return fibRec(n-1) + fibRec(n-2);    /* 自己调自己两次 → 大量重复计算，O(2^n) */
}
long fibDp(int n){                       /* 版本B：递推(DP) —— 从小到大打表，每个只算一次 */
    long f[25];                          /* f[] 就是"表"：存中间结果避免重复算 */
    f[0] = 0; f[1] = 1;                  /* 初始条件（=递归的出口） */
    for(int i = 2; i <= n; i++)          /* 从小到大：算f[i]时前两项已现成 */
        f[i] = f[i-1] + f[i-2];          /* ★热区：递推式与递归式一模一样 */
    return f[n];                         /* O(n)：快就快在"算过的不再算" */
}
int main(void){
    printf("%ld %ld\\n", fibRec(10), fibDp(10));   /* 两版答案相同：55 55 */
    return 0;
}'''
N['rev_j'] = '''public class Rev {
    public static void main(String[] args){
        int[] a = {1,2,3,4,5};
        // 双指针：i 从左往右，j 从右往左，向中间走
        for(int i = 0, j = a.length - 1; i < j; i++, j--){
            // ★热区：i<j 就继续 —— 相遇即停（奇数个时中间那个不用动）
            int t = a[i]; a[i] = a[j]; a[j] = t;   // ★热区：交换三行（借中间变量 t）
        }
        for(int x : a) System.out.print(x + " ");  // 输出 5 4 3 2 1
        System.out.println();
    }
}'''
N['rev_c'] = '''#include <stdio.h>
int main(void){
    int a[5] = {1,2,3,4,5};
    /* 双指针：i从左往右，j从右往左，向中间走 */
    for(int i = 0, j = 4; i < j; i++, j--){    /* ★热区：i<j就继续 —— 相遇即停（奇数个中间不动） */
        int t = a[i]; a[i] = a[j]; a[j] = t;   /* ★热区：交换三行（借中间变量t） */
    }
    for(int i = 0; i < 5; i++) printf("%d ", a[i]);   /* 输出 5 4 3 2 1 */
    printf("\\n");
    return 0;
}'''
N['nq_j'] = '''public class Nq {
    static int n = 4, count = 0;
    static int[] pos = new int[n];       // pos[i] = 第 i 行皇后放在哪一列（每行恰好一个）

    static boolean ok(int row, int col){ // ★热区：约束检查 —— (row,col)能放吗？
        for(int i = 0; i < row; i++)     // 逐个检查上面已放好的每一行
            // 两种冲突：同列(pos[i]==col)；对角线(|列差|==|行差|)
            if(pos[i] == col || Math.abs(pos[i] - col) == row - i) return false;
        return true;                     // 跟谁都不冲突 → 可放
    }

    static void place(int row){          // ★热区：逐行递归尝试 —— 一次只处理一行
        if(row == n){ count++; return; } // 出口：0~n-1 行全放完 → 找到一解
        for(int col = 0; col < n; col++) // 本行从第 0 列试到第 n-1 列
            if(ok(row, col)){            // 这一列不冲突 → 放上，去下一行
                pos[row] = col;
                place(row + 1);
            }                            // for 自然走完 = 所有列试尽 = ★隐式回溯
    }

    public static void main(String[] args){
        place(0);                        // 从第 0 行开始放
        System.out.println("4皇后解数=" + count);   // 2
    }
}'''
N['nq_c'] = '''#include <stdio.h>
#include <stdlib.h>
int n = 4, count = 0, pos[4];               /* pos[i] = 第i行皇后放在哪一列（每行恰好一个） */
int ok(int row, int col){                   /* ★热区：约束检查 —— (row,col)能放吗？ */
    for(int i = 0; i < row; i++)            /* 逐个检查上面已放好的每一行 */
        if(pos[i] == col || abs(pos[i] - col) == row - i) return 0;   /* 同列/对角线冲突 */
    return 1;
}
void place(int row){                        /* ★热区：逐行递归尝试 —— 一次只处理一行 */
    if(row == n){ count++; return; }        /* 出口：0~n-1行全放完 → 找到一解 */
    for(int col = 0; col < n; col++)        /* 本行从第0列试到第n-1列 */
        if(ok(row, col)){                   /* 这列不冲突 → 放上，去下一行 */
            pos[row] = col;
            place(row + 1);
        }                                    /* for自然走完 = 所有列试尽 = ★隐式回溯 */
}
int main(void){
    place(0);                                /* 从第0行开始放 */
    printf("4皇后解数=%d\\n", count);   /* 2 */
    return 0;
}'''

ORDER = ['lcs_j','lcs_c','tri_j','tri_c','lis_j','lis_c','ms_j','ms_c',
         'bs_j','bs_c','act_j','act_c','fib_j','fib_c','rev_j','rev_c','nq_j','nq_c']

esc = lambda s: html.escape(s, quote=False)
p = '35-算法可视化.html'
src = io.open(p, encoding='utf-8').read()

s0 = src.index('<!-- ============ Tab1 Java/C 对照 ============ -->')
s1 = src.index('<!-- ============ Tab1 考纲地图 ============ -->')
sec = src[s0:s1]

ms = list(re.finditer(r'<div class="code">.*?</div>', sec, re.S))
assert len(ms) == 20, f'代码块数量异常: {len(ms)}'

new_sec, last = [], 0
for idx, m in enumerate(ms):
    new_sec.append(sec[last:m.start()])
    if idx >= 2:   # 前两个(背包 Java/C)已是注释版，跳过
        new_sec.append('<div class="code">' + esc(N[ORDER[idx-2]]) + '</div>')
    else:
        new_sec.append(m.group(0))
    last = m.end()
new_sec.append(sec[last:])
src = src[:s0] + ''.join(new_sec) + src[s1:]

io.open(p, 'w', encoding='utf-8', newline='\n').write(src)
print('9 例 18 个代码块已替换为逐行注释版')
