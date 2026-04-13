#!/usr/bin/env python3
"""
面向对象练习脚本
用于练习封装、继承、多态、重载、重写
"""

import random

class 面向对象练习:
    """面向对象练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_encapsulation(self):
        """练习：封装"""
        print(f"\n【题目】封装的含义是什么？")
        user_answer = input("你的答案：")
        correct = '数据与操作绑定，信息隐蔽'
        
        self.total += 1
        if '隐蔽' in user_answer or '绑定' in user_answer:
            self.score += 1
            print(f"✅ 正确！封装：数据与操作绑定，信息隐蔽")
        else:
            print(f"❌ 错误！封装：数据与操作绑定，信息隐蔽")
    
    def practice_inheritance(self):
        """练习：继承"""
        print(f"\n【题目】继承的含义是什么？")
        user_answer = input("你的答案：")
        correct = '子类继承父类属性和方法'
        
        self.total += 1
        if '继承' in user_answer or '父类' in user_answer:
            self.score += 1
            print(f"✅ 正确！继承：子类继承父类属性和方法")
            print(f"   实现代码复用")
        else:
            print(f"❌ 错误！继承：子类继承父类属性和方法")
    
    def practice_polymorphism(self):
        """练习：多态 ⭐重点"""
        print(f"\n【题目】多态的含义是什么？")
        user_answer = input("你的答案：")
        correct = '同一接口不同实现'
        
        self.total += 1
        if '接口' in user_answer or '不同实现' in user_answer:
            self.score += 1
            print(f"✅ 正确！多态：同一接口不同实现")
            print(f"   重载：编译时确定")
            print(f"   重写：运行时确定")
        else:
            print(f"❌ 错误！多态：同一接口不同实现")
    
    def practice_overload_definition(self):
        """练习：重载定义 ⭐重点"""
        print(f"\n【题目】重载是什么？")
        user_answer = input("你的答案：")
        correct = '同类中同名方法不同参数'
        
        self.total += 1
        if '同名' in user_answer and '参数' in user_answer:
            self.score += 1
            print(f"✅ 正确！重载：同类中同名方法不同参数")
            print(f"   编译时确定")
        else:
            print(f"❌ 错误！重载：同类中同名方法不同参数")
    
    def practice_override_definition(self):
        """练习：重写定义 ⭐重点"""
        print(f"\n【题目】重写是什么？")
        user_answer = input("你的答案：")
        correct = '子类重新定义父类方法'
        
        self.total += 1
        if '子类' in user_answer and '父类' in user_answer:
            self.score += 1
            print(f"✅ 正确！重写：子类重新定义父类方法")
            print(f"   运行时确定")
        else:
            print(f"❌ 错误！重写：子类重新定义父类方法")
    
    def practice_overload_vs_override(self):
        """练习：重载vs重写 ⭐重点必考"""
        print(f"\n【题目】重载和重写的区别？")
        print("请选择正确的描述：")
        print("A. 重载是同类同名不同参数，重写是子类重定义父类方法")
        print("B. 重载是子类重定义父类方法，重写是同类同名不同参数")
        user_answer = input("你的答案（A或B）：")
        correct = 'A'
        
        self.total += 1
        if user_answer.upper() == correct:
            self.score += 1
            print(f"✅ 正确！重载是同类同名不同参数，重写是子类重定义父类方法")
        else:
            print(f"❌ 错误！正确答案是A")
            print(f"   重载：同类同名不同参数")
            print(f"   重写：子类重定义父类方法")
    
    def practice_overload_timing(self):
        """练习：重载确定时机"""
        print(f"\n【题目】重载何时确定？")
        user_answer = input("你的答案：")
        correct = '编译时'
        
        self.total += 1
        if '编译' in user_answer:
            self.score += 1
            print(f"✅ 正确！重载在编译时确定")
        else:
            print(f"❌ 错误！重载在编译时确定")
    
    def practice_override_timing(self):
        """练习：重写确定时机 ⭐重点"""
        print(f"\n【题目】重写何时确定？")
        user_answer = input("你的答案：")
        correct = '运行时'
        
        self.total += 1
        if '运行' in user_answer:
            self.score += 1
            print(f"✅ 正确！重写在运行时确定（动态绑定）")
        else:
            print(f"❌ 错误！重写在运行时确定（动态绑定）")
    
    def practice_abstract_vs_interface(self):
        """练习：抽象类vs接口 ⭐重点"""
        print(f"\n【题目】抽象类和接口的区别？")
        print("请选择：")
        print("A. 抽象类可有具体方法，单继承；接口全抽象方法，多实现")
        print("B. 抽象类全抽象方法，多继承；接口可有具体方法，单实现")
        user_answer = input("你的答案（A或B）：")
        correct = 'A'
        
        self.total += 1
        if user_answer.upper() == correct:
            self.score += 1
            print(f"✅ 正确！")
            print(f"   抽象类：可有具体方法，单继承")
            print(f"   接口：全抽象方法（Java8前），多实现")
        else:
            print(f"❌ 错误！正确答案是A")
            print(f"   抽象类：可有具体方法，单继承")
            print(f"   接口：全抽象方法（Java8前），多实现")
    
    def practice_class_vs_object(self):
        """练习：类vs对象"""
        print(f"\n【题目】类和对象的区别？")
        user_answer = input("你的答案：")
        correct = '类是模板抽象，对象是实例具体'
        
        self.total += 1
        if '模板' in user_answer or '实例' in user_answer:
            self.score += 1
            print(f"✅ 正确！类是模板抽象，对象是实例具体")
        else:
            print(f"❌ 错误！类是模板抽象，对象是实例具体")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("面向对象练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 封装")
        print("2. 继承")
        print("3. 多态 ⭐重点")
        print("4. 重载定义 ⭐重点")
        print("5. 重写定义 ⭐重点")
        print("6. 重载vs重写 ⭐重点必考")
        print("7. 重载确定时机")
        print("8. 重写确定时机 ⭐重点")
        print("9. 抽象类vs接口 ⭐重点")
        print("10. 类vs对象")
        print("11. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_encapsulation()
            elif choice == '2':
                self.practice_inheritance()
            elif choice == '3':
                self.practice_polymorphism()
            elif choice == '4':
                self.practice_overload_definition()
            elif choice == '5':
                self.practice_override_definition()
            elif choice == '6':
                self.practice_overload_vs_override()
            elif choice == '7':
                self.practice_overload_timing()
            elif choice == '8':
                self.practice_override_timing()
            elif choice == '9':
                self.practice_abstract_vs_interface()
            elif choice == '10':
                self.practice_class_vs_object()
            elif choice == '11':
                types = [
                    self.practice_overload_vs_override,
                    self.practice_override_timing,
                    self.practice_abstract_vs_interface,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 面向对象练习()
    practice.run()