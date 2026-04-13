#!/usr/bin/env python3
"""
基础排序算法练习脚本
用于练习直接插入、冒泡、简单选择排序
"""

import random

class 基础排序练习:
    """基础排序练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
        
        # 排序算法对比数据
        self.sorts = {
            '直接插入': {'time': 'O(n²)', 'space': 'O(1)', 'stable': True},
            '冒泡排序': {'time': 'O(n²)', 'space': 'O(1)', 'stable': True},
            '简单选择': {'time': 'O(n²)', 'space': 'O(1)', 'stable': False},
        }
    
    def practice_insertion_stable(self):
        """练习：直接插入排序稳定性"""
        print(f"\n【题目】直接插入排序是稳定的吗？")
        user_answer = input("你的答案（稳定/不稳定）：")
        correct = '稳定'
        
        self.total += 1
        if user_answer == correct:
            self.score += 1
            print(f"✅ 正确！直接插入排序是稳定的")
        else:
            print(f"❌ 错误！直接插入排序是稳定的")
            print(f"   相等元素不会交换位置")
    
    def practice_bubble_stable(self):
        """练习：冒泡排序稳定性"""
        print(f"\n【题目】冒泡排序是稳定的吗？")
        user_answer = input("你的答案（稳定/不稳定）：")
        correct = '稳定'
        
        self.total += 1
        if user_answer == correct:
            self.score += 1
            print(f"✅ 正确！冒泡排序是稳定的")
        else:
            print(f"❌ 错误！冒泡排序是稳定的")
            print(f"   相等元素不交换，保持原有顺序")
    
    def practice_selection_stable(self):
        """练习：简单选择排序稳定性 ⭐重点"""
        print(f"\n【题目】简单选择排序是稳定的吗？")
        user_answer = input("你的答案（稳定/不稳定）：")
        correct = '不稳定'
        
        self.total += 1
        if user_answer == correct:
            self.score += 1
            print(f"✅ 正确！简单选择排序是不稳定的")
            print(f"   例：[3,3,1] → 选最小1交换到第一个位置")
            print(f"   结果：[1,3,3]，两个3的相对位置改变了")
        else:
            print(f"❌ 错误！简单选择排序是不稳定的")
            print(f"   原因：跨距离交换可能改变相等元素相对位置")
    
    def practice_time_complexity(self):
        """练习：时间复杂度"""
        sorts = ['直接插入', '冒泡排序', '简单选择']
        sort_name = random.choice(sorts)
        
        print(f"\n【题目】{sort_name}的时间复杂度是？")
        user_answer = input("你的答案：").upper()
        correct = 'O(N²)'
        
        self.total += 1
        if user_answer.replace(' ', '') == correct.replace(' ', ''):
            self.score += 1
            print(f"✅ 正确！{sort_name}时间复杂度O(n²)")
        else:
            print(f"❌ 错误！{sort_name}时间复杂度O(n²)")
    
    def practice_space_complexity(self):
        """练习：空间复杂度"""
        sorts = ['直接插入', '冒泡排序', '简单选择']
        sort_name = random.choice(sorts)
        
        print(f"\n【题目】{sort_name}的空间复杂度是？")
        user_answer = input("你的答案：").upper()
        correct = 'O(1)'
        
        self.total += 1
        if user_answer.replace(' ', '') == correct.replace(' ', ''):
            self.score += 1
            print(f"✅ 正确！{sort_name}空间复杂度O(1)")
        else:
            print(f"❌ 错误！{sort_name}空间复杂度O(1)")
    
    def practice_stable_sorts(self):
        """练习：哪些排序是稳定的 ⭐重点"""
        print(f"\n【题目】O(n²)时间复杂度的排序中，哪些是稳定的？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['直接插入', '冒泡排序', '插入', '冒泡']
        
        self.total += 1
        if any(c in user_answer for c in correct):
            self.score += 1
            print(f"✅ 正确！直接插入和冒泡排序是稳定的")
            print(f"   简单选择排序不稳定")
        else:
            print(f"❌ 错误！O(n²)稳定排序：直接插入、冒泡排序")
            print(f"   O(n²)不稳定排序：简单选择排序")
    
    def practice_unstable_sorts(self):
        """练习：哪些排序不稳定 ⭐重点"""
        print(f"\n【题目】O(n²)时间复杂度的排序中，哪个是不稳定的？")
        user_answer = input("你的答案：")
        correct = '简单选择'
        
        self.total += 1
        if '选择' in user_answer:
            self.score += 1
            print(f"✅ 正确！简单选择排序不稳定")
        else:
            print(f"❌ 错误！简单选择排序不稳定")
    
    def practice_best_case(self):
        """练习：最佳情况"""
        print(f"\n【题目】直接插入排序在什么情况下效率最高？")
        user_answer = input("你的答案：")
        correct = '基本有序'
        
        self.total += 1
        if '有序' in user_answer:
            self.score += 1
            print(f"✅ 正确！基本有序时效率最高")
            print(f"   原因：几乎不需要移动元素")
        else:
            print(f"❌ 错误！基本有序时效率最高")
    
    def practice_comparison(self):
        """练习：排序对比"""
        questions = [
            ('时间复杂度O(n²)的稳定排序有哪些？', '直接插入、冒泡排序'),
            ('时间复杂度O(n²)的不稳定排序有哪些？', '简单选择排序'),
            ('基本有序数据用什么排序效率高？', '直接插入排序'),
            ('简单排序中哪种交换次数最少？', '简单选择排序'),
            ('冒泡排序为什么稳定？', '相等元素不交换'),
            ('简单选择排序为什么不稳定？', '跨距离交换'),
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
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("基础排序算法练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 直接插入排序稳定性")
        print("2. 冒泡排序稳定性")
        print("3. 简单选择排序稳定性 ⭐重点")
        print("4. 时间复杂度")
        print("5. 空间复杂度")
        print("6. 哪些排序稳定 ⭐重点")
        print("7. 哪些排序不稳定 ⭐重点")
        print("8. 最佳情况")
        print("9. 排序对比")
        print("10. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_insertion_stable()
            elif choice == '2':
                self.practice_bubble_stable()
            elif choice == '3':
                self.practice_selection_stable()
            elif choice == '4':
                self.practice_time_complexity()
            elif choice == '5':
                self.practice_space_complexity()
            elif choice == '6':
                self.practice_stable_sorts()
            elif choice == '7':
                self.practice_unstable_sorts()
            elif choice == '8':
                self.practice_best_case()
            elif choice == '9':
                self.practice_comparison()
            elif choice == '10':
                types = [
                    self.practice_selection_stable,
                    self.practice_stable_sorts,
                    self.practice_unstable_sorts,
                    self.practice_comparison,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 基础排序练习()
    practice.run()