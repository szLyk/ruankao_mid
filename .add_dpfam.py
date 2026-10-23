# -*- coding: utf-8 -*-
"""35号 s-dual 追加 DP 家族四连（LCS/数字三角形/LIS/最大子段和），插入到 0-1 背包卡之后，老卡编号顺延"""
import html, io

JAVA = {}
C = {}

JAVA['lcs'] = '''public class LCS {
    public static void main(String[] args){
        char[] a = "ABCBDAB".toCharArray(), b = "BDCABA".toCharArray();
        int m = a.length, n = b.length;
        int[][] dp = new int[m+1][n+1];   // dp[i][j] = a 前 i 个与 b 前 j 个的 LCS 长度
        for(int i = 1; i <= m; i++)
            for(int j = 1; j <= n; j++){
                if(a[i-1] == b[j-1])
                    dp[i][j] = dp[i-1][j-1] + 1;                 // ★热区：末位相同 → 接上
                else
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]); // ★末位不同 → 丢一个
            }
        System.out.println(dp[m][n]);
    }
}'''

C['lcs'] = '''#include <stdio.h>
int main(void){
    char a[] = "ABCBDAB", b[] = "BDCABA";
    int m = 7, n = 6;
    int dp[8][7];                                    /* dp[i][j] = a前i个与b前j个的LCS长度 */
    for(int i = 0; i <= m; i++) dp[i][0] = 0;        /* 边界：空串 LCS = 0 */
    for(int j = 0; j <= n; j++) dp[0][j] = 0;
    for(int i = 1; i <= m; i++)
        for(int j = 1; j <= n; j++){
            if(a[i-1] == b[j-1])
                dp[i][j] = dp[i-1][j-1] + 1;          /* ★热区：末位相同 → 接上 */
            else{
                dp[i][j] = dp[i-1][j];                /* ★末位不同 → 丢一个，取大 */
                if(dp[i][j-1] > dp[i][j]) dp[i][j] = dp[i][j-1];
            }
        }
    printf("%d\\n", dp[m][n]);
    return 0;
}'''

JAVA['tri'] = '''public class Tri {
    public static void main(String[] args){
        int[][] t = { {2}, {3, 4}, {6, 5, 7}, {4, 1, 8, 3} };
        int n = 4;
        int[][] f = new int[n][n];                    // f[i][j] = 从(i,j)走到底的最大和
        for(int j = 0; j < n; j++) f[n-1][j] = t[n-1][j];   // 底边就是初始值
        for(int i = n - 2; i >= 0; i--)               // ★热区：自底向上填表
            for(int j = 0; j <= i; j++)
                f[i][j] = t[i][j] + Math.max(f[i+1][j], f[i+1][j+1]);  // ★左下/右下取优
        System.out.println(f[0][0]);
    }
}'''

C['tri'] = '''#include <stdio.h>
int main(void){
    int t[4][4] = {{2}, {3,4}, {6,5,7}, {4,1,8,3}};   /* 缺省元素自动补 0 */
    int f[4][4], n = 4;
    for(int j = 0; j < n; j++) f[n-1][j] = t[n-1][j];  /* 底边初始化 */
    for(int i = n - 2; i >= 0; i--)                    /* ★热区：自底向上填表 */
        for(int j = 0; j <= i; j++){
            int better = f[i+1][j] > f[i+1][j+1] ? f[i+1][j] : f[i+1][j+1];
            f[i][j] = t[i][j] + better;                /* ★左下/右下取优（C 无 max，用三目） */
        }
    printf("%d\\n", f[0][0]);
    return 0;
}'''

JAVA['lis'] = '''public class LIS {
    public static void main(String[] args){
        int[] a = {3, 1, 4, 1, 5, 9, 2, 6};
        int n = a.length, best = 0;
        int[] f = new int[n];                // f[i] = 以 a[i] 结尾的最长递增子序列长度
        for(int i = 0; i < n; i++){
            f[i] = 1;                        // 至少包含自己
            for(int j = 0; j < i; j++)
                if(a[j] < a[i] && f[j] + 1 > f[i])   // ★热区：a[i] 能接在 a[j] 后面
                    f[i] = f[j] + 1;
            if(f[i] > best) best = f[i];     // ★热区：答案 = 所有 f[i] 的最大值
        }
        System.out.println(best);
    }
}'''

C['lis'] = '''#include <stdio.h>
int main(void){
    int a[8] = {3,1,4,1,5,9,2,6}, n = 8, best = 0;
    int f[8];                                    /* f[i] = 以 a[i] 结尾的 LIS 长度 */
    for(int i = 0; i < n; i++){
        f[i] = 1;                                /* 至少包含自己 */
        for(int j = 0; j < i; j++)
            if(a[j] < a[i] && f[j] + 1 > f[i])   /* ★热区：能接在 a[j] 后面 */
                f[i] = f[j] + 1;
        if(f[i] > best) best = f[i];             /* ★答案 = 所有 f[i] 的最大值 */
    }
    printf("%d\\n", best);
    return 0;
}'''

JAVA['ms'] = '''public class MS {
    public static void main(String[] args){
        int[] a = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
        int n = a.length;
        int f = a[0], ans = a[0];            // f = 以 a[i] 结尾的最大子段和
        for(int i = 1; i < n; i++){
            f = Math.max(a[i], f + a[i]);    // ★热区：接上前缀 or 自立门户
            if(f > ans) ans = f;
        }
        System.out.println(ans);
    }
}'''

C['ms'] = '''#include <stdio.h>
int main(void){
    int a[9] = {-2,1,-3,4,-1,2,1,-5,4}, n = 9;
    int f = a[0], ans = a[0];               /* f = 以 a[i] 结尾的最大子段和 */
    for(int i = 1; i < n; i++){
        f = f + a[i] > a[i] ? f + a[i] : a[i];  /* ★热区：接上前缀 or 自立门户 */
        if(f > ans) ans = f;
    }
    printf("%d\\n", ans);
    return 0;
}'''

BLOCKS = [
    ('2️⃣ LCS 最长公共子序列（DP 家族·字符串类，2014下同族）',
     '状态 dp[i][j] = a 前 i 个与 b 前 j 个的 LCS 长度　★转移：末位相同 <b>dp[i-1][j-1]+1</b>，不同 <b>max(上, 左)</b>　边界：第 0 行/列 = 0　复杂度 O(mn)',
     '4', 'lcs'),
    ('3️⃣ 数字三角形（DP 家族·路径类，2017上/2019上同族）',
     '状态 f[i][j] = 从 (i,j) 走到底的最大和　★转移：<b>自底向上</b>，f[i][j] = t[i][j] + max(左下, 右下)　答案 = f[0][0]　复杂度 O(n²)',
     '21', 'tri'),
    ('4️⃣ LIS 最长递增子序列（DP 家族·序列类）',
     '状态 f[i] = <b>以 a[i] 结尾</b>的 LIS 长度　★转移：扫描 i 前面每个 j，能接就 f[i]=max(f[j]+1)　答案 = max(f[i)]——注意答案不在最后一个元素，在全程最大　复杂度 O(n²)',
     '4', 'lis'),
    ('5️⃣ 最大子段和（DP 家族·序列类，Kadane 一遍过）',
     '状态 f = 以当前元素结尾的最大子段和　★转移：max(a[i], f+a[i])——前面攒的是正资产就接，负资产就扔　答案 = 过程最大 f　复杂度 O(n)',
     '6', 'ms'),
]

esc = lambda s: html.escape(s, quote=False)
cards = []
for title, desc, out, key in BLOCKS:
    cards.append(f'''
 <div class="card">
  <h2>{title}</h2>
  <div class="tip">{desc}　→ <b>输出 {out}</b></div>
  <div style="font-size:12px;font-weight:700;margin:6px 0 2px;color:var(--acc)">Java 版（已实测）</div>
  <div class="code">{esc(JAVA[key])}</div>
  <div style="font-size:12px;font-weight:700;margin:8px 0 2px;color:var(--acc)">C 版</div>
  <div class="code">{esc(C[key])}</div>
 </div>''')
insertion = '\n'.join(cards)

p = '35-算法可视化.html'
src = io.open(p, encoding='utf-8').read()

# 1) 老卡编号顺延（降序替换防串号）
for old, new in [('6️⃣', '9️⃣'), ('5️⃣', '8️⃣'), ('4️⃣', '7️⃣'), ('3️⃣', '6️⃣'), ('2️⃣', '5️⃣')]:
    assert src.count(old) == 1, f'编号 {old} 出现次数异常: {src.count(old)}'
    src = src.replace(old, new)

# 2) 插入到（已顺延的）二分卡之前
anchor = '\n <div class="card">\n  <h2>5️⃣ 二分查找（分治与二分）</h2>'
assert src.count(anchor) == 1, '二分卡锚点异常'
src = src.replace(anchor, insertion + anchor)

# 3) 顶部口径文案更新
tip_old = 'T0 五板块 + 回溯的<b>双语对照示例</b>'
tip_new = 'T0 五板块（<b>DP 家族四连</b>：0-1 背包 / LCS / 数字三角形 / LIS / 最大子段和——背包见 1️⃣）+ 回溯的<b>双语对照示例</b>'
assert src.count(tip_old) == 1, 'tip 锚点异常'
src = src.replace(tip_old, tip_new)

io.open(p, 'w', encoding='utf-8', newline='\n').write(src)
print('DP 家族四连注入完成：s-dual 现共 10 卡')
