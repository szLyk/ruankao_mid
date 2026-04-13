#!/usr/bin/env python3
"""
图的遍历练习脚本
用于练习DFS和BFS
"""

import random
from collections import deque

class 图遍历练习:
    """图遍历练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
        
        # 示例图
        self.example_graphs = [
            # 图1: 1-2-3-4-5 链式
            {
                'name': '链式图',
                'graph': '1-2-3-4-5',
                'dfs_from_1': '1 2 3 4 5',
                'bfs_from_1': '1 2 3 4 5'
            },
            # 图2: 星形图（1为中心）
            {
                'name': '星形图',
                'graph': '1连接2,3,4,5',
                'dfs_from_1': '1 2 3 4 5',
                'bfs_from_1': '1 2 3 4 5'
            },
        ]
    
    def practice_dfs_implementation(self):
        """练习：DFS用什么实现"""
        print(f"\n【题目】深度优先搜索DFS用什么数据结构实现？")
        user_answer = input("你的答案：")
        correct_answers = ['栈', 'stack', '递归', 'recursion']
        
        self.total += 1
        if user_answer.lower() in [a.lower() for a in correct_answers]:
            self.score += 1
            print(f"✅ 正确！DFS用栈或递归实现")
        else:
            print(f"❌ 错误！DFS用栈或递归实现")
            print(f"   DFS：深入探索，后进先出，用栈")
    
    def practice_bfs_implementation(self):
        """练习：BFS用什么实现"""
        print(f"\n【题目】广度优先搜索BFS用什么数据结构实现？")
        user_answer = input("你的答案：")
        correct_answers = ['队列', 'queue']
        
        self.total += 1
        if user_answer.lower() in [a.lower() for a in correct_answers]:
            self.score += 1
            print(f"✅ 正确！BFS用队列实现")
        else:
            print(f"❌ 错误！BFS用队列实现")
            print(f"   BFS：按层次遍历，先进先出，用队列")
    
    def practice_dfs_vs_bfs(self):
        """练习：DFS与BFS对比"""
        questions = [
            ('DFS的特点是什么？', '深入探索，沿一条路径深入到底再回溯'),
            ('BFS的特点是什么？', '按层次遍历，逐层探索'),
            ('无权图最短路径用什么算法？', 'BFS'),
            ('拓扑排序用什么算法？', 'DFS'),
            ('连通性检测用什么算法？', 'DFS或BFS都可以'),
        ]
        
        question, correct = random.choice(questions)
        
        print(f"\n【题目】{question}")
        user_answer = input("你的答案：")
        
        self.total += 1
        if user_answer.strip() in correct:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
    
    def practice_dfs_sequence(self):
        """练习：DFS遍历序列"""
        # 简单图的DFS序列判断
        print(f"\n【题目】给定图结构：")
        print("    A")
        print("   /|\\")
        print("  B C D")
        print("  |")
        print("  E")
        print(f"\n从A开始DFS遍历，可能的序列是？")
        print("（假设邻接点顺序为B,C,D）")
        user_answer = input("你的答案（如：A B E C D）：").upper().replace(' ', '')
        
        # DFS可能结果（取决于邻接点顺序）
        correct = 'ABECD'
        
        self.total += 1
        if user_answer == correct:
            self.score += 1
            print(f"✅ 正确！DFS序列是 A B E C D")
        else:
            print(f"❌ 错误！DFS序列是 A B E C D")
            print(f"   DFS过程：")
            print(f"   1. 访问A")
            print(f"   2. 访问A的第一个邻接点B")
            print(f"   3. 访问B的邻接点E")
            print(f"   4. E无邻接点，回溯到B")
            print(f"   5. B无其他邻接点，回溯到A")
            print(f"   6. 访问A的下一个邻接点C")
            print(f"   7. 访问A的下一个邻接点D")
    
    def practice_bfs_sequence(self):
        """练习：BFS遍历序列"""
        print(f"\n【题目】给定图结构：")
        print("    A")
        print("   /|\\")
        print("  B C D")
        print("  |")
        print("  E")
        print(f"\n从A开始BFS遍历，序列是？")
        print("（假设邻接点顺序为B,C,D）")
        user_answer = input("你的答案（如：A B C D E）：").upper().replace(' ', '')
        
        correct = 'ABCDE'
        
        self.total += 1
        if user_answer == correct:
            self.score += 1
            print(f"✅ 正确！BFS序列是 A B C D E")
        else:
            print(f"❌ 错误！BFS序列是 A B C D E")
            print(f"   BFS过程：")
            print(f"   1. 访问A，A入队")
            print(f"   2. A出队，访问A的邻接点B,C,D，入队")
            print(f"   3. B出队，访问B的邻接点E，入队")
            print(f"   4. C,D,E依次出队（无新邻接点）")
    
    def practice_dfs_application(self):
        """练习：DFS应用场景"""
        scenarios = [
            ('拓扑排序', True),
            ('检测环', True),
            ('路径查找', True),
            ('最短路径（无权）', False),
            ('任务调度', False),
        ]
        
        scenario, correct = random.choice(scenarios)
        
        print(f"\n【题目】{scenario}是否适合用DFS？")
        user_answer = input("你的答案（适合/不适合）：")
        
        self.total += 1
        expected = "适合" if correct else "不适合"
        
        if user_answer == expected:
            self.score += 1
            print(f"✅ 正确！答案确实是 {expected}")
        else:
            print(f"❌ 错误！正确答案是 {expected}")
            if correct:
                print(f"   DFS应用：拓扑排序、检测环、路径查找")
            else:
                print(f"   最短路径用BFS，任务调度用队列")
    
    def practice_bfs_application(self):
        """练习：BFS应用场景"""
        scenarios = [
            ('无权图最短路径', True),
            ('层次遍历', True),
            ('连通性检测', True),
            ('拓扑排序', False),
            ('递归实现', False),
        ]
        
        scenario, correct = random.choice(scenarios)
        
        print(f"\n【题目】{scenario}是否适合用BFS？")
        user_answer = input("你的答案（适合/不适合）：")
        
        self.total += 1
        expected = "适合" if correct else "不适合"
        
        if user_answer == expected:
            self.score += 1
            print(f"✅ 正确！答案确实是 {expected}")
        else:
            print(f"❌ 错误！正确答案是 {expected}")
            if correct:
                print(f"   BFS应用：最短路径、层次遍历、连通性检测")
            else:
                print(f"   拓扑排序用DFS，递归是DFS的实现方式")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("图的遍历练习（DFS/BFS）")
        print("="*40)
        print("\n练习内容：")
        print("1. DFS实现方式")
        print("2. BFS实现方式")
        print("3. DFS与BFS对比")
        print("4. DFS遍历序列")
        print("5. BFS遍历序列")
        print("6. DFS应用场景")
        print("7. BFS应用场景")
        print("8. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_dfs_implementation()
            elif choice == '2':
                self.practice_bfs_implementation()
            elif choice == '3':
                self.practice_dfs_vs_bfs()
            elif choice == '4':
                self.practice_dfs_sequence()
            elif choice == '5':
                self.practice_bfs_sequence()
            elif choice == '6':
                self.practice_dfs_application()
            elif choice == '7':
                self.practice_bfs_application()
            elif choice == '8':
                types = [
                    self.practice_dfs_implementation,
                    self.practice_bfs_implementation,
                    self.practice_dfs_vs_bfs,
                    self.practice_dfs_application,
                    self.practice_bfs_application,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 图遍历练习()
    practice.run()