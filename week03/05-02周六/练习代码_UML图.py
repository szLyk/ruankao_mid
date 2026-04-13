#!/usr/bin/env python3
"""
UML图练习脚本
用于练习类图关系、用例图
"""

import random

class UML练习:
    """UML图练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_class_diagram(self):
        """练习：类图用途 ⭐重点"""
        print(f"\n【题目】类图的用途是什么？")
        user_answer = input("你的答案：")
        correct = '展示类结构和关系'
        
        self.total += 1
        if '类' in user_answer and '结构' in user_answer or '关系' in user_answer:
            self.score += 1
            print(f"✅ 正确！类图：展示类结构和关系")
        else:
            print(f"❌ 错误！类图：展示类结构和关系")
    
    def practice_usecase_diagram(self):
        """练习：用例图用途 ⭐重点"""
        print(f"\n【题目】用例图的用途是什么？")
        user_answer = input("你的答案：")
        correct = '展示用户功能视图'
        
        self.total += 1
        if '用例' in user_answer or '功能' in user_answer:
            self.score += 1
            print(f"✅ 正确！用例图：展示用户功能视图")
        else:
            print(f"❌ 错误！用例图：展示用户功能视图")
    
    def practice_association(self):
        """练习：关联关系"""
        print(f"\n【题目】关联关系的含义？")
        user_answer = input("你的答案：")
        correct = '一般关系，双方独立'
        
        self.total += 1
        if '关联' in user_answer or '独立' in user_answer:
            self.score += 1
            print(f"✅ 正确！关联：一般关系，双方独立")
            print(f"   符号：实线")
        else:
            print(f"❌ 错误！关联：一般关系，双方独立")
            print(f"   符号：实线")
    
    def practice_dependency(self):
        """练习：依赖关系"""
        print(f"\n【题目】依赖关系的含义？")
        user_answer = input("你的答案：")
        correct = '使用关系，临时使用'
        
        self.total += 1
        if '依赖' in user_answer or '使用' in user_answer:
            self.score += 1
            print(f"✅ 正确！依赖：使用关系，临时使用")
            print(f"   符号：虚线箭头")
        else:
            print(f"❌ 错误！依赖：使用关系，临时使用")
            print(f"   符号：虚线箭头")
    
    def practice_aggregation(self):
        """练习：聚合关系 ⭐重点"""
        print(f"\n【题目】聚合关系的含义？")
        user_answer = input("你的答案：")
        correct = '整体-部分，可独立存在'
        
        self.total += 1
        if '聚合' in user_answer or '独立' in user_answer:
            self.score += 1
            print(f"✅ 正确！聚合：整体-部分，可独立存在")
            print(f"   符号：空心菱形")
            print(f"   例：公司和员工（员工可独立）")
        else:
            print(f"❌ 错误！聚合：整体-部分，可独立存在")
            print(f"   符号：空心菱形")
    
    def practice_composition(self):
        """练习：组合关系 ⭐重点"""
        print(f"\n【题目】组合关系的含义？")
        user_answer = input("你的答案：")
        correct = '整体-部分，不可独立存在'
        
        self.total += 1
        if '组合' in user_answer or '不可独立' in user_answer:
            self.score += 1
            print(f"✅ 正确！组合：整体-部分，不可独立存在")
            print(f"   符号：实心菱形")
            print(f"   例：人和心脏（心脏不可独立）")
        else:
            print(f"❌ 错误！组合：整体-部分，不可独立存在")
            print(f"   符号：实心菱形")
    
    def practice_aggregation_vs_composition(self):
        """练习：聚合vs组合 ⭐重点必考"""
        print(f"\n【题目】聚合和组合的区别？")
        print("请选择：")
        print("A. 聚合可独立存在（空心菱形），组合不可独立（实心菱形）")
        print("B. 聚合不可独立（实心菱形），组合可独立（空心菱形）")
        user_answer = input("你的答案（A或B）：")
        correct = 'A'
        
        self.total += 1
        if user_answer.upper() == correct:
            self.score += 1
            print(f"✅ 正确！")
            print(f"   聚合：可独立存在，空心菱形")
            print(f"   组合：不可独立存在，实心菱形")
        else:
            print(f"❌ 错误！正确答案是A")
            print(f"   聚合：可独立存在，空心菱形")
            print(f"   组合：不可独立存在，实心菱形")
    
    def practice_generalization(self):
        """练习：泛化关系"""
        print(f"\n【题目】泛化关系的含义？")
        user_answer = input("你的答案：")
        correct = '继承关系'
        
        self.total += 1
        if '继承' in user_answer or '泛化' in user_answer:
            self.score += 1
            print(f"✅ 正确！泛化：继承关系")
            print(f"   符号：实线空心箭头")
        else:
            print(f"❌ 错误！泛化：继承关系")
            print(f"   符号：实线空心箭头")
    
    def practice_realization(self):
        """练习：实现关系"""
        print(f"\n【题目】实现关系的含义？")
        user_answer = input("你的答案：")
        correct = '接口实现'
        
        self.total += 1
        if '接口' in user_answer or '实现' in user_answer:
            self.score += 1
            print(f"✅ 正确！实现：接口实现")
            print(f"   符号：虚线空心箭头")
        else:
            print(f"❌ 错误！实现：接口实现")
            print(f"   符号：虚线空心箭头")
    
    def practice_relation_symbol(self):
        """练习：关系符号 ⭐重点"""
        relations = [
            ('聚合关系的符号是？', '空心菱形'),
            ('组合关系的符号是？', '实心菱形'),
            ('泛化关系的符号是？', '实线空心箭头'),
            ('实现关系的符号是？', '虚线空心箭头'),
            ('依赖关系的符号是？', '虚线箭头'),
        ]
        
        question, correct = random.choice(relations)
        
        print(f"\n【题目】{question}")
        user_answer = input("你的答案：")
        
        self.total += 1
        if user_answer.strip() in correct:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
    
    def practice_example(self):
        """练习：关系示例"""
        examples = [
            ('公司和员工是什么关系？', '聚合'),
            ('人和心脏是什么关系？', '组合'),
            ('学生继承Person是什么关系？', '泛化'),
            ('类实现Runnable是什么关系？', '实现'),
        ]
        
        question, correct = random.choice(examples)
        
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
        print("UML图练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 类图用途 ⭐重点")
        print("2. 用例图用途 ⭐重点")
        print("3. 关联关系")
        print("4. 依赖关系")
        print("5. 聚合关系 ⭐重点")
        print("6. 组合关系 ⭐重点")
        print("7. 聚合vs组合 ⭐重点必考")
        print("8. 泛化关系")
        print("9. 实现关系")
        print("10. 关系符号 ⭐重点")
        print("11. 关系示例")
        print("12. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_class_diagram()
            elif choice == '2':
                self.practice_usecase_diagram()
            elif choice == '3':
                self.practice_association()
            elif choice == '4':
                self.practice_dependency()
            elif choice == '5':
                self.practice_aggregation()
            elif choice == '6':
                self.practice_composition()
            elif choice == '7':
                self.practice_aggregation_vs_composition()
            elif choice == '8':
                self.practice_generalization()
            elif choice == '9':
                self.practice_realization()
            elif choice == '10':
                self.practice_relation_symbol()
            elif choice == '11':
                self.practice_example()
            elif choice == '12':
                types = [
                    self.practice_aggregation_vs_composition,
                    self.practice_relation_symbol,
                    self.practice_example,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = UML练习()
    practice.run()