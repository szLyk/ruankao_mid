#!/usr/bin/env python3
"""
二叉树基础练习脚本
用于练习二叉树性质计算
"""

import random
import math

class 二叉树练习:
    """二叉树练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_property1(self):
        """练习：性质1 - 第i层最多节点数"""
        i = random.randint(1, 6)
        
        print(f"\n【题目】二叉树第{i}层最多有多少个节点？")
        user_answer = int(input("你的答案："))
        correct_answer = 2 ** (i - 1)
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   性质1：第i层最多 2^(i-1) 个节点")
    
    def practice_property2(self):
        """练习：性质2 - 深度k最多节点数"""
        k = random.randint(1, 5)
        
        print(f"\n【题目】深度为{k}的二叉树最多有多少个节点？")
        user_answer = int(input("你的答案："))
        correct_answer = 2 ** k - 1
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   性质2：深度k最多 2^k - 1 个节点")
    
    def practice_property3(self):
        """练习：性质3 - n0 = n2 + 1 ⭐重点"""
        n2 = random.randint(0, 50)
        
        print(f"\n【题目】二叉树中度为2的节点数n2={n2}，叶子节点数n0是多少？")
        user_answer = int(input("你的答案："))
        correct_answer = n2 + 1
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   性质3 ⭐重点：n0 = n2 + 1")
    
    def practice_property3_reverse(self):
        """练习：性质3反向 - 给n0求n2"""
        n0 = random.randint(1, 51)
        
        print(f"\n【题目】二叉树叶子节点数n0={n0}，度为2的节点数n2是多少？")
        user_answer = int(input("你的答案："))
        correct_answer = n0 - 1
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   性质3：n0 = n2 + 1，所以 n2 = n0 - 1")
    
    def practice_total_nodes(self):
        """练习：总节点数计算"""
        n0 = random.randint(10, 50)
        n1 = random.randint(0, 10)
        
        print(f"\n【题目】二叉树n0={n0}, n1={n1}, 求总节点数n？")
        user_answer = int(input("你的答案："))
        
        n2 = n0 - 1
        correct_answer = n0 + n1 + n2
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   计算步骤：")
            print(f"   1. n2 = n0 - 1 = {n2}")
            print(f"   2. n = n0 + n1 + n2 = {n0} + {n1} + {n2} = {correct_answer}")
    
    def practice_depth(self):
        """练习：性质4 - 完全二叉树深度"""
        n = random.choice([15, 31, 63, 100, 127, 50])
        
        print(f"\n【题目】{n}个节点的完全二叉树深度是多少？")
        user_answer = int(input("你的答案："))
        correct_answer = int(math.log2(n)) + 1
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   性质4：深度 = ⌊log₂n⌋ + 1")
            print(f"   log₂{n} ≈ {math.log2(n):.2f}")
            print(f"   ⌊log₂{n}⌋ = {int(math.log2(n))}")
    
    def practice_node_number(self):
        """练习：性质5 - 完全二叉树节点编号"""
        i = random.randint(1, 50)
        
        questions = [
            (f"完全二叉树节点{i}的父节点编号是？", i // 2),
            (f"完全二叉树节点{i}的左孩子编号是？（若存在）", 2 * i),
            (f"完全二叉树节点{i}的右孩子编号是？（若存在）", 2 * i + 1),
        ]
        
        question, correct = random.choice(questions)
        
        print(f"\n【题目】{question}")
        user_answer = int(input("你的答案："))
        
        self.total += 1
        if user_answer == correct:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
            print(f"   性质5：")
            print(f"   父节点 = ⌊i/2⌋")
            print(f"   左孩子 = 2i")
            print(f"   右孩子 = 2i+1")
    
    def practice_full_vs_complete(self):
        """练习：满二叉树vs完全二叉树"""
        questions = [
            ('深度为4的满二叉树有多少个节点？', 15),
            ('深度为5的满二叉树有多少个节点？', 31),
            ('满二叉树是否是完全二叉树？', '是'),
            ('完全二叉树是否一定是满二叉树？', '不一定'),
        ]
        
        question, correct = random.choice(questions)
        
        print(f"\n【题目】{question}")
        user_answer = input("你的答案：")
        
        self.total += 1
        if str(user_answer).strip() == str(correct):
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
            print(f"   满二叉树：每层节点都达到最大")
            print(f"   完全二叉树：除最后一层外每层节点最大，最后一层节点集中左边")
            print(f"   满二叉树是完全二叉树的特例")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("二叉树基础练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 性质1：第i层最多节点")
        print("2. 性质2：深度k最多节点")
        print("3. 性质3：n0 = n2 + 1 ⭐重点")
        print("4. 性质3反向：给n0求n2")
        print("5. 总节点数计算")
        print("6. 完全二叉树深度")
        print("7. 节点编号关系")
        print("8. 满二叉树vs完全二叉树")
        print("9. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_property1()
            elif choice == '2':
                self.practice_property2()
            elif choice == '3':
                self.practice_property3()
            elif choice == '4':
                self.practice_property3_reverse()
            elif choice == '5':
                self.practice_total_nodes()
            elif choice == '6':
                self.practice_depth()
            elif choice == '7':
                self.practice_node_number()
            elif choice == '8':
                self.practice_full_vs_complete()
            elif choice == '9':
                types = [
                    self.practice_property3,
                    self.practice_property3_reverse,
                    self.practice_total_nodes,
                    self.practice_depth,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 二叉树练习()
    practice.run()