#!/usr/bin/env python3
"""
二叉树遍历练习脚本
用于练习前序、中序、后序、层序遍历
"""

import random

class 二叉树遍历练习:
    """二叉树遍历练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
        
        # 示例二叉树
        self.example_trees = [
            # 树1: A( B(D,E), C(F) )
            {
                'tree': '      A\n     / \\\\ \n    B   C\n   / \\\\   \\\\ \n  D   E   F',
                'preorder': 'A B D E C F',
                'inorder': 'D B E A C F',
                'postorder': 'D E B F C A',
                'levelorder': 'A B C D E F'
            },
            # 树2: A( B, C(D,E) )
            {
                'tree': '      A\n     / \\\\ \n    B   C\n       / \\\\ \n      D   E',
                'preorder': 'A B C D E',
                'inorder': 'B A D C E',
                'postorder': 'B D E C A',
                'levelorder': 'A B C D E'
            },
            # 树3: A( B(D), C )
            {
                'tree': '      A\n     / \\\\ \n    B   C\n   /\n  D',
                'preorder': 'A B D C',
                'inorder': 'D B A C',
                'postorder': 'D B C A',
                'levelorder': 'A B C D'
            },
        ]
    
    def practice_preorder(self):
        """练习：前序遍历"""
        tree = random.choice(self.example_trees)
        
        print(f"\n【题目】给定二叉树结构：")
        print(tree['tree'])
        print(f"请写出前序遍历结果（根-左-右）")
        user_answer = input("你的答案：").replace(' ', '').upper()
        correct_answer = tree['preorder'].replace(' ', '')
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {tree['preorder']}")
        else:
            print(f"❌ 错误！正确答案是 {tree['preorder']}")
            print(f"   前序遍历：根 → 左 → 右")
    
    def practice_inorder(self):
        """练习：中序遍历"""
        tree = random.choice(self.example_trees)
        
        print(f"\n【题目】给定二叉树结构：")
        print(tree['tree'])
        print(f"请写出中序遍历结果（左-根-右）")
        user_answer = input("你的答案：").replace(' ', '').upper()
        correct_answer = tree['inorder'].replace(' ', '')
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {tree['inorder']}")
        else:
            print(f"❌ 错误！正确答案是 {tree['inorder']}")
            print(f"   中序遍历：左 → 根 → 右")
    
    def practice_postorder(self):
        """练习：后序遍历"""
        tree = random.choice(self.example_trees)
        
        print(f"\n【题目】给定二叉树结构：")
        print(tree['tree'])
        print(f"请写出后序遍历结果（左-右-根）")
        user_answer = input("你的答案：").replace(' ', '').upper()
        correct_answer = tree['postorder'].replace(' ', '')
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {tree['postorder']}")
        else:
            print(f"❌ 错误！正确答案是 {tree['postorder']}")
            print(f"   后序遍历：左 → 右 → 根")
    
    def practice_reconstruct(self):
        """练习：由遍历序列还原二叉树 ⭐重点"""
        problems = [
            {
                'preorder': 'ABDECF',
                'inorder': 'DBEACF',
                'tree': '      A\n     / \\\\ \n    B   C\n   / \\\\   \\\\ \n  D   E   F',
                'postorder': 'DEBFCA'
            },
            {
                'preorder': 'ABCDE',
                'inorder': 'BADCE',
                'tree': '      A\n     / \\\\ \n    B   C\n       / \\\\ \n      D   E',
                'postorder': 'BDECA'
            },
            {
                'preorder': 'ABDC',
                'inorder': 'DBAC',
                'tree': '      A\n     / \\\\ \n    B   C\n   /\n  D',
                'postorder': 'DBCA'
            },
        ]
        
        problem = random.choice(problems)
        
        print(f"\n【题目】给定遍历序列：")
        print(f"前序：{problem['preorder']}")
        print(f"中序：{problem['inorder']}")
        print(f"请写出后序遍历结果")
        user_answer = input("你的答案：").replace(' ', '').upper()
        correct_answer = problem['postorder']
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
            print(f"   二叉树结构：")
            print(problem['tree'])
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   还原方法：")
            print(f"   1. 前序找根（第一个元素）")
            print(f"   2. 中序分左右（根左边是左子树，右边是右子树）")
            print(f"   3. 递归处理")
            print(f"   二叉树结构：")
            print(problem['tree'])
    
    def practice_unique_determine(self):
        """练习：唯一确定二叉树的条件"""
        questions = [
            ('前序+中序能否唯一确定二叉树？', '能'),
            ('后序+中序能否唯一确定二叉树？', '能'),
            ('前序+后序能否唯一确定二叉树？', '不能'),
            ('只有前序能否确定二叉树？', '不能'),
            ('只有中序能否确定二叉树？', '不能'),
        ]
        
        question, correct = random.choice(questions)
        
        print(f"\n【题目】{question}")
        user_answer = input("你的答案（能/不能）：")
        
        self.total += 1
        if user_answer == correct:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
            print(f"   关键结论：")
            print(f"   前序+中序 → 能唯一确定")
            print(f"   后序+中序 → 能唯一确定")
            print(f"   前序+后序 → 不能唯一确定（缺少中序信息）")
    
    def practice_levelorder(self):
        """练习：层序遍历"""
        tree = random.choice(self.example_trees)
        
        print(f"\n【题目】给定二叉树结构：")
        print(tree['tree'])
        print(f"请写出层序遍历结果（从上到下，从左到右）")
        user_answer = input("你的答案：").replace(' ', '').upper()
        correct_answer = tree['levelorder'].replace(' ', '')
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {tree['levelorder']}")
        else:
            print(f"❌ 错误！正确答案是 {tree['levelorder']}")
            print(f"   层序遍历：从上到下，从左到右")
            print(f"   用队列实现")
    
    def practice_traversal_order(self):
        """练习：遍历顺序记忆"""
        orders = [
            ('前序遍历顺序', '根-左-右'),
            ('中序遍历顺序', '左-根-右'),
            ('后序遍历顺序', '左-右-根'),
        ]
        
        order, correct = random.choice(orders)
        
        print(f"\n【题目】{order}是？")
        user_answer = input("你的答案（如：根-左-右）：")
        
        self.total += 1
        if user_answer.replace(' ', '') == correct.replace(' ', ''):
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("二叉树遍历练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 前序遍历（根-左-右）")
        print("2. 中序遍历（左-根-右）")
        print("3. 后序遍历（左-右-根）")
        print("4. 遍历序列还原二叉树 ⭐重点")
        print("5. 唯一确定二叉树的条件")
        print("6. 层序遍历")
        print("7. 遍历顺序记忆")
        print("8. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_preorder()
            elif choice == '2':
                self.practice_inorder()
            elif choice == '3':
                self.practice_postorder()
            elif choice == '4':
                self.practice_reconstruct()
            elif choice == '5':
                self.practice_unique_determine()
            elif choice == '6':
                self.practice_levelorder()
            elif choice == '7':
                self.practice_traversal_order()
            elif choice == '8':
                types = [
                    self.practice_reconstruct,
                    self.practice_unique_determine,
                    self.practice_preorder,
                    self.practice_inorder,
                    self.practice_postorder,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 二叉树遍历练习()
    practice.run()