#!/usr/bin/env python3
"""
ER图练习脚本
用于练习ER图基本元素和关系转换
"""

import random

class ER图练习:
    """ER图练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_entity(self):
        """练习：实体"""
        print(f"\n【题目】实体用什么图形表示？")
        user_answer = input("你的答案：")
        correct = '矩形'
        
        self.total += 1
        if '矩形' in user_answer:
            self.score += 1
            print(f"✅ 正确！实体用矩形表示")
        else:
            print(f"❌ 错误！实体用矩形表示")
    
    def practice_attribute(self):
        """练习：属性"""
        print(f"\n【题目】属性用什么图形表示？")
        user_answer = input("你的答案：")
        correct = '椭圆'
        
        self.total += 1
        if '椭圆' in user_answer or '圆形' in user_answer:
            self.score += 1
            print(f"✅ 正确！属性用椭圆表示")
        else:
            print(f"❌ 错误！属性用椭圆表示")
    
    def practice_relationship(self):
        """练习：关系"""
        print(f"\n【题目】关系用什么图形表示？")
        user_answer = input("你的答案：")
        correct = '菱形'
        
        self.total += 1
        if '菱形' in user_answer:
            self.score += 1
            print(f"✅ 正确！关系用菱形表示")
        else:
            print(f"❌ 错误！关系用菱形表示")
    
    def practice_1_1(self):
        """练习：1:1联系转换 ⭐重点"""
        print(f"\n【题目】1:1联系如何转换为关系模式？")
        user_answer = input("你的答案：")
        correct = '可合并到任一实体'
        
        self.total += 1
        if '合并' in user_answer or '任一' in user_answer:
            self.score += 1
            print(f"✅ 正确！1:1联系：可合并到任一实体")
            print(f"   或单独建立关系，加入两端主键")
        else:
            print(f"❌ 错误！1:1联系：可合并到任一实体")
    
    def practice_1_n(self):
        """练习：1:N联系转换 ⭐重点"""
        print(f"\n【题目】1:N联系如何转换为关系模式？")
        user_answer = input("你的答案：")
        correct = '合并到N端实体'
        
        self.total += 1
        if 'N端' in user_answer:
            self.score += 1
            print(f"✅ 正确！1:N联系：合并到N端实体")
            print(f"   加入1端主键")
        else:
            print(f"❌ 错误！1:N联系：合并到N端实体")
    
    def practice_m_n(self):
        """练习：M:N联系转换 ⭐重点必考"""
        print(f"\n【题目】M:N联系如何转换为关系模式？")
        user_answer = input("你的答案：")
        correct = '单独建立关系，包含两端主键'
        
        self.total += 1
        if '单独' in user_answer or '两端' in user_answer:
            self.score += 1
            print(f"✅ 正确！M:N联系：单独建立关系")
            print(f"   包含两端主键和联系属性")
        else:
            print(f"❌ 错误！M:N联系：单独建立关系")
            print(f"   包含两端主键和联系属性")
    
    def practice_entity_transform(self):
        """练习：实体转换"""
        print(f"\n【题目】每个实体如何转换为关系模式？")
        user_answer = input("你的答案：")
        correct = '每个实体单独一个关系'
        
        self.total += 1
        if '单独' in user_answer:
            self.score += 1
            print(f"✅ 正确！每个实体单独一个关系")
        else:
            print(f"❌ 错误！每个实体单独一个关系")
    
    def practice_example_1_n(self):
        """练习：1:N示例"""
        print(f"\n【题目】学生-班级（多学生属于一班）如何转换？")
        user_answer = input("你的答案：")
        correct = '班级主键加到学生关系中'
        
        self.total += 1
        if '学生' in user_answer and ('班级' in user_answer or 'N端' in user_answer):
            self.score += 1
            print(f"✅ 正确！学生是N端，班级主键加到学生关系中")
            print(f"   学生关系：(学号, 姓名, 班级号)")
        else:
            print(f"❌ 错误！学生是N端，班级主键加到学生关系中")
    
    def practice_example_m_n(self):
        """练习：M:N示例 ⭐重点"""
        print(f"\n【题目】学生-课程（多学生选多课程）如何转换？")
        user_answer = input("你的答案：")
        correct = '单独建立选课关系'
        
        self.total += 1
        if '选课' in user_answer or '单独' in user_answer:
            self.score += 1
            print(f"✅ 正确！单独建立选课关系")
            print(f"   学生关系：(学号, 姓名)")
            print(f"   课程关系：(课程号, 课程名)")
            print(f"   选课关系：(学号, 课程号, 成绩)")
        else:
            print(f"❌ 错误！单独建立选课关系")
            print(f"   学生关系：(学号, 姓名)")
            print(f"   课程关系：(课程号, 课程名)")
            print(f"   选课关系：(学号, 课程号, 成绩)")
    
    def practice_contact_type(self):
        """练习：联系类型"""
        contacts = [
            ('一对一联系', '1:1'),
            ('一对多联系', '1:N'),
            ('多对多联系', 'M:N'),
        ]
        
        contact, correct = random.choice(contacts)
        
        print(f"\n【题目】{contact}的表示方法是？")
        user_answer = input("你的答案：")
        
        self.total += 1
        if user_answer.strip().replace(' ', '') == correct.replace(':', ''):
            self.score += 1
            print(f"✅ 正确！答案是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("ER图练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 实体图形")
        print("2. 属性图形")
        print("3. 关系图形")
        print("4. 1:1联系转换 ⭐重点")
        print("5. 1:N联系转换 ⭐重点")
        print("6. M:N联系转换 ⭐重点必考")
        print("7. 实体转换")
        print("8. 1:N示例")
        print("9. M:N示例 ⭐重点")
        print("10. 联系类型")
        print("11. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_entity()
            elif choice == '2':
                self.practice_attribute()
            elif choice == '3':
                self.practice_relationship()
            elif choice == '4':
                self.practice_1_1()
            elif choice == '5':
                self.practice_1_n()
            elif choice == '6':
                self.practice_m_n()
            elif choice == '7':
                self.practice_entity_transform()
            elif choice == '8':
                self.practice_example_1_n()
            elif choice == '9':
                self.practice_example_m_n()
            elif choice == '10':
                self.practice_contact_type()
            elif choice == '11':
                types = [
                    self.practice_m_n,
                    self.practice_example_m_n,
                    self.practice_1_n,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = ER图练习()
    practice.run()