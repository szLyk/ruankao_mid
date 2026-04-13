#!/usr/bin/env python3
"""
DFD图练习脚本
用于练习数据流图补全技巧
"""

import random

class DFD练习:
    """DFD图练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_external_entity(self):
        """练习：外部实体 ⭐重点"""
        print(f"\n【题目】DFD中外部实体用什么图形？")
        user_answer = input("你的答案：")
        correct = '方框'
        
        self.total += 1
        if '方框' in user_answer or '矩形' in user_answer:
            self.score += 1
            print(f"✅ 正确！外部实体用方框表示")
        else:
            print(f"❌ 错误！外部实体用方框表示")
    
    def practice_process(self):
        """练习：加工/处理 ⭐重点"""
        print(f"\n【题目】DFD中加工用什么图形？")
        user_answer = input("你的答案：")
        correct = '圆圈或椭圆'
        
        self.total += 1
        if '圆' in user_answer or '椭圆' in user_answer:
            self.score += 1
            print(f"✅ 正确！加工用圆圈或椭圆表示")
        else:
            print(f"❌ 错误！加工用圆圈或椭圆表示")
    
    def practice_data_flow(self):
        """练习：数据流 ⭐重点"""
        print(f"\n【题目】DFD中数据流用什么表示？")
        user_answer = input("你的答案：")
        correct = '箭头'
        
        self.total += 1
        if '箭头' in user_answer:
            self.score += 1
            print(f"✅ 正确！数据流用箭头表示")
        else:
            print(f"❌ 错误！数据流用箭头表示")
    
    def practice_data_store(self):
        """练习：数据存储 ⭐重点"""
        print(f"\n【题目】DFD中数据存储用什么图形？")
        user_answer = input("你的答案：")
        correct = '双横线'
        
        self.total += 1
        if '横线' in user_answer or '线' in user_answer:
            self.score += 1
            print(f"✅ 正确！数据存储用双横线表示")
        else:
            print(f"❌ 错误！数据存储用双横线表示")
    
    def practice_external_entity_meaning(self):
        """练习：外部实体含义 ⭐重点"""
        print(f"\n【题目】外部实体是什么？")
        user_answer = input("你的答案：")
        correct = '系统外部的人/系统/部门'
        
        self.total += 1
        if '外部' in user_answer and ('人' in user_answer or '系统' in user_answer):
            self.score += 1
            print(f"✅ 正确！外部实体：系统外部的人/系统/部门")
            print(f"   例：用户、管理员、银行系统")
        else:
            print(f"❌ 错误！外部实体：系统外部的人/系统/部门")
    
    def practice_process_meaning(self):
        """练习：加工含义 ⭐重点"""
        print(f"\n【题目】加工是什么？")
        user_answer = input("你的答案：")
        correct = '数据处理过程'
        
        self.total += 1
        if '处理' in user_answer or '加工' in user_answer:
            self.score += 1
            print(f"✅ 正确！加工：数据处理过程")
            print(f"   例：处理订单、计算金额")
        else:
            print(f"❌ 错误！加工：数据处理过程")
    
    def practice_find_external_entity(self):
        """练习：找外部实体技巧 ⭐重点"""
        print(f"\n【题目】DFD补全时，如何找外部实体？")
        user_answer = input("你的答案：")
        correct = '找题目描述中的人/系统/部门'
        
        self.total += 1
        if '人' in user_answer or '系统' in user_answer:
            self.score += 1
            print(f"✅ 正确！找外部实体：")
            print(f"   找题目描述中的"人"、"系统"、"部门"")
            print(f"   例：用户、管理员、银行系统")
        else:
            print(f"❌ 错误！找外部实体：找"人/系统/部门"")
    
    def practice_find_process(self):
        """练习：找加工技巧 ⭐重点"""
        print(f"\n【题目】DFD补全时，如何找加工？")
        user_answer = input("你的答案：")
        correct = '找动词：处理、计算、生成'
        
        self.total += 1
        if '动词' in user_answer or '处理' in user_answer:
            self.score += 1
            print(f"✅ 正确！找加工：")
            print(f"   找动词：处理、计算、生成、验证")
            print(f"   例：处理订单、计算金额、生成报表")
        else:
            print(f"❌ 错误！找加工：找动词")
    
    def practice_find_data_store(self):
        """练习：找数据存储 ⭐重点"""
        print(f"\n【题目】DFD补全时，如何找数据存储？")
        user_answer = input("你的答案：")
        correct = '找存储相关词：数据库、文件、表'
        
        self.total += 1
        if '存储' in user_answer or '数据库' in user_answer or '文件' in user_answer:
            self.score += 1
            print(f"✅ 正确！找数据存储：")
            print(f"   找存储相关词：数据库、文件、表")
            print(f"   例：订单表、用户信息库")
        else:
            print(f"❌ 错误！找数据存储：找"数据库/文件/表"")
    
    def practice_example_external(self):
        """练习：外部实体示例 ⭐重点"""
        examples = [
            ('用户下单'，'用户'),
            ('银行验证支付'，'银行'),
            ('系统通知管理员'，'管理员'),
        ]
        
        example, correct = random.choice(examples)
        
        print(f"\n【题目】"{example}"中的外部实体是？")
        user_answer = input("你的答案：")
        
        self.total += 1
        if user_answer.strip() in correct:
            self.score += 1
            print(f"✅ 正确！答案是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
    
    def practice_example_process(self):
        """练习：加工示例 ⭐重点"""
        examples = [
            ('处理订单信息'，'处理订单'),
            ('计算订单金额'，'计算金额'),
            ('生成销售报表'，'生成报表'),
        ]
        
        example, correct = random.choice(examples)
        
        print(f"\n【题目】"{example}"中的加工是？")
        user_answer = input("你的答案：")
        
        self.total += 1
        if user_answer.strip() in correct:
            self.score += 1
            print(f"✅ 正确！答案是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
    
    def practice_dfd_sequence(self):
        """练习：DFD解题顺序 ⭐重点"""
        print(f"\n【题目】DFD补全解题顺序？")
        user_answer = input("你的答案：")
        correct = '找外部实体→找加工→找数据流→找数据存储'
        
        self.total += 1
        if '外部' in user_answer:
            self.score += 1
            print(f"✅ 正确！DFD补全顺序：")
            print(f"   1. 找外部实体（人/系统/部门）")
            print(f"   2. 找加工（动词）")
            print(f"   3. 找数据流（数据传递）")
            print(f"   4. 找数据存储（数据库/文件）")
        else:
            print(f"❌ 错误！DFD补全顺序：")
            print(f"   1. 找外部实体")
            print(f"   2. 找加工")
            print(f"   3. 找数据流")
            print(f"   4. 找数据存储")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("DFD图练习（下午题1）")
        print("="*40)
        print("\n练习内容：")
        print("1. 外部实体图形 ⭐重点")
        print("2. 加工图形 ⭐重点")
        print("3. 数据流图形 ⭐重点")
        print("4. 数据存储图形 ⭐重点")
        print("5. 外部实体含义 ⭐重点")
        print("6. 加工含义 ⭐重点")
        print("7. 找外部实体技巧 ⭐重点")
        print("8. 找加工技巧 ⭐重点")
        print("9. 找数据存储技巧 ⭐重点")
        print("10. 外部实体示例 ⭐重点")
        print("11. 加工示例 ⭐重点")
        print("12. DFD解题顺序 ⭐重点")
        print("13. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_external_entity()
            elif choice == '2':
                self.practice_process()
            elif choice == '3':
                self.practice_data_flow()
            elif choice == '4':
                self.practice_data_store()
            elif choice == '5':
                self.practice_external_entity_meaning()
            elif choice == '6':
                self.practice_process_meaning()
            elif choice == '7':
                self.practice_find_external_entity()
            elif choice == '8':
                self.practice_find_process()
            elif choice == '9':
                self.practice_find_data_store()
            elif choice == '10':
                self.practice_example_external()
            elif choice == '11':
                self.practice_example_process()
            elif choice == '12':
                self.practice_dfd_sequence()
            elif choice == '13':
                types = [
                    self.practice_find_external_entity,
                    self.practice_find_process,
                    self.practice_example_external,
                    self.practice_dfd_sequence,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = DFD练习()
    practice.run()