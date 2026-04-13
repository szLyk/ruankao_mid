#!/usr/bin/env python3
"""
线性结构练习脚本
用于练习栈、队列、数组、链表相关概念
"""

import random

class 线性结构练习:
    """线性结构练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_stack_sequence(self):
        """练习：栈的合法出栈序列判断"""
        sequences = [
            ('1,2,3,4,5', '5,4,3,2,1', True),   # 全部进栈再出栈
            ('1,2,3,4,5', '4,5,3,2,1', True),   # 合法
            ('1,2,3,4,5', '4,3,5,1,2', False),  # 不合法：5必须在1,2之前
            ('1,2,3,4,5', '3,4,5,2,1', True),   # 合法
            ('1,2,3,4,5', '1,2,3,4,5', True),   # 边进边出
            ('1,2,3,4,5', '2,1,3,4,5', True),   # 合法
        ]
        
        in_seq, out_seq, correct = random.choice(sequences)
        
        print(f"\n【题目】入栈顺序：{in_seq}")
        print(f"判断出栈序列：{out_seq} 是否合法？")
        user_answer = input("你的答案（合法/不合法）：")
        
        self.total += 1
        expected = "合法" if correct else "不合法"
        
        if user_answer == expected:
            self.score += 1
            print(f"✅ 正确！答案确实是 {expected}")
        else:
            print(f"❌ 错误！正确答案是 {expected}")
            print(f"   栈的特性：LIFO（后进先出）")
            print(f"   判断规则：不能'先出后进'")
    
    def practice_stack_application(self):
        """练习：栈的应用场景"""
        scenarios = [
            ('函数调用返回地址保存', True),
            ('表达式求值（后缀表达式）', True),
            ('括号匹配检查', True),
            ('页面浏览历史（后退）', True),
            ('CPU任务调度', False),  # 用队列
            ('打印队列', False),     # 用队列
        ]
        
        scenario, correct = random.choice(scenarios)
        
        print(f"\n【题目】以下场景是否适合使用栈？")
        print(f"场景：{scenario}")
        user_answer = input("你的答案（适合/不适合）：")
        
        self.total += 1
        expected = "适合" if correct else "不适合"
        
        if user_answer == expected:
            self.score += 1
            print(f"✅ 正确！答案确实是 {expected}")
        else:
            print(f"❌ 错误！正确答案是 {expected}")
            if correct:
                print(f"   栈的应用：函数调用、递归、括号匹配、表达式求值")
            else:
                print(f"   该场景应该用队列（FIFO）")
    
    def practice_queue_application(self):
        """练习：队列的应用场景"""
        scenarios = [
            ('CPU任务调度', True),
            ('打印任务队列', True),
            ('消息队列', True),
            ('图的BFS遍历', True),
            ('函数调用栈', False),  # 用栈
            ('表达式求值', False),  # 用栈
        ]
        
        scenario, correct = random.choice(scenarios)
        
        print(f"\n【题目】以下场景是否适合使用队列？")
        print(f"场景：{scenario}")
        user_answer = input("你的答案（适合/不适合）：")
        
        self.total += 1
        expected = "适合" if correct else "不适合"
        
        if user_answer == expected:
            self.score += 1
            print(f"✅ 正确！答案确实是 {expected}")
        else:
            print(f"❌ 错误！正确答案是 {expected}")
            if correct:
                print(f"   队列的应用：任务调度、消息队列、BFS遍历")
            else:
                print(f"   该场景应该用栈（LIFO）")
    
    def practice_array_vs_linkedlist(self):
        """练习：数组与链表对比"""
        questions = [
            ('频繁访问元素，用什么结构更合适？', '数组'),
            ('频繁插入删除元素，用什么结构更合适？', '链表'),
            ('数组访问元素的时间复杂度是？', 'O(1)'),
            ('链表访问元素的时间复杂度是？', 'O(n)'),
            ('数组插入元素的时间复杂度是？', 'O(n)'),
            ('链表插入元素的时间复杂度是？', 'O(1)'),
        ]
        
        question, correct = random.choice(questions)
        
        print(f"\n【题目】{question}")
        user_answer = input("你的答案：")
        
        self.total += 1
        if user_answer.lower() == correct.lower():
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
            print(f"   数组：顺序存储，访问O(1)，插入删除O(n)")
            print(f"   链表：链式存储，访问O(n)，插入删除O(1)")
    
    def practice_circular_queue(self):
        """练习：循环队列"""
        questions = [
            ('循环队列队满条件是？', '(rear+1)%n==front'),
            ('循环队列队空条件是？', 'rear==front'),
            ('循环队列牺牲几个单元判断队满？', '1个'),
            ('循环队列解决什么问题？', '假溢出'),
        ]
        
        question, correct = random.choice(questions)
        
        print(f"\n【题目】{question}")
        user_answer = input("你的答案：")
        
        self.total += 1
        # 答案可能有多种写法
        correct_answers = [correct, correct.replace('==', '='), '1']
        if user_answer.replace(' ', '') in [a.replace(' ', '') for a in correct_answers]:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
            print(f"   循环队列：解决假溢出问题")
            print(f"   队满：(rear+1)%n == front")
            print(f"   队空：rear == front")
    
    def practice_complexity(self):
        """练习：时间复杂度"""
        questions = [
            ('数组随机访问的时间复杂度？', 'O(1)'),
            ('链表查找元素的时间复杂度？', 'O(n)'),
            ('栈入栈操作的时间复杂度？', 'O(1)'),
            ('队列入队操作的时间复杂度？', 'O(1)'),
        ]
        
        question, correct = random.choice(questions)
        
        print(f"\n【题目】{question}")
        user_answer = input("你的答案：")
        
        self.total += 1
        if user_answer.upper() == correct.upper():
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
        print("线性结构练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 栈的出栈序列判断")
        print("2. 栈的应用场景")
        print("3. 队列的应用场景")
        print("4. 数组vs链表对比")
        print("5. 循环队列")
        print("6. 时间复杂度")
        print("7. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_stack_sequence()
            elif choice == '2':
                self.practice_stack_application()
            elif choice == '3':
                self.practice_queue_application()
            elif choice == '4':
                self.practice_array_vs_linkedlist()
            elif choice == '5':
                self.practice_circular_queue()
            elif choice == '6':
                self.practice_complexity()
            elif choice == '7':
                types = [
                    self.practice_stack_sequence,
                    self.practice_stack_application,
                    self.practice_queue_application,
                    self.practice_array_vs_linkedlist,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 线性结构练习()
    practice.run()