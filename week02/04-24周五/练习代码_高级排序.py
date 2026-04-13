#!/usr/bin/env python3
"""
高级排序算法练习脚本
用于练习快速排序、归并排序、堆排序
"""

import random

class 高级排序练习:
    """高级排序练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_quick_stable(self):
        """练习：快速排序稳定性 ⭐重点"""
        print(f"\n【题目】快速排序是稳定的吗？")
        user_answer = input("你的答案（稳定/不稳定）：")
        correct = '不稳定'
        
        self.total += 1
        if user_answer == correct:
            self.score += 1
            print(f"✅ 正确！快速排序是不稳定的")
        else:
            print(f"❌ 错误！快速排序是不稳定的")
            print(f"   分区过程可能改变相等元素相对位置")
    
    def practice_merge_stable(self):
        """练习：归并排序稳定性 ⭐重点"""
        print(f"\n【题目】归并排序是稳定的吗？")
        user_answer = input("你的答案（稳定/不稳定）：")
        correct = '稳定'
        
        self.total += 1
        if user_answer == correct:
            self.score += 1
            print(f"✅ 正确！归并排序是稳定的")
            print(f"   合并时相等元素不改变顺序")
        else:
            print(f"❌ 错误！归并排序是稳定的")
            print(f"   合并时相等元素优先选择左边的")
    
    def practice_heap_stable(self):
        """练习：堆排序稳定性 ⭐重点"""
        print(f"\n【题目】堆排序是稳定的吗？")
        user_answer = input("你的答案（稳定/不稳定）：")
        correct = '不稳定'
        
        self.total += 1
        if user_answer == correct:
            self.score += 1
            print(f"✅ 正确！堆排序是不稳定的")
            print(f"   堆调整可能改变相等元素相对位置")
        else:
            print(f"❌ 错误！堆排序是不稳定的")
            print(f"   这是考试高频陷阱！")
    
    def practice_quick_time(self):
        """练习：快速排序时间复杂度"""
        questions = [
            ('快速排序平均时间复杂度？', 'O(n log n)'),
            ('快速排序最坏时间复杂度？', 'O(n²)'),
            ('快速排序最坏情况是什么？', '基准选择不当，每次只分出一个元素'),
        ]
        
        question, correct = random.choice(questions)
        
        print(f"\n【题目】{question}")
        user_answer = input("你的答案：").upper()
        
        self.total += 1
        if user_answer.replace(' ', '') == correct.replace(' ', '').upper():
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
    
    def practice_merge_space(self):
        """练习：归并排序空间复杂度 ⭐重点"""
        print(f"\n【题目】归并排序的空间复杂度是？")
        user_answer = input("你的答案：").upper()
        correct = 'O(N)'
        
        self.total += 1
        if user_answer.replace(' ', '') == correct:
            self.score += 1
            print(f"✅ 正确！归并排序需要O(n)额外空间")
        else:
            print(f"❌ 错误！归并排序需要O(n)额外空间")
            print(f"   合并需要临时数组存储结果")
    
    def practice_heap_space(self):
        """练习：堆排序空间复杂度 ⭐重点"""
        print(f"\n【题目】堆排序的空间复杂度是？")
        user_answer = input("你的答案：").upper()
        correct = 'O(1)'
        
        self.total += 1
        if user_answer.replace(' ', '') == correct:
            self.score += 1
            print(f"✅ 正确！堆排序空间复杂度O(1)")
            print(f"   无需额外空间，原地排序")
        else:
            print(f"❌ 错误！堆排序空间复杂度O(1)")
    
    def practice_time_onlogn_stable(self):
        """练习：O(n log n)稳定排序 ⭐重点"""
        print(f"\n【题目】时间复杂度O(n log n)且稳定的排序是？")
        user_answer = input("你的答案：")
        correct = '归并排序'
        
        self.total += 1
        if '归并' in user_answer:
            self.score += 1
            print(f"✅ 正确！归并排序是O(n log n)稳定的")
            print(f"   快排和堆排序不稳定")
        else:
            print(f"❌ 错误！归并排序是O(n log n)稳定的")
    
    def practice_time_onlogn_unstable(self):
        """练习：O(n log n)不稳定排序 ⭐重点"""
        print(f"\n【题目】时间复杂度O(n log n)且不稳定的排序有哪些？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['快速', '堆', '快排', '堆排序']
        
        self.total += 1
        if any(c in user_answer for c in correct):
            self.score += 1
            print(f"✅ 正确！快排和堆排序都是O(n log n)不稳定")
        else:
            print(f"❌ 错误！快排和堆排序都是O(n log n)不稳定")
    
    def practice_space_o1_onlogn(self):
        """练习：O(1)空间O(n log n)时间 ⭐重点"""
        print(f"\n【题目】时间复杂度O(n log n)且空间复杂度O(1)的排序是？")
        user_answer = input("你的答案：")
        correct = '堆排序'
        
        self.total += 1
        if '堆' in user_answer:
            self.score += 1
            print(f"✅ 正确！堆排序是O(n log n)时间O(1)空间")
            print(f"   归并需要O(n)空间，快排需要O(log n)空间")
        else:
            print(f"❌ 错误！堆排序是O(n log n)时间O(1)空间")
    
    def practice_stable_slogan(self):
        """练习：稳定性口诀 ⭐重点"""
        print(f"\n【题目】排序稳定性口诀是什么？")
        user_answer = input("你的答案：")
        correct = '快选堆希不稳定'
        
        self.total += 1
        if '快' in user_answer and '选' in user_answer and '堆' in user_answer:
            self.score += 1
            print(f"✅ 正确！口诀：快选堆希不稳定")
            print(f"   快速、选择、堆、希尔排序不稳定")
            print(f"   其他排序稳定")
        else:
            print(f"❌ 错误！口诀：快选堆希不稳定")
            print(f"   快速、选择、堆、希尔排序不稳定")
    
    def practice_comparison(self):
        """练习：排序对比"""
        questions = [
            ('平均最快的排序是？', '快速排序'),
            ('稳定的O(n log n)排序是？', '归并排序'),
            ('无额外空间的O(n log n)排序是？', '堆排序'),
            ('堆排序稳定吗？', '不稳定'),
            ('归并排序需要额外空间吗？', '需要O(n)'),
            ('快速排序最坏情况？', 'O(n²)'),
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
        print("高级排序算法练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 快速排序稳定性 ⭐重点")
        print("2. 归并排序稳定性 ⭐重点")
        print("3. 堆排序稳定性 ⭐重点")
        print("4. 快速排序时间复杂度")
        print("5. 归并排序空间复杂度 ⭐重点")
        print("6. 堆排序空间复杂度 ⭐重点")
        print("7. O(n log n)稳定排序 ⭐重点")
        print("8. O(n log n)不稳定排序 ⭐重点")
        print("9. O(1)空间O(n log n)时间 ⭐重点")
        print("10. 稳定性口诀 ⭐重点")
        print("11. 排序对比")
        print("12. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_quick_stable()
            elif choice == '2':
                self.practice_merge_stable()
            elif choice == '3':
                self.practice_heap_stable()
            elif choice == '4':
                self.practice_quick_time()
            elif choice == '5':
                self.practice_merge_space()
            elif choice == '6':
                self.practice_heap_space()
            elif choice == '7':
                self.practice_time_onlogn_stable()
            elif choice == '8':
                self.practice_time_onlogn_unstable()
            elif choice == '9':
                self.practice_space_o1_onlogn()
            elif choice == '10':
                self.practice_stable_slogan()
            elif choice == '11':
                self.practice_comparison()
            elif choice == '12':
                types = [
                    self.practice_quick_stable,
                    self.practice_merge_stable,
                    self.practice_heap_stable,
                    self.practice_time_onlogn_stable,
                    self.practice_time_onlogn_unstable,
                    self.practice_space_o1_onlogn,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 高级排序练习()
    practice.run()