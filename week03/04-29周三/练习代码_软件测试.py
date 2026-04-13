#!/usr/bin/env python3
"""
软件测试练习脚本
用于练习白盒测试、黑盒测试方法
"""

import random

class 软件测试练习:
    """软件测试练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_unit_test(self):
        """练习：单元测试"""
        print(f"\n【题目】单元测试用什么测试方法？")
        user_answer = input("你的答案：")
        correct = '白盒测试'
        
        self.total += 1
        if '白盒' in user_answer:
            self.score += 1
            print(f"✅ 正确！单元测试用白盒测试")
            print(f"   测试对象：模块/函数")
        else:
            print(f"❌ 错误！单元测试用白盒测试")
    
    def practice_system_test(self):
        """练习：系统测试 ⭐重点"""
        print(f"\n【题目】系统测试用什么测试方法？")
        user_answer = input("你的答案：")
        correct = '黑盒测试'
        
        self.total += 1
        if '黑盒' in user_answer:
            self.score += 1
            print(f"✅ 正确！系统测试用黑盒测试")
            print(f"   测试对象：整个系统")
        else:
            print(f"❌ 错误！系统测试用黑盒测试")
    
    def practice_acceptance_test(self):
        """练习：验收测试"""
        print(f"\n【题目】验收测试用什么测试方法？")
        user_answer = input("你的答案：")
        correct = '黑盒测试'
        
        self.total += 1
        if '黑盒' in user_answer:
            self.score += 1
            print(f"✅ 正确！验收测试用黑盒测试")
            print(f"   测试对象：用户验收")
        else:
            print(f"❌ 错误！验收测试用黑盒测试")
    
    def practice_whitebox_methods(self):
        """练习：白盒测试方法 ⭐重点"""
        print(f"\n【题目】白盒测试的方法有哪些？")
        user_answer = input("你的答案（说出一种）：")
        correct_methods = ['语句覆盖', '判断覆盖', '条件覆盖', '路径覆盖']
        
        self.total += 1
        if any(method in user_answer for method in correct_methods):
            self.score += 1
            print(f"✅ 正确！白盒测试方法：")
            print(f"   1. 语句覆盖")
            print(f"   2. 判断覆盖")
            print(f"   3. 条件覆盖")
            print(f"   4. 路径覆盖")
        else:
            print(f"❌ 错误！白盒测试方法：")
            print(f"   1. 语句覆盖")
            print(f"   2. 判断覆盖")
            print(f"   3. 条件覆盖")
            print(f"   4. 路径覆盖")
    
    def practice_blackbox_methods(self):
        """练习：黑盒测试方法 ⭐重点"""
        print(f"\n【题目】黑盒测试的方法有哪些？")
        user_answer = input("你的答案（说出一种）：")
        correct_methods = ['等价类划分', '边界值分析', '错误推测法', '因果图法']
        
        self.total += 1
        if any(method in user_answer for method in correct_methods):
            self.score += 1
            print(f"✅ 正确！黑盒测试方法：")
            print(f"   1. 等价类划分")
            print(f"   2. 边界值分析")
            print(f"   3. 错误推测法")
            print(f"   4. 因果图法")
        else:
            print(f"❌ 错误！黑盒测试方法：")
            print(f"   1. 等价类划分")
            print(f"   2. 边界值分析")
            print(f"   3. 错误推测法")
            print(f"   4. 因果图法")
    
    def practice_path_coverage(self):
        """练习：路径覆盖 ⭐重点"""
        print(f"\n【题目】白盒测试中覆盖强度最大的是？")
        user_answer = input("你的答案：")
        correct = '路径覆盖'
        
        self.total += 1
        if '路径' in user_answer:
            self.score += 1
            print(f"✅ 正确！路径覆盖覆盖强度最大")
            print(f"   覆盖所有可能的执行路径")
        else:
            print(f"❌ 错误！路径覆盖覆盖强度最大")
    
    def practice_statement_coverage(self):
        """练习：语句覆盖"""
        print(f"\n【题目】白盒测试中覆盖强度最小的是？")
        user_answer = input("你的答案：")
        correct = '语句覆盖'
        
        self.total += 1
        if '语句' in user_answer:
            self.score += 1
            print(f"✅ 正确！语句覆盖覆盖强度最小")
            print(f"   每条语句至少执行一次")
        else:
            print(f"❌ 错误！语句覆盖覆盖强度最小")
    
    def practice_coverage_order(self):
        """练习：覆盖强度顺序 ⭐重点"""
        print(f"\n【题目】白盒测试覆盖强度从小到大排序？")
        user_answer = input("你的答案：")
        correct = '语句→判断→条件→路径'
        
        self.total += 1
        if '语句' in user_answer and '路径' in user_answer:
            self.score += 1
            print(f"✅ 正确！覆盖强度：语句 < 判断 < 条件 < 路径")
        else:
            print(f"❌ 错误！覆盖强度：语句 < 判断 < 条件 < 路径")
    
    def practice_boundary_value(self):
        """练习：边界值分析"""
        print(f"\n【题目】边界值分析适用于什么场景？")
        user_answer = input("你的答案：")
        correct = '输入有范围边界'
        
        self.total += 1
        if '边界' in user_answer or '范围' in user_answer:
            self.score += 1
            print(f"✅ 正确！边界值分析适用于输入有范围的场景")
        else:
            print(f"❌ 错误！边界值分析适用于输入有范围的场景")
    
    def practice_equivalence_class(self):
        """练习：等价类划分"""
        print(f"\n【题目】等价类划分的原理是什么？")
        user_answer = input("你的答案：")
        correct = '分有效和无效等价类'
        
        self.total += 1
        if '等价' in user_answer or '有效' in user_answer:
            self.score += 1
            print(f"✅ 正确！等价类划分：分有效等价类和无效等价类")
        else:
            print(f"❌ 错误！等价类划分：分有效等价类和无效等价类")
    
    def practice_test_comparison(self):
        """练习：测试对比 ⭐重点"""
        questions = [
            ('单元测试用什么方法？', '白盒测试'),
            ('系统测试用什么方法？', '黑盒测试'),
            ('验收测试用什么方法？', '黑盒测试'),
            ('白盒测试关注什么？', '内部逻辑'),
            ('黑盒测试关注什么？', '功能行为'),
            ('白盒最强覆盖是？', '路径覆盖'),
            ('白盒最弱覆盖是？', '语句覆盖'),
            ('黑盒常用方法是？', '等价类划分、边界值分析'),
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
        print("软件测试练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 单元测试方法")
        print("2. 系统测试方法 ⭐重点")
        print("3. 验收测试方法")
        print("4. 白盒测试方法 ⭐重点")
        print("5. 黑盒测试方法 ⭐重点")
        print("6. 路径覆盖 ⭐重点")
        print("7. 语句覆盖")
        print("8. 覆盖强度顺序 ⭐重点")
        print("9. 边界值分析")
        print("10. 等价类划分")
        print("11. 测试对比 ⭐重点")
        print("12. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_unit_test()
            elif choice == '2':
                self.practice_system_test()
            elif choice == '3':
                self.practice_acceptance_test()
            elif choice == '4':
                self.practice_whitebox_methods()
            elif choice == '5':
                self.practice_blackbox_methods()
            elif choice == '6':
                self.practice_path_coverage()
            elif choice == '7':
                self.practice_statement_coverage()
            elif choice == '8':
                self.practice_coverage_order()
            elif choice == '9':
                self.practice_boundary_value()
            elif choice == '10':
                self.practice_equivalence_class()
            elif choice == '11':
                self.practice_test_comparison()
            elif choice == '12':
                types = [
                    self.practice_system_test,
                    self.practice_whitebox_methods,
                    self.practice_blackbox_methods,
                    self.practice_path_coverage,
                    self.practice_coverage_order,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 软件测试练习()
    practice.run()