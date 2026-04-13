#!/usr/bin/env python3
"""
范式练习脚本
用于练习1NF、2NF、3NF、BCNF判断
"""

import random

class 范式练习:
    """范式练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_1nf(self):
        """练习：1NF"""
        print(f"\n【题目】1NF的条件是什么？")
        user_answer = input("你的答案：")
        correct = '属性不可再分'
        
        self.total += 1
        if '不可再分' in user_answer or '原子' in user_answer:
            self.score += 1
            print(f"✅ 正确！1NF：属性不可再分（原子性）")
        else:
            print(f"❌ 错误！1NF：属性不可再分（原子性）")
    
    def practice_2nf(self):
        """练习：2NF ⭐重点"""
        print(f"\n【题目】2NF的条件是什么？")
        user_answer = input("你的答案：")
        correct = '消除非主属性对码的部分依赖'
        
        self.total += 1
        if '部分依赖' in user_answer:
            self.score += 1
            print(f"✅ 正确！2NF：消除非主属性对码的部分依赖")
            print(f"   部分依赖：非主属性依赖于码的一部分")
        else:
            print(f"❌ 错误！2NF：消除非主属性对码的部分依赖")
    
    def practice_3nf(self):
        """练习：3NF ⭐重点"""
        print(f"\n【题目】3NF的条件是什么？")
        user_answer = input("你的答案：")
        correct = '消除非主属性对码的传递依赖'
        
        self.total += 1
        if '传递依赖' in user_answer:
            self.score += 1
            print(f"✅ 正确！3NF：消除非主属性对码的传递依赖")
            print(f"   传递依赖：非主属性依赖于其他非主属性")
        else:
            print(f"❌ 错误！3NF：消除非主属性对码的传递依赖")
    
    def practice_bcnf(self):
        """练习：BCNF ⭐重点"""
        print(f"\n【题目】BCNF的条件是什么？")
        user_answer = input("你的答案：")
        correct = '主属性不部分/传递依赖于码'
        
        self.total += 1
        if '主属性' in user_answer:
            self.score += 1
            print(f"✅ 正确！BCNF：主属性不部分/传递依赖于码")
            print(f"   消除所有依赖问题")
        else:
            print(f"❌ 错误！BCNF：主属性不部分/传递依赖于码")
    
    def practice_candidate_key(self):
        """练习：候选码定义 ⭐重点"""
        print(f"\n【题目】候选码是什么？")
        user_answer = input("你的答案：")
        correct = '能唯一标识元组的最小属性集'
        
        self.total += 1
        if '唯一标识' in user_answer and '最小' in user_answer:
            self.score += 1
            print(f"✅ 正确！候选码：能唯一标识元组的最小属性集")
        else:
            print(f"❌ 错误！候选码：能唯一标识元组的最小属性集")
    
    def practice_primary_attribute(self):
        """练习：主属性定义"""
        print(f"\n【题目】主属性是什么？")
        user_answer = input("你的答案：")
        correct = '包含在任何候选码中的属性'
        
        self.total += 1
        if '候选码' in user_answer:
            self.score += 1
            print(f"✅ 正确！主属性：包含在任何候选码中的属性")
        else:
            print(f"❌ 错误！主属性：包含在任何候选码中的属性")
    
    def practice_non_primary_attribute(self):
        """练习：非主属性定义"""
        print(f"\n【题目】非主属性是什么？")
        user_answer = input("你的答案：")
        correct = '不包含在任何候选码中的属性'
        
        self.total += 1
        if '不包含' in user_answer:
            self.score += 1
            print(f"✅ 正确！非主属性：不包含在任何候选码中的属性")
        else:
            print(f"❌ 错误！非主属性：不包含在任何候选码中的属性")
    
    def practice_partial_dependency(self):
        """练习：部分依赖 ⭐重点"""
        print(f"\n【题目】部分依赖是什么？")
        user_answer = input("你的答案：")
        correct = '非主属性依赖于码的一部分'
        
        self.total += 1
        if '一部分' in user_answer:
            self.score += 1
            print(f"✅ 正确！部分依赖：非主属性依赖于码的一部分")
            print(f"   例：码是(A,B)，但C只依赖于A")
        else:
            print(f"❌ 错误！部分依赖：非主属性依赖于码的一部分")
    
    def practice_transitive_dependency(self):
        """练习：传递依赖 ⭐重点"""
        print(f"\n【题目】传递依赖是什么？")
        user_answer = input("你的答案：")
        correct = '非主属性依赖于其他非主属性'
        
        self.total += 1
        if '非主属性' in user_answer and '依赖' in user_answer:
            self.score += 1
            print(f"✅ 正确！传递依赖：非主属性依赖于其他非主属性")
            print(f"   例：A→B→C，C传递依赖于A")
        else:
            print(f"❌ 错误！传递依赖：非主属性依赖于其他非主属性")
    
    def practice_nf_order(self):
        """练习：范式级别顺序 ⭐重点"""
        print(f"\n【题目】范式级别从低到高排序？")
        user_answer = input("你的答案：")
        correct = '1NF → 2NF → 3NF → BCNF'
        
        self.total += 1
        if '1NF' in user_answer and 'BCNF' in user_answer:
            self.score += 1
            print(f"✅ 正确！范式级别：1NF → 2NF → 3NF → BCNF")
        else:
            print(f"❌ 错误！范式级别：1NF → 2NF → 3NF → BCNF")
    
    def practice_find_candidate_key(self):
        """练习：找候选码步骤 ⭐重点"""
        print(f"\n【题目】找候选码的步骤？")
        print("请按顺序说出步骤")
        user_answer = input("你的答案：")
        
        self.total += 1
        # 简化判断
        print(f"✅ 找候选码步骤：")
        print(f"   1. 找能唯一标识元组的最小属性集")
        print(f"   2. 根据函数依赖确定")
        print(f"   3. 能推导所有属性的属性集就是候选码")
    
    def practice_judge_nf(self):
        """练习：判断范式级别 ⭐重点必考"""
        print(f"\n【题目】判断范式级别的步骤？")
        user_answer = input("你的答案：")
        correct = '找候选码→找主属性→找非主属性→判断依赖类型'
        
        self.total += 1
        if '候选码' in user_answer and '依赖' in user_answer:
            self.score += 1
            print(f"✅ 正确！判断范式步骤：")
            print(f"   1. 找候选码")
            print(f"   2. 找主属性")
            print(f"   3. 找非主属性")
            print(f"   4. 判断依赖类型（部分/传递）")
        else:
            print(f"❌ 错误！判断范式步骤：")
            print(f"   1. 找候选码")
            print(f"   2. 找主属性")
            print(f"   3. 找非主属性")
            print(f"   4. 判断依赖类型（部分/传递）")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("范式练习（1NF/2NF/3NF/BCNF）")
        print("="*40)
        print("\n练习内容：")
        print("1. 1NF条件")
        print("2. 2NF条件 ⭐重点")
        print("3. 3NF条件 ⭐重点")
        print("4. BCNF条件 ⭐重点")
        print("5. 候选码定义 ⭐重点")
        print("6. 主属性定义")
        print("7. 非主属性定义")
        print("8. 部分依赖 ⭐重点")
        print("9. 传递依赖 ⭐重点")
        print("10. 范式级别顺序 ⭐重点")
        print("11. 找候选码步骤 ⭐重点")
        print("12. 判断范式步骤 ⭐重点必考")
        print("13. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_1nf()
            elif choice == '2':
                self.practice_2nf()
            elif choice == '3':
                self.practice_3nf()
            elif choice == '4':
                self.practice_bcnf()
            elif choice == '5':
                self.practice_candidate_key()
            elif choice == '6':
                self.practice_primary_attribute()
            elif choice == '7':
                self.practice_non_primary_attribute()
            elif choice == '8':
                self.practice_partial_dependency()
            elif choice == '9':
                self.practice_transitive_dependency()
            elif choice == '10':
                self.practice_nf_order()
            elif choice == '11':
                self.practice_find_candidate_key()
            elif choice == '12':
                self.practice_judge_nf()
            elif choice == '13':
                types = [
                    self.practice_2nf,
                    self.practice_3nf,
                    self.practice_partial_dependency,
                    self.practice_transitive_dependency,
                    self.practice_judge_nf,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 范式练习()
    practice.run()