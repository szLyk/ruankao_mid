# -*- coding: utf-8 -*-
"""35号 1️⃣0-1背包卡：Java/C 代码替换为逐行人话注释版（逻辑与已实测版完全一致，注释重排）"""
import html, io

OLD_JAVA = '''public class Pack {
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

OLD_C = '''#include <stdio.h>
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

NEW_JAVA = '''public class Pack {
    public static void main(String[] args){
        int[] w = {2,3,4,5};   // w = 每件物品的重量：件1占2、件2占3、件3占4、件4占5
        int[] v = {3,4,5,6};   // v = 每件物品的价值：装进去分别值 3、4、5、6
        int C = 8, n = 4;      // C = 背包总容量；n = 物品件数

        // ★灵魂一行：dp[i][j] = "只准从前 i 件里挑、限重 j" 时能拿到的最大价值
        //   行 i = 已考虑前几件；列 j = 背包限重。new int 全 0 → 第 0 行(一件不看)天然为 0
        int[][] dp = new int[n+1][C+1];

        for(int i = 1; i <= n; i++)          // 把第 i 件物品拿到桌面上来决策
            for(int j = 0; j <= C; j++){     // 对每种限重档位 j 都重新决策一遍

                // ①不拿：答案 = 只看前 i-1 件的旧答案，照抄上一行同列
                dp[i][j] = dp[i-1][j];

                // ②试拿：j >= w[i-1] 才装得下(w数组从0编号,第i件是w[i-1])；
                //   拿 = 腾出 w[i-1] 空间(查 dp[i-1][j-w[i-1]]) 再加价值 v[i-1]；
                //   新成绩 > 不拿 → 覆盖。★两分支取 max 就是这一整个 if
                if(j >= w[i-1] && dp[i-1][j-w[i-1]] + v[i-1] > dp[i][j])
                    dp[i][j] = dp[i-1][j-w[i-1]] + v[i-1];
            }
        // 右下角 = "4件随便挑、限重8"的最大价值 → 10（方案：件2+件4）
        System.out.println(dp[n][C]);
    }
}'''

NEW_C = '''#include <stdio.h>
int main(void){
    int w[4] = {2,3,4,5}, v[4] = {3,4,5,6};    /* w=重量 v=价值 */
    int C = 8, n = 4;                          /* C=背包总容量 n=件数 */
    int dp[5][9];              /* ★灵魂一行：dp[i][j] = 只准从前i件挑、限重j的最大价值 */
    for(int j = 0; j <= C; j++) dp[0][j] = 0;  /* 第0行：一件不看，价值全0 */
    for(int i = 1; i <= n; i++)                /* 把第i件拿到桌面上来决策 */
        for(int j = 0; j <= C; j++){           /* 对每种限重j都决策一遍 */
            dp[i][j] = dp[i-1][j];             /* ①不拿：照抄上一行同列的旧答案 */
            /* ②试拿：装得下(j>=w[i-1]) 且 拿了更优(腾出w[i-1]查旧表+价值v[i-1]) */
            if(j >= w[i-1] && dp[i-1][j-w[i-1]] + v[i-1] > dp[i][j])
                dp[i][j] = dp[i-1][j-w[i-1]] + v[i-1];
        }
    printf("%d\\n", dp[n][C]);  /* 右下角=答案10（方案：件2+件4） */
    return 0;
}'''

esc = lambda s: html.escape(s, quote=False)
p = '35-算法可视化.html'
src = io.open(p, encoding='utf-8').read()

for old, new in [(OLD_JAVA, NEW_JAVA), (OLD_C, NEW_C)]:
    o, n = esc(old), esc(new)
    assert src.count(o) == 1, '锚点出现次数异常: ' + o[:40]
    src = src.replace(o, n)

io.open(p, 'w', encoding='utf-8', newline='\n').write(src)
print('0-1背包卡已替换为逐行注释版')
