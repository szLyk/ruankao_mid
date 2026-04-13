#!/usr/bin/env python3
"""
查找算法练习脚本
用于练习顺序查找、二分查找
"""

import random
import math

class 查找算法练习:
    """查找算法练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_sequential_complexity(self):
        """练习：顺序查找时间复杂度"""
        print(f"\n【题目】顺序查找的时间复杂度是？")
        user_answer = input("你的答案：").upper()
        correct = 'O(N)'
        
        self.total += 1
        if user_answer.replace(' ', '') == correct.replace(' ', ''):
            self.score += 1
            print(f"✅ 正确！顺序查找时间复杂度是 O(n)")
        else:
            print(f"❌ 错误！顺序查找时间复杂度是 O(n)")
            print(f"   顺序查找逐个比较，最坏需要n次")
    
    def practice_binary_complexity(self):
        """练习：二分查找时间复杂度 ⭐重点"""
        print(f"\n【题目】二分查找的时间复杂度是？")
        user_answer = input("你的答案：").upper()
        correct = 'O(LOGN)'
        
        self.total += 1
        if user_answer.replace(' ', '').replace('LOG', 'LOG') in correct.replace(' ', '').replace('LOG', 'LOG'):
            self.score += 1
            print(f"✅ 正确！二分查找时间复杂度是 O(log n)")
        else:
            print(f"❌ 错误！二分查找时间复杂度是 O(log n)")
            print(f"   二分查找每次缩小一半范围")
    
    def practice_binary_condition(self):
        """练习：二分查找前提条件 ⭐重点"""
        print(f"\n【题目】二分查找的前提条件是？")
        user_answer = input("你的答案：")
        correct = '有序表'
        
        self.total += 1
        if '有序' in user_answer or '排序' in user_answer:
            self.score += 1
            print(f"✅ 正确！二分查找前提是有序表")
        else:
            print(f"❌ 错误！二分查找前提是有序表")
            print(f"   无序表只能用顺序查找")
    
    def practice_binary_storage(self):
        """练习：二分查找存储要求"""
        print(f"\n【题目】二分查找仅适用于什么存储结构？")
        user_answer = input("你的答案：")
        correct = '顺序存储'
        
        self.total += 1
        if '顺序' in user_answer or '数组' in user_answer:
            self.score += 1
            print(f"✅ 正确！二分查找仅适用于顺序存储（数组）")
        else:
            print(f"❌ 错误！二分查找仅适用于顺序存储（数组）")
            print(f"   链表无法直接访问中间元素")
    
    def practice_binary_count(self):
        """练习：二分查找次数计算 ⭐重点"""
        n = random.choice([100, 50, 200, 1000, 15, 31])
        
        print(f"\n【题目】{n}个有序元素，二分查找最多需要比较几次？")
        user_answer = int(input("你的答案："))
        correct = math.ceil(math.log2(n + 1))
        
        self.total += 1
        if user_answer == correct:
            self.score += 1
            print(f"✅ 正确！最多比较 {correct} 次")
        else:
            print(f"❌ 错误！最多比较 {correct} 次")
            print(f"   公式：⌈log₂(n+1)⌉")
            print(f"   log₂({n+1}) ≈ {math.log2(n+1):.2f}")
            print(f"   ⌈log₂({n+1})⌉ = {correct}")
    
    def practice_sequential_vs_binary(self):
        """练习：顺序查找vs二分查找"""
        questions = [
            ('无序表用什么查找？', '顺序查找'),
            ('有序表用什么查找效率更高？', '二分查找'),
            ('链表用什么查找？', '顺序查找'),
            ('数组有序用什么查找？', '二分查找'),
            ('顺序查找最佳情况比较次数？', '1次'),
            ('顺序查找最坏情况比较次数？', 'n次'),
            ('二分查找最佳情况比较次数？', '1次'),
            ('二分查找最坏情况比较次数？', 'log₂n次'),
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
    
    def practice_binary_example(self):
        """练习：二分查找实例"""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        target = 7
        
        print(f"\n【题目】有序数组：{arr}")
        print(f"查找元素{target}，第一次比较的是哪个元素？")
        user_answer = int(input("你的答案："))
        
        mid = len(arr) // 2  # 中间位置
        
        self.total += 1
        if user_answer == arr[mid]:
            self.score += 1
            print(f"✅ 正确！第一次比较的是 arr[4] = {arr[mid]}")
        else:
            print(f"❌ 错误！第一次比较的是 arr[4] = {arr[mid]}")
            print(f"   mid = (0 + 7) / 2 = 4")
            print(f"   arr[4] = 9")
            print(f"   7 < 9，继续在左半部分查找")
    
    def practice_binary_find_process(self):
        """练习：二分查找过程"""
        arr = [1, 3, 5, 7, 9, 11, 13, 15]
        target = 7
        
        print(f"\n【题目】有序数组：{arr}")
        print(f"查找元素{target}，写出查找过程")
        print(f"格式：每次比较的元素")
        user_answer = input("你的答案（如：9,5,7）：")
        
        correct = '9,5,7'
        
        self.total += 1
        if user_answer.replace(' ', '') == correct.replace(' ', ''):
            self.score += 1
            print(f"✅ 正确！查找过程：")
            print(f"   1. mid=4, arr[4]=9, 7<9，左半部分")
            print(f"   2. mid=2, arr[2]=5, 7>5，右半部分")
            print(f"   3. mid=3, arr[3]=7, 找到！")
        else:
            print(f"❌ 错误！查找过程：")
            print(f"   1. mid=4, arr[4]=9, 7<9，左半部分")
            print(f"   2. mid=2, arr[2]=5, 7>5，右半部分")
            print(f"   3. mid=3, arr[3]=7, 找到！")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("查找算法练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 顺序查找时间复杂度")
        print("2. 二分查找时间复杂度 ⭐重点")
        print("3. 二分查找前提条件 ⭐重点")
        print("4. 二分查找存储要求")
        print("5. 二分查找次数计算 ⭐重点")
        print("6. 顺序vs二分对比")
        print("7. 二分查找实例")
        print("8. 二分查找过程")
        print("9. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_sequential_complexity()
            elif choice == '2':
                self.practice_binary_complexity()
            elif choice == '3':
                self.practice_binary_condition()
            elif choice == '4':
                self.practice_binary_storage()
            elif choice == '5':
                self.practice_binary_count()
            elif choice == '6':
                self.practice_sequential_vs_binary()
            elif choice == '7':
                self.practice_binary_example()
            elif choice == '8':
                self.practice_binary_find_process()
            elif choice == '9':
                types = [
                    self.practice_binary_complexity,
                    self.practice_binary_condition,
                    self.practice_binary_count,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 查找算法练习()
    practice.run()