#!/usr/bin/env python3
"""
Java程序设计练习脚本
用于练习Java核心概念（下午题5）
"""

import random

class Java练习:
    """Java程序设计练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_class_definition(self):
        """练习：类定义 ⭐重点"""
        print(f"\n【题目】Java类定义用什么关键字？")
        user_answer = input("你的答案：")
        correct = 'class'
        
        self.total += 1
        if 'class' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！类定义用 class 关键字")
        else:
            print(f"❌ 错误！类定义用 class 关键字")
    
    def practice_inheritance(self):
        """练习：继承 ⭐重点"""
        print(f"\n【题目】Java继承用什么关键字？")
        user_answer = input("你的答案：")
        correct = 'extends'
        
        self.total += 1
        if 'extends' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！继承用 extends 关键字")
        else:
            print(f"❌ 错误！继承用 extends 关键字")
    
    def practice_interface(self):
        """练习：接口实现 ⭐重点"""
        print(f"\n【题目】Java实现接口用什么关键字？")
        user_answer = input("你的答案：")
        correct = 'implements'
        
        self.total += 1
        if 'implements' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！实现接口用 implements 关键字")
        else:
            print(f"❌ 错误！实现接口用 implements 关键字")
    
    def practice_override(self):
        """练习：重写注解 ⭐重点"""
        print(f"\n【题目】方法重写用什么注解？")
        user_answer = input("你的答案：")
        correct = '@Override'
        
        self.total += 1
        if 'override' in user_answer.lower() or '@' in user_answer:
            self.score += 1
            print(f"✅ 正确！方法重写用 @Override 注解")
        else:
            print(f"❌ 错误！方法重写用 @Override 注解")
    
    def practice_constructor(self):
        """练习：构造方法 ⭐重点"""
        print(f"\n【题目】构造方法特点？")
        user_answer = input("你的答案：")
        correct = '与类同名，无返回类型'
        
        self.total += 1
        if '同名' in user_answer:
            self.score += 1
            print(f"✅ 正确！构造方法：与类同名，无返回类型")
        else:
            print(f"❌ 错误！构造方法：与类同名，无返回类型")
    
    def practice_list(self):
        """练习：List集合 ⭐重点"""
        print(f"\n【题目】List接口常用实现类？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['ArrayList', 'LinkedList']
        
        self.total += 1
        if 'ArrayList' in user_answer or 'LinkedList' in user_answer:
            self.score += 1
            print(f"✅ 正确！List实现类：ArrayList、LinkedList")
        else:
            print(f"❌ 错误！List实现类：ArrayList、LinkedList")
    
    def practice_map(self):
        """练习：Map集合 ⭐重点"""
        print(f"\n【题目】Map接口常用实现类？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['HashMap', ' TreeMap']
        
        self.total += 1
        if 'HashMap' in user_answer or 'TreeMap' in user_answer:
            self.score += 1
            print(f"✅ 正确！Map实现类：HashMap、TreeMap")
        else:
            print(f"❌ 错误！Map实现类：HashMap、TreeMap")
    
    def practice_abstract_class(self):
        """练习：抽象类 ⭐重点"""
        print(f"\n【题目】抽象类用什么关键字？")
        user_answer = input("你的答案：")
        correct = 'abstract'
        
        self.total += 1
        if 'abstract' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！抽象类用 abstract 关键字")
        else:
            print(f"❌ 错误！抽象类用 abstract 关键字")
    
    def practice_interface_keyword(self):
        """练习：接口定义 ⭐重点"""
        print(f"\n【题目】接口用什么关键字定义？")
        user_answer = input("你的答案：")
        correct = 'interface'
        
        self.total += 1
        if 'interface' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！接口用 interface 关键字定义")
        else:
            print(f"❌ 错误！接口用 interface 关键字定义")
    
    def practice_new_object(self):
        """练习：创建对象 ⭐重点"""
        print(f"\n【题目】创建对象用什么关键字？")
        user_answer = input("你的答案：")
        correct = 'new'
        
        self.total += 1
        if 'new' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！创建对象用 new 关键字")
        else:
            print(f"❌ 错误！创建对象用 new 关键字")
    
    def practice_exception(self):
        """练习：异常处理 ⭐重点"""
        print(f"\n【题目】Java异常处理关键字？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['try', 'catch', 'finally', 'throw', 'throws']
        
        self.total += 1
        if any(c in user_answer.lower() for c in correct):
            self.score += 1
            print(f"✅ 正确！异常处理：try-catch-finally-throw-throws")
        else:
            print(f"❌ 错误！异常处理：try-catch-finally-throw-throws")
    
    def practice_try_catch(self):
        """练习：try-catch ⭐重点"""
        print(f"\n【题目】异常捕获用什么？")
        user_answer = input("你的答案：")
        correct = 'try-catch'
        
        self.total += 1
        if 'try' in user_answer.lower() and 'catch' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！异常捕获用 try-catch")
        else:
            print(f"❌ 错误！异常捕获用 try-catch")
    
    def practice_public_private(self):
        """练习：访问控制 ⭐重点"""
        print(f"\n【题目】Java访问控制修饰符有哪些？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['public', 'private', 'protected']
        
        self.total += 1
        if any(c in user_answer.lower() for c in correct):
            self.score += 1
            print(f"✅ 正确！访问修饰符：public、private、protected")
        else:
            print(f"❌ 错误！访问修饰符：public、private、protected")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("Java程序设计练习（下午题5）")
        print("="*40)
        print("\n练习内容：")
        print("1. 类定义 class ⭐重点")
        print("2. 继承 extends ⭐重点")
        print("3. 接口实现 implements ⭐重点")
        print("4. 重写注解 @Override ⭐重点")
        print("5. 构造方法 ⭐重点")
        print("6. List集合 ⭐重点")
        print("7. Map集合 ⭐重点")
        print("8. 抽象类 abstract ⭐重点")
        print("9. 接口定义 interface ⭐重点")
        print("10. 创建对象 new ⭐重点")
        print("11. 异常处理 ⭐重点")
        print("12. try-catch ⭐重点")
        print("13. 访问修饰符 ⭐重点")
        print("14. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_class_definition()
            elif choice == '2':
                self.practice_inheritance()
            elif choice == '3':
                self.practice_interface()
            elif choice == '4':
                self.practice_override()
            elif choice == '5':
                self.practice_constructor()
            elif choice == '6':
                self.practice_list()
            elif choice == '7':
                self.practice_map()
            elif choice == '8':
                self.practice_abstract_class()
            elif choice == '9':
                self.practice_interface_keyword()
            elif choice == '10':
                self.practice_new_object()
            elif choice == '11':
                self.practice_exception()
            elif choice == '12':
                self.practice_try_catch()
            elif choice == '13':
                self.practice_public_private()
            elif choice == '14':
                types = [
                    self.practice_inheritance,
                    self.practice_interface,
                    self.practice_override,
                    self.practice_list,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = Java练习()
    practice.run()