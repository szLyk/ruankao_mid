#!/usr/bin/env python3
"""
UML图下午题练习脚本
用于练习UML类图和用例图补全（下午题3）⭐重点必考
"""

import random

class UML练习:
    """UML图练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_aggregation(self):
        """练习：聚合关系 ⭐重点"""
        print(f"\n【题目】聚合关系用什么符号？")
        user_answer = input("你的答案：")
        correct = '空心菱形'
        
        self.total += 1
        if '空心' in user_answer or '菱形' in user_answer:
            self.score += 1
            print(f"✅ 正确！聚合关系用空心菱形表示")
        else:
            print(f"❌ 错误！聚合关系用空心菱形表示")
        print("💡 记忆技巧：空心=可独立存在")
    
    def practice_composition(self):
        """练习：组合关系 ⭐重点"""
        print(f"\n【题目】组合关系用什么符号？")
        user_answer = input("你的答案：")
        correct = '实心菱形'
        
        self.total += 1
        if '实心' in user_answer or '菱形' in user_answer:
            self.score += 1
            print(f"✅ 正确！组合关系用实心菱形表示")
        else:
            print(f"❌ 错误！组合关系用实心菱形表示")
        print("💡 记忆技巧：实心=不可独立存在")
    
    def practice_aggregation_meaning(self):
        """练习：聚合含义 ⭐重点"""
        print(f"\n【题目】聚合关系的含义？")
        user_answer = input("你的答案：")
        correct = '整体-部分，可独立存在'
        
        self.total += 1
        if '独立' in user_answer or '整体' in user_answer or '部分' in user_answer:
            self.score += 1
            print(f"✅ 正确！聚合：整体-部分，部分可独立存在")
        else:
            print(f"❌ 错误！聚合：整体-部分，部分可独立存在")
    
    def practice_composition_meaning(self):
        """练习：组合含义 ⭐重点"""
        print(f"\n【题目】组合关系的含义？")
        user_answer = input("你的答案：")
        correct = '整体-部分，不可独立存在'
        
        self.total += 1
        if '不可' in user_answer or '不能' in user_answer:
            self.score += 1
            print(f"✅ 正确！组合：整体-部分，部分不可独立存在")
        else:
            print(f"❌ 错误！组合：整体-部分，部分不可独立存在")
    
    def practice_company_employee(self):
        """练习：公司-员工 ⭐重点"""
        print(f"\n【题目】公司和员工是什么关系？")
        user_answer = input("你的答案（聚合/组合）：")
        correct = '聚合'
        
        self.total += 1
        if '聚合' in user_answer:
            self.score += 1
            print(f"✅ 正确！公司-员工是聚合关系")
            print("💡 解析：员工离开公司还能独立存在")
        else:
            print(f"❌ 错误！公司-员工是聚合关系")
            print("💡 解析：员工离开公司还能独立存在")
    
    def practice_person_heart(self):
        """练习：人-心脏 ⭐重点"""
        print(f"\n【题目】人和心脏是什么关系？")
        user_answer = input("你的答案（聚合/组合）：")
        correct = '组合'
        
        self.total += 1
        if '组合' in user_answer:
            self.score += 1
            print(f"✅ 正确！人-心脏是组合关系")
            print("💡 解析：心脏离开人无法独立存在")
        else:
            print(f"❌ 错误！人-心脏是组合关系")
            print("💡 解析：心脏离开人无法独立存在")
    
    def practice_generalization(self):
        """练习：泛化关系"""
        print(f"\n【题目】泛化（继承）关系用什么符号？")
        user_answer = input("你的答案：")
        correct = '实线空心箭头'
        
        self.total += 1
        if '实线' in user_answer or '继承' in user_answer:
            self.score += 1
            print(f"✅ 正确！泛化用实线空心箭头表示")
        else:
            print(f"❌ 错误！泛化用实线空心箭头表示")
    
    def practice_realization(self):
        """练习：实现关系"""
        print(f"\n【题目】实现（接口实现）关系用什么符号？")
        user_answer = input("你的答案：")
        correct = '虚线空心箭头'
        
        self.total += 1
        if '虚线' in user_answer or '接口' in user_answer:
            self.score += 1
            print(f"✅ 正确！实现用虚线空心箭头表示")
        else:
            print(f"❌ 错误！实现用虚线空心箭头表示")
    
    def practice_association(self):
        """练习：关联关系"""
        print(f"\n【题目】关联关系用什么符号？")
        user_answer = input("你的答案：")
        correct = '实线'
        
        self.total += 1
        if '实线' in user_answer:
            self.score += 1
            print(f"✅ 正确！关联用实线表示")
        else:
            print(f"❌ 错误！关联用实线表示")
    
    def practice_dependency(self):
        """练习：依赖关系"""
        print(f"\n【题目】依赖关系用什么符号？")
        user_answer = input("你的答案：")
        correct = '虚线箭头'
        
        self.total += 1
        if '虚线' in user_answer:
            self.score += 1
            print(f"✅ 正确！依赖用虚线箭头表示")
        else:
            print(f"❌ 错误！依赖用虚线箭头表示")
    
    def practice_usecase_diagram(self):
        """练习：用例图组成 ⭐重点"""
        print(f"\n【题目】用例图由什么组成？")
        user_answer = input("你的答案：")
        correct = '用例、参与者、关系'
        
        self.total += 1
        if '用例' in user_answer or '参与者' in user_answer:
            self.score += 1
            print(f"✅ 正确！用例图：用例、参与者、关系")
        else:
            print(f"❌ 错误！用例图：用例、参与者、关系")
    
    def practice_include(self):
        """练习：include关系 ⭐重点"""
        print(f"\n【题目】include关系含义？")
        user_answer = input("你的答案：")
        correct = '必须包含的用例'
        
        self.total += 1
        if '必须' in user_answer or '包含' in user_answer:
            self.score += 1
            print(f"✅ 正确！include：必须包含的用例")
        else:
            print(f"❌ 错误！include：必须包含的用例")
    
    def practice_extend(self):
        """练习：extend关系"""
        print(f"\n【题目】extend关系含义？")
        user_answer = input("你的答案：")
        correct = '可选扩展的用例'
        
        self.total += 1
        if '可选' in user_answer or '扩展' in user_answer:
            self.score += 1
            print(f"✅ 正确！extend：可选扩展的用例")
        else:
            print(f"❌ 错误！extend：可选扩展的用例")
    
    def practice_find_attribute(self):
        """练习：找属性 ⭐重点"""
        print(f"\n【题目】类图中属性从哪里找？")
        user_answer = input("你的答案：")
        correct = '题目描述找名词'
        
        self.total += 1
        if '名词' in user_answer or '描述' in user_answer:
            self.score += 1
            print(f"✅ 正确！属性从题目描述找名词")
        else:
            print(f"❌ 错误！属性从题目描述找名词")
    
    def practice_find_method(self):
        """练习：找方法 ⭐重点"""
        print(f"\n【题目】类图中方法从哪里找？")
        user_answer = input("你的答案：")
        correct = '题目描述找动词'
        
        self.total += 1
        if '动词' in user_answer or '描述' in user_answer:
            self.score += 1
            print(f"✅ 正确！方法从题目描述找动词")
        else:
            print(f"❌ 错误！方法从题目描述找动词")
    
    def practice_judge_relation(self):
        """练习：判断关系 ⭐重点"""
        print(f"\n【题目】判断聚合还是组合的关键？")
        user_answer = input("你的答案：")
        correct = '看部分能否独立存在'
        
        self.total += 1
        if '独立' in user_answer:
            self.score += 1
            print(f"✅ 正确！判断关键：看部分能否独立存在")
        else:
            print(f"❌ 错误！判断关键：看部分能否独立存在")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
        if self.score == self.total:
            print("🎉 全对！UML图掌握得很好！")
        elif self.score >= self.total * 0.8:
            print("👍 不错！继续巩固！")
        else:
            print("💪 还需努力！重点记住聚合vs组合")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("UML图下午题练习（下午题3）⭐重点必考")
        print("="*40)
        print("\n练习内容：")
        print("1. 聚合关系符号 ⭐重点")
        print("2. 组合关系符号 ⭐重点")
        print("3. 聚合含义 ⭐重点")
        print("4. 组合含义 ⭐重点")
        print("5. 公司-员工判断 ⭐重点")
        print("6. 人-心脏判断 ⭐重点")
        print("7. 泛化关系")
        print("8. 实现关系")
        print("9. 关联关系")
        print("10. 依赖关系")
        print("11. 用例图组成 ⭐重点")
        print("12. include关系 ⭐重点")
        print("13. extend关系")
        print("14. 找属性技巧 ⭐重点")
        print("15. 找方法技巧 ⭐重点")
        print("16. 判断关系技巧 ⭐重点")
        print("17. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_aggregation()
            elif choice == '2':
                self.practice_composition()
            elif choice == '3':
                self.practice_aggregation_meaning()
            elif choice == '4':
                self.practice_composition_meaning()
            elif choice == '5':
                self.practice_company_employee()
            elif choice == '6':
                self.practice_person_heart()
            elif choice == '7':
                self.practice_generalization()
            elif choice == '8':
                self.practice_realization()
            elif choice == '9':
                self.practice_association()
            elif choice == '10':
                self.practice_dependency()
            elif choice == '11':
                self.practice_usecase_diagram()
            elif choice == '12':
                self.practice_include()
            elif choice == '13':
                self.practice_extend()
            elif choice == '14':
                self.practice_find_attribute()
            elif choice == '15':
                self.practice_find_method()
            elif choice == '16':
                self.practice_judge_relation()
            elif choice == '17':
                types = [
                    self.practice_aggregation,
                    self.practice_composition,
                    self.practice_company_employee,
                    self.practice_person_heart,
                    self.practice_judge_relation,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = UML练习()
    practice.run()