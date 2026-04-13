#!/usr/bin/env python3
"""
下午题综合训练练习脚本
涵盖DFD、ER、UML、Java四种题型 ⭐模拟考试
"""

import random

class 下午题综合训练:
    """下午题综合练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    # ========== DFD图练习（第1题）==========
    
    def practice_dfd_external_entity(self):
        """练习：DFD外部实体 ⭐重点"""
        print(f"\n【DFD题】外部实体用什么图形？")
        user_answer = input("你的答案：")
        correct = '方框'
        
        self.total += 1
        if '方框' in user_answer or '矩形' in user_answer:
            self.score += 1
            print(f"✅ 正确！外部实体用方框表示")
            print("💡 技巧：找题目中的'人/系统/部门'")
        else:
            print(f"❌ 错误！外部实体用方框表示")
    
    def practice_dfd_process(self):
        """练习：DFD加工 ⭐重点"""
        print(f"\n【DFD题】加工/处理用什么图形？")
        user_answer = input("你的答案：")
        correct = '圆圈'
        
        self.total += 1
        if '圆' in user_answer or '圆圈' in user_answer:
            self.score += 1
            print(f"✅ 正确！加工用圆圈表示")
            print("💡 技巧：找题目中的动词短语")
        else:
            print(f"❌ 错误！加工用圆圈表示")
    
    def practice_dfd_data_store(self):
        """练习：DFD数据存储 ⭐重点"""
        print(f"\n【DFD题】数据存储用什么图形？")
        user_answer = input("你的答案：")
        correct = '双横线'
        
        self.total += 1
        if '横线' in user_answer or '线' in user_answer:
            self.score += 1
            print(f"✅ 正确！数据存储用双横线表示")
            print("💡 技巧：找题目中的'表/文件/数据库'")
        else:
            print(f"❌ 错误！数据存储用双横线表示")
    
    def practice_dfd_find_entity(self):
        """练习：DFD找外部实体 ⭐重点"""
        print(f"\n【DFD题】如何找外部实体？")
        user_answer = input("你的答案：")
        correct = '找人/系统/部门'
        
        self.total += 1
        if '人' in user_answer or '系统' in user_answer or '部门' in user_answer:
            self.score += 1
            print(f"✅ 正确！找外部实体：人/系统/部门")
        else:
            print(f"❌ 错误！找外部实体：人/系统/部门")
    
    # ========== ER图练习（第2题）==========
    
    def practice_er_entity(self):
        """练习：ER实体 ⭐重点"""
        print(f"\n【ER题】实体用什么图形？")
        user_answer = input("你的答案：")
        correct = '矩形'
        
        self.total += 1
        if '矩形' in user_answer or '方框' in user_answer:
            self.score += 1
            print(f"✅ 正确！实体用矩形表示")
            print("💡 技巧：找题目中的核心对象")
        else:
            print(f"❌ 错误！实体用矩形表示")
    
    def practice_er_relationship(self):
        """练习：ER联系 ⭐重点"""
        print(f"\n【ER题】联系用什么图形？")
        user_answer = input("你的答案：")
        correct = '菱形'
        
        self.total += 1
        if '菱形' in user_answer:
            self.score += 1
            print(f"✅ 正确！联系用菱形表示")
            print("💡 技巧：找实体间的关系动词")
        else:
            print(f"❌ 错误！联系用菱形表示")
    
    def practice_er_attribute(self):
        """练习：ER属性 ⭐重点"""
        print(f"\n【ER题】属性用什么图形？")
        user_answer = input("你的答案：")
        correct = '椭圆'
        
        self.total += 1
        if '椭圆' in user_answer or '圆' in user_answer:
            self.score += 1
            print(f"✅ 正确！属性用椭圆表示")
            print("💡 技巧：找实体的特征描述")
        else:
            print(f"❌ 错误！属性用椭圆表示")
    
    def practice_er_mn_relation(self):
        """练习：ER M:N联系转关系模式 ⭐重点"""
        print(f"\n【ER题】M:N联系如何转关系模式？")
        user_answer = input("你的答案：")
        correct = '单独建表，包含两边主键'
        
        self.total += 1
        if '单独' in user_answer or '建表' in user_answer:
            self.score += 1
            print(f"✅ 正确！M:N联系单独建表，包含两边主键")
            print("💡 例如：选课(学号,课程号,成绩)")
        else:
            print(f"❌ 错误！M:N联系单独建表，包含两边主键")
    
    # ========== UML图练习（第3题）==========
    
    def practice_uml_find_attribute(self):
        """练习：UML找属性 ⭐重点"""
        print(f"\n【UML题】类图属性从哪里找？")
        user_answer = input("你的答案：")
        correct = '找名词'
        
        self.total += 1
        if '名词' in user_answer:
            self.score += 1
            print(f"✅ 正确！属性从题目描述找名词")
        else:
            print(f"❌ 错误！属性从题目描述找名词")
    
    def practice_uml_find_method(self):
        """练习：UML找方法 ⭐重点"""
        print(f"\n【UML题】类图方法从哪里找？")
        user_answer = input("你的答案：")
        correct = '找动词'
        
        self.total += 1
        if '动词' in user_answer:
            self.score += 1
            print(f"✅ 正确！方法从题目描述找动词")
        else:
            print(f"❌ 错误！方法从题目描述找动词")
    
    def practice_uml_aggregation_vs_composition(self):
        """练习：UML聚合vs组合 ⭐重点"""
        print(f"\n【UML题】聚合和组合的区别？")
        user_answer = input("你的答案：")
        correct = '聚合可独立（空心），组合不可独立（实心）'
        
        self.total += 1
        if '独立' in user_answer or '空心' in user_answer or '实心' in user_answer:
            self.score += 1
            print(f"✅ 正确！聚合可独立（空心菱形），组合不可独立（实心菱形）")
        else:
            print(f"❌ 错误！聚合可独立（空心），组合不可独立（实心）")
    
    def practice_uml_usecase_participant(self):
        """练习：UML用例图参与者 ⭐重点"""
        print(f"\n【UML题】用例图参与者用什么图形？")
        user_answer = input("你的答案：")
        correct = '人形图标'
        
        self.total += 1
        if '人' in user_answer or '人形' in user_answer:
            self.score += 1
            print(f"✅ 正确！参与者用人形图标表示")
            print("💡 技巧：找与系统交互的人/系统")
        else:
            print(f"❌ 错误！参与者用人形图标表示")
    
    def practice_uml_include(self):
        """练习：UML include ⭐重点"""
        print(f"\n【UML题】include关系含义？")
        user_answer = input("你的答案：")
        correct = '必须包含的用例'
        
        self.total += 1
        if '必须' in user_answer or '包含' in user_answer:
            self.score += 1
            print(f"✅ 正确！include表示必须包含的用例")
        else:
            print(f"❌ 错误！include表示必须包含的用例")
    
    # ========== Java程序设计练习（第5题）==========
    
    def practice_java_inheritance(self):
        """练习：Java继承 ⭐重点"""
        print(f"\n【Java题】Java继承用什么关键字？")
        user_answer = input("你的答案：")
        correct = 'extends'
        
        self.total += 1
        if 'extends' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！Java继承用 extends 关键字")
        else:
            print(f"❌ 错误！Java继承用 extends 关键字")
    
    def practice_java_interface(self):
        """练习：Java接口实现 ⭐重点"""
        print(f"\n【Java题】Java实现接口用什么关键字？")
        user_answer = input("你的答案：")
        correct = 'implements'
        
        self.total += 1
        if 'implements' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！Java实现接口用 implements 关键字")
        else:
            print(f"❌ 错误！Java实现接口用 implements 关键字")
    
    def practice_java_override(self):
        """练习：Java重写 ⭐重点"""
        print(f"\n【Java题】方法重写用什么注解？")
        user_answer = input("你的答案：")
        correct = '@Override'
        
        self.total += 1
        if 'override' in user_answer.lower() or '@' in user_answer:
            self.score += 1
            print(f"✅ 正确！方法重写用 @Override 注解")
        else:
            print(f"❌ 错误！方法重写用 @Override 注解")
    
    def practice_java_list(self):
        """练习：Java List ⭐重点"""
        print(f"\n【Java题】List接口常用实现类？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['ArrayList', 'LinkedList']
        
        self.total += 1
        if 'ArrayList' in user_answer or 'LinkedList' in user_answer:
            self.score += 1
            print(f"✅ 正确！List实现类：ArrayList、LinkedList")
        else:
            print(f"❌ 错误！List实现类：ArrayList、LinkedList")
    
    def practice_java_map(self):
        """练习：Java Map ⭐重点"""
        print(f"\n【Java题】Map接口常用实现类？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['HashMap', 'TreeMap']
        
        self.total += 1
        if 'HashMap' in user_answer or 'TreeMap' in user_answer:
            self.score += 1
            print(f"✅ 正确！Map实现类：HashMap、TreeMap")
        else:
            print(f"❌ 错误！Map实现类：HashMap、TreeMap")
    
    def practice_java_new(self):
        """练习：Java创建对象 ⭐重点"""
        print(f"\n【Java题】创建对象用什么关键字？")
        user_answer = input("你的答案：")
        correct = 'new'
        
        self.total += 1
        if 'new' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！创建对象用 new 关键字")
        else:
            print(f"❌ 错误！创建对象用 new 关键字")
    
    def practice_java_super(self):
        """练习：Java调用父类方法"""
        print(f"\n【Java题】调用父类方法用什么关键字？")
        user_answer = input("你的答案：")
        correct = 'super'
        
        self.total += 1
        if 'super' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！调用父类方法用 super 关键字")
        else:
            print(f"❌ 错误！调用父类方法用 super 关键字")
    
    def practice_java_try_catch(self):
        """练习：Java异常处理 ⭐重点"""
        print(f"\n【Java题】异常捕获用什么结构？")
        user_answer = input("你的答案：")
        correct = 'try-catch'
        
        self.total += 1
        if 'try' in user_answer.lower() and 'catch' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！异常捕获用 try-catch 结构")
        else:
            print(f"❌ 错误！异常捕获用 try-catch 结构")
    
    # ========== 综合练习 ==========
    
    def practice_random(self):
        """随机练习"""
        practices = [
            # DFD
            self.practice_dfd_external_entity,
            self.practice_dfd_process,
            self.practice_dfd_find_entity,
            # ER
            self.practice_er_entity,
            self.practice_er_relationship,
            self.practice_er_mn_relation,
            # UML
            self.practice_uml_find_attribute,
            self.practice_uml_find_method,
            self.practice_uml_aggregation_vs_composition,
            # Java
            self.practice_java_inheritance,
            self.practice_java_interface,
            self.practice_java_list,
        ]
        random.choice(practices)()
    
    def practice_by_topic(self):
        """按主题练习"""
        print("\n选择练习主题：")
        print("1. DFD图（第1题）")
        print("2. ER图（第2题）")
        print("3. UML图（第3题）")
        print("4. Java程序设计（第5题）")
        
        choice = input("输入数字：")
        
        if choice == '1':
            practices = [
                self.practice_dfd_external_entity,
                self.practice_dfd_process,
                self.practice_dfd_data_store,
                self.practice_dfd_find_entity,
            ]
            for p in practices:
                p()
        elif choice == '2':
            practices = [
                self.practice_er_entity,
                self.practice_er_relationship,
                self.practice_er_attribute,
                self.practice_er_mn_relation,
            ]
            for p in practices:
                p()
        elif choice == '3':
            practices = [
                self.practice_uml_find_attribute,
                self.practice_uml_find_method,
                self.practice_uml_aggregation_vs_composition,
                self.practice_uml_usecase_participant,
                self.practice_uml_include,
            ]
            for p in practices:
                p()
        elif choice == '4':
            practices = [
                self.practice_java_inheritance,
                self.practice_java_interface,
                self.practice_java_override,
                self.practice_java_list,
                self.practice_java_map,
                self.practice_java_new,
                self.practice_java_try_catch,
            ]
            for p in practices:
                p()
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*50}")
        print(f"📊 综合训练完成！得分：{self.score}/{self.total}")
        if self.score == self.total:
            print("🎉 全对！下午题掌握得很好！考试必过！")
        elif self.score >= self.total * 0.8:
            print("👍 不错！继续保持！")
        else:
            print("💪 还需努力！重点复习薄弱题型")
        print("="*50)
    
    def run(self):
        """运行练习"""
        print("="*50)
        print("下午题综合训练 ⭐模拟考试")
        print("="*50)
        print("\n涵盖题型：")
        print("- DFD图（第1题）⭐必做")
        print("- ER图（第2题）⭐必做")
        print("- UML图（第3题）⭐必做")
        print("- Java程序设计（第5题）⭐推荐选做")
        print("\n策略：必做1、2、3题（45分），选做5题")
        print("="*50)
        print("\n练习模式：")
        print("1. 按主题练习")
        print("2. 随机练习")
        print("3. 综合练习（全部题型）")
        print("0. 退出")
        
        while True:
            choice = input("\n选择模式（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_by_topic()
            elif choice == '2':
                count = input("练习次数（默认5）：")
                n = int(count) if count else 5
                for _ in range(n):
                    self.practice_random()
            elif choice == '3':
                # 全部题型各练一次
                practices = [
                    self.practice_dfd_external_entity,
                    self.practice_dfd_process,
                    self.practice_dfd_find_entity,
                    self.practice_er_entity,
                    self.practice_er_relationship,
                    self.practice_er_mn_relation,
                    self.practice_uml_find_attribute,
                    self.practice_uml_find_method,
                    self.practice_uml_aggregation_vs_composition,
                    self.practice_java_inheritance,
                    self.practice_java_interface,
                    self.practice_java_list,
                    self.practice_java_override,
                ]
                for p in practices:
                    p()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    training = 下午题综合训练()
    training.run()