#!/usr/bin/env python3
"""
数据结构与算法错题复习练习脚本
涵盖：二叉树性质、栈队列、排序、查找、时间复杂度 ⭐复习重点
"""

import random

class 数据结构与算法复习:
    """数据结构与算法复习练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    # ========== 二叉树性质 ⭐重点必考 ==========
    
    def practice_n0_n2(self):
        """练习：n0 = n2 + 1 ⭐⭐⭐最重点"""
        print(f"\n【二叉树】叶子节点与度为2节点关系？")
        user_answer = input("你的答案（n0=?）：")
        correct = 'n2 + 1'
        
        self.total += 1
        if 'n2' in user_answer or 'n2+1' in user_answer or '加1' in user_answer:
            self.score += 1
            print(f"✅ 正确！n0 = n2 + 1 ⭐必背公式")
        else:
            print(f"❌ 错误！n0 = n2 + 1 ⭐必背公式")
    
    def practice_layer_max(self):
        """练习：第i层最多节点"""
        print(f"\n【二叉树】第i层最多多少节点？")
        user_answer = input("你的答案：")
        correct = '2^(i-1)'
        
        self.total += 1
        if '2' in user_answer and 'i' in user_answer:
            self.score += 1
            print(f"✅ 正确！第i层最多 2^(i-1) 个节点")
        else:
            print(f"❌ 错误！第i层最多 2^(i-1) 个节点")
    
    def practice_depth_max(self):
        """练习：深度k最多节点"""
        print(f"\n【二叉树】深度为k最多多少节点？")
        user_answer = input("你的答案：")
        correct = '2^k - 1'
        
        self.total += 1
        if '2' in user_answer and 'k' in user_answer and ('-1' in user_answer or '减1' in user_answer):
            self.score += 1
            print(f"✅ 正确！深度k最多 2^k - 1 个节点")
        else:
            print(f"❌ 错误！深度k最多 2^k - 1 个节点")
    
    def practice_calculate_n0(self):
        """练习：计算n0 ⭐重点"""
        print(f"\n【二叉树】n=100，求叶子节点数？")
        user_answer = input("你的答案：")
        correct = '50'
        
        self.total += 1
        if user_answer == '50':
            self.score += 1
            print(f"✅ 正确！n0=50")
            print("💡 解析：完全二叉树 n0 = ceil(n/2) = 50")
        else:
            print(f"❌ 错误！n0=50")
            print("💡 解析：完全二叉树 n0 = ceil(n/2)")
    
    def practice_full_vs_complete(self):
        """练习：满二叉树vs完全二叉树 ⭐重点"""
        print(f"\n【二叉树】完全二叉树特点？")
        user_answer = input("你的答案：")
        correct = '前k-1层满，最后一层从左到右'
        
        self.total += 1
        if '左' in user_answer or '满' in user_answer:
            self.score += 1
            print(f"✅ 正确！完全二叉树：前k-1层满，最后一层从左到右排列")
        else:
            print(f"❌ 错误！完全二叉树：前k-1层满，最后一层从左到右排列")
    
    def practice_traversal_determine(self):
        """练习：遍历序列确定二叉树 ⭐重点"""
        print(f"\n【二叉树】哪两种遍历能唯一确定二叉树？")
        user_answer = input("你的答案：")
        correct = '前序+中序，或后序+中序'
        
        self.total += 1
        if '中序' in user_answer:
            self.score += 1
            print(f"✅ 正确！必须包含中序：前序+中序 或 后序+中序")
        else:
            print(f"❌ 错误！必须包含中序：前序+中序 或 后序+中序")
    
    # ========== 栈和队列 ⭐重点 ==========
    
    def practice_stack_lifo(self):
        """练习：栈LIFO ⭐重点"""
        print(f"\n【栈】栈的特点？")
        user_answer = input("你的答案：")
        correct = '后进先出LIFO'
        
        self.total += 1
        if '后进' in user_answer or 'LIFO' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！栈：后进先出（LIFO）")
        else:
            print(f"❌ 错误！栈：后进先出（LIFO）")
    
    def practice_queue_fifo(self):
        """练习：队列FIFO ⭐重点"""
        print(f"\n【队列】队列的特点？")
        user_answer = input("你的答案：")
        correct = '先进先出FIFO'
        
        self.total += 1
        if '先进' in user_answer or 'FIFO' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！队列：先进先出（FIFO）")
        else:
            print(f"❌ 错误！队列：先进先出（FIFO）")
    
    def practice_stack_application(self):
        """练习：栈的应用 ⭐重点"""
        print(f"\n【栈】栈的应用场景有哪些？")
        user_answer = input("你的答案：")
        correct = ['递归', '表达式', '括号', '后退']
        
        self.total += 1
        if any(c in user_answer for c in correct):
            self.score += 1
            print(f"✅ 正确！栈应用：递归调用、表达式求值、括号匹配、浏览器后退")
        else:
            print(f"❌ 错误！栈应用：递归调用、表达式求值、括号匹配、浏览器后退")
    
    def practice_queue_application(self):
        """练习：队列的应用 ⭐重点"""
        print(f"\n【队列】队列的应用场景有哪些？")
        user_answer = input("你的答案：")
        correct = ['打印', '消息', '调度', '排队']
        
        self.total += 1
        if any(c in user_answer for c in correct):
            self.score += 1
            print(f"✅ 正确！队列应用：打印机任务、消息队列、进程调度")
        else:
            print(f"❌ 错误！队列应用：打印机任务、消息队列、进程调度")
    
    # ========== 排序算法 ⭐重点必考 ==========
    
    def practice_stable_sort(self):
        """练习：稳定排序 ⭐⭐⭐最重点"""
        print(f"\n【排序】稳定排序有哪些？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['冒泡', '插入', '归并', '基数']
        
        self.total += 1
        if any(c in user_answer for c in correct):
            self.score += 1
            print(f"✅ 正确！稳定排序：冒泡、插入、归并、基数 ⭐必背")
        else:
            print(f"❌ 错误！稳定排序：冒泡、插入、归并、基数 ⭐必背")
    
    def practice_unstable_sort(self):
        """练习：不稳定排序 ⭐⭐⭐最重点"""
        print(f"\n【排序】不稳定排序有哪些？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['快速', '选择', '堆', '希尔']
        
        self.total += 1
        if any(c in user_answer for c in correct):
            self.score += 1
            print(f"✅ 正确！不稳定排序：快速、选择、堆、希尔 ⭐必背")
        else:
            print(f"❌ 错误！不稳定排序：快速、选择、堆、希尔 ⭐必背")
    
    def practice_stable_nlogn(self):
        """练习：O(nlogn)且稳定 ⭐重点"""
        print(f"\n【排序】时间复杂度O(nlogn)且稳定？")
        user_answer = input("你的答案：")
        correct = '归并'
        
        self.total += 1
        if '归并' in user_answer:
            self.score += 1
            print(f"✅ 正确！归并排序：O(nlogn)且稳定 ⭐重点")
        else:
            print(f"❌ 错误！归并排序：O(nlogn)且稳定 ⭐重点")
    
    def practice_unstable_nlogn(self):
        """练习：O(nlogn)且不稳定 ⭐重点"""
        print(f"\n【排序】时间复杂度O(nlogn)且不稳定？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['快速', '堆']
        
        self.total += 1
        if '快速' in user_answer or '堆' in user_answer:
            self.score += 1
            print(f"✅ 正确！快速排序、堆排序：O(nlogn)且不稳定")
        else:
            print(f"❌ 错误！快速排序、堆排序：O(nlogn)且不稳定")
    
    def practice_quicksort_worst(self):
        """练习：快排最坏 ⭐重点"""
        print(f"\n【排序】快速排序最坏时间复杂度？")
        user_answer = input("你的答案：")
        correct = 'O(n^2)'
        
        self.total += 1
        if 'n2' in user_answer or '平方' in user_answer:
            self.score += 1
            print(f"✅ 正确！快排最坏O(n^2)，已排序时发生")
        else:
            print(f"❌ 错误！快排最坏O(n^2)，已排序时发生")
    
    # ========== 查找算法 ⭐重点 ==========
    
    def practice_binary_search_condition(self):
        """练习：二分查找条件 ⭐重点"""
        print(f"\n【查找】二分查找的前提条件？")
        user_answer = input("你的答案：")
        correct = '有序'
        
        self.total += 1
        if '有序' in user_answer or '顺序' in user_answer:
            self.score += 1
            print(f"✅ 正确！二分查找需要有序序列")
        else:
            print(f"❌ 错误！二分查找需要有序序列")
    
    def practice_binary_search_time(self):
        """练习：二分查找时间复杂度 ⭐重点"""
        print(f"\n【查找】二分查找时间复杂度？")
        user_answer = input("你的答案：")
        correct = 'O(log n)'
        
        self.total += 1
        if 'log' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！二分查找O(log n)")
        else:
            print(f"❌ 错误！二分查找O(log n)")
    
    def practice_binary_search_count(self):
        """练习：二分查找次数 ⭐重点"""
        print(f"\n【查找】n=100，二分查找最多几次？")
        user_answer = input("你的答案：")
        correct = '7'
        
        self.total += 1
        if user_answer == '7':
            self.score += 1
            print(f"✅ 正确！floor(log2(100))+1 = 6+1 = 7次")
        else:
            print(f"❌ 错误！floor(log2(100))+1 = 7次")
    
    # ========== 时间复杂度 ⭐重点 ==========
    
    def practice_time_order(self):
        """练习：时间复杂度排序 ⭐重点"""
        print(f"\n【时间复杂度】从小到大排序？")
        user_answer = input("你的答案（说出两个）：")
        correct = ['O(1)', 'O(log n)', 'O(n)', 'O(nlog n)', 'O(n^2)']
        
        self.total += 1
        if 'O(1)' in user_answer or '常数' in user_answer or 'log' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！O(1) < O(log n) < O(n) < O(nlog n) < O(n^2)")
        else:
            print(f"❌ 错误！O(1) < O(log n) < O(n) < O(nlog n) < O(n^2)")
    
    def practice_nested_loop_time(self):
        """练习：嵌套循环时间复杂度 ⭐重点"""
        print(f"\n【时间复杂度】两层嵌套循环？")
        user_answer = input("你的答案：")
        correct = 'O(n^2)'
        
        self.total += 1
        if 'n2' in user_answer or '平方' in user_answer:
            self.score += 1
            print(f"✅ 正确！两层循环O(n^2)")
        else:
            print(f"❌ 错误！两层循环O(n^2)")
    
    def practice_half_loop_time(self):
        """练习：每次减半循环 ⭐重点"""
        print(f"\n【时间复杂度】while(n>1){n/=2}？")
        user_answer = input("你的答案：")
        correct = 'O(log n)'
        
        self.total += 1
        if 'log' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！每次减半O(log n)")
        else:
            print(f"❌ 错误！每次减半O(log n)")
    
    # ========== 图的基础 ⭐重点 ==========
    
    def practice_dfs_structure(self):
        """练习：DFS用栈 ⭐重点"""
        print(f"\n【图】DFS用什么数据结构？")
        user_answer = input("你的答案：")
        correct = '栈'
        
        self.total += 1
        if '栈' in user_answer:
            self.score += 1
            print(f"✅ 正确！DFS使用栈（递归隐式栈）")
        else:
            print(f"❌ 错误！DFS使用栈（递归隐式栈）")
    
    def practice_bfs_structure(self):
        """练习：BFS用队列 ⭐重点"""
        print(f"\n【图】BFS用什么数据结构？")
        user_answer = input("你的答案：")
        correct = '队列'
        
        self.total += 1
        if '队列' in user_answer:
            self.score += 1
            print(f"✅ 正确！BFS使用队列")
        else:
            print(f"❌ 错误！BFS使用队列")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*50}")
        print(f"📊 复习完成！得分：{self.score}/{self.total}")
        if self.score == self.total:
            print("🎉 全对！数据结构与算法掌握很好！")
        elif self.score >= self.total * 0.8:
            print("👍 不错！继续巩固重点公式！")
        else:
            print("💪 还需努力！重点记住：n0=n2+1、稳定排序、DFS/BFS")
    
    def run(self):
        """运行练习"""
        print("="*50)
        print("数据结构与算法错题复习 ⭐重点")
        print("="*50)
        print("\n复习重点：")
        print("1. 二叉树性质（n0=n2+1）⭐⭐⭐最重点")
        print("2. 栈队列（LIFO/FIFO）⭐重点")
        print("3. 排序稳定性 ⭐⭐⭐最重点")
        print("4. 二分查找 ⭐重点")
        print("5. 时间复杂度 ⭐重点")
        print("6. DFS/BFS ⭐重点")
        print("7. 综合复习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择复习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                practices = [
                    self.practice_n0_n2,
                    self.practice_layer_max,
                    self.practice_calculate_n0,
                    self.practice_traversal_determine,
                ]
                for p in practices:
                    p()
            elif choice == '2':
                practices = [
                    self.practice_stack_lifo,
                    self.practice_queue_fifo,
                    self.practice_stack_application,
                    self.practice_queue_application,
                ]
                for p in practices:
                    p()
            elif choice == '3':
                practices = [
                    self.practice_stable_sort,
                    self.practice_unstable_sort,
                    self.practice_stable_nlogn,
                    self.practice_unstable_nlogn,
                    self.practice_quicksort_worst,
                ]
                for p in practices:
                    p()
            elif choice == '4':
                practices = [
                    self.practice_binary_search_condition,
                    self.practice_binary_search_time,
                    self.practice_binary_search_count,
                ]
                for p in practices:
                    p()
            elif choice == '5':
                practices = [
                    self.practice_time_order,
                    self.practice_nested_loop_time,
                    self.practice_half_loop_time,
                ]
                for p in practices:
                    p()
            elif choice == '6':
                practices = [
                    self.practice_dfs_structure,
                    self.practice_bfs_structure,
                ]
                for p in practices:
                    p()
            elif choice == '7':
                practices = [
                    self.practice_n0_n2,
                    self.practice_stable_sort,
                    self.practice_unstable_sort,
                    self.practice_stack_lifo,
                    self.practice_binary_search_time,
                    self.practice_dfs_structure,
                    self.practice_bfs_structure,
                ]
                for p in practices:
                    p()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    review = 数据结构与算法复习()
    review.run()