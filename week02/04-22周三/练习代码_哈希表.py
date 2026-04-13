#!/usr/bin/env python3
"""
哈希表练习脚本
用于练习哈希冲突解决方法
"""

import random

class 哈希表练习:
    """哈希表练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_hash_complexity(self):
        """练习：哈希查找时间复杂度"""
        print(f"\n【题目】哈希查找的理想时间复杂度是？")
        user_answer = input("你的答案：").upper()
        correct = 'O(1)'
        
        self.total += 1
        if user_answer.replace(' ', '') == correct:
            self.score += 1
            print(f"✅ 正确！哈希查找理想情况下O(1)")
        else:
            print(f"❌ 错误！哈希查找理想情况下O(1)")
            print(f"   通过哈希函数直接定位")
    
    def practice_hash_conflict_methods(self):
        """练习：哈希冲突解决方法 ⭐重点"""
        print(f"\n【题目】哈希冲突的常用解决方法有哪些？")
        user_answer = input("你的答案（说出一种）：")
        correct_methods = ['开放定址法', '链地址法', '再哈希法', '公共溢出区']
        
        self.total += 1
        if any(method in user_answer for method in correct_methods):
            self.score += 1
            print(f"✅ 正确！哈希冲突解决方法：")
            print(f"   1. 开放定址法")
            print(f"   2. 链地址法")
            print(f"   3. 再哈希法")
            print(f"   4. 公共溢出区")
        else:
            print(f"❌ 错误！哈希冲突解决方法：")
            print(f"   1. 开放定址法")
            print(f"   2. 链地址法")
            print(f"   3. 再哈希法")
            print(f"   4. 公共溢出区")
    
    def practice_open_addressing(self):
        """练习：开放定址法"""
        print(f"\n【题目】开放定址法的原理是什么？")
        user_answer = input("你的答案：")
        correct = '冲突时找下一个空位'
        
        self.total += 1
        if '下一个' in user_answer or '空位' in user_answer or '探测' in user_answer:
            self.score += 1
            print(f"✅ 正确！开放定址法：冲突时找下一个空位")
        else:
            print(f"❌ 错误！开放定址法：冲突时找下一个空位")
            print(f"   线性探测：H(key) = (H(key)+1) mod m")
            print(f"   二次探测：H(key) = (H(key)+d²) mod m")
    
    def practice_chaining(self):
        """练习：链地址法 ⭐重点"""
        print(f"\n【题目】链地址法的原理是什么？")
        user_answer = input("你的答案：")
        correct = '同位置元素用链表连接'
        
        self.total += 1
        if '链表' in user_answer or '链' in user_answer:
            self.score += 1
            print(f"✅ 正确！链地址法：同位置元素用链表连接")
        else:
            print(f"❌ 错误！链地址法：同位置元素用链表连接")
            print(f"   优点：不产生堆积现象")
    
    def practice_chaining_advantage(self):
        """练习：链地址法优点 ⭐重点"""
        print(f"\n【题目】链地址法相比开放定址法的优点是？")
        user_answer = input("你的答案：")
        correct = '不产生堆积现象'
        
        self.total += 1
        if '堆积' in user_answer or '聚集' in user_answer:
            self.score += 1
            print(f"✅ 正确！链地址法不产生堆积现象")
        else:
            print(f"❌ 错误！链地址法不产生堆积现象")
            print(f"   开放定址法可能产生堆积（连续占用）")
            print(f"   链地址法避免这个问题")
    
    def practice_hash_function(self):
        """练习：哈希函数设计"""
        print(f"\n【题目】最常用的哈希函数设计方法是？")
        user_answer = input("你的答案：")
        correct = '除留余数法'
        
        self.total += 1
        if '余数' in user_answer or 'mod' in user_answer.lower() or '除' in user_answer:
            self.score += 1
            print(f"✅ 正确！除留余数法：H(key) = key mod p")
        else:
            print(f"❌ 错误！最常用的是除留余数法")
            print(f"   H(key) = key mod p（p≤表长）")
    
    def practice_load_factor(self):
        """练习：装填因子"""
        print(f"\n【题目】哈希表的装填因子α是什么？")
        user_answer = input("你的答案：")
        correct = '元素数/表长'
        
        self.total += 1
        if '元素' in user_answer and '表长' in user_answer or 'n/m' in user_answer.lower():
            self.score += 1
            print(f"✅ 正确！装填因子α = 元素数/表长")
        else:
            print(f"❌ 错误！装填因子α = 元素数/表长")
            print(f"   α = n/m，影响查找效率")
    
    def practice_btree(self):
        """练习：B树"""
        print(f"\n【题目】B树的特点是什么？")
        user_answer = input("你的答案：")
        
        self.total += 1
        if '多路' in user_answer or '平衡' in user_answer or '磁盘' in user_answer:
            self.score += 1
            print(f"✅ 正确！B树是多路平衡查找树，适合磁盘存储")
        else:
            print(f"❌ B树是多路平衡查找树")
            print(f"   特点：节点存储多个关键字，减少磁盘IO")
    
    def practice_bplus_tree(self):
        """练习：B+树 ⭐重点"""
        print(f"\n【题目】B+树相比B树的区别？")
        user_answer = input("你的答案：")
        correct = '数据只在叶子节点，叶子节点链式连接'
        
        self.total += 1
        if '叶子' in user_answer and ('链' in user_answer or '连接' in user_answer):
            self.score += 1
            print(f"✅ 正确！B+树：数据只在叶子节点，叶子节点链式连接")
        else:
            print(f"❌ 错误！B+树特点：")
            print(f"   1. 数据只在叶子节点存储")
            print(f"   2. 叶子节点链式连接")
            print(f"   3. 查找效率稳定（都到叶子）")
    
    def practice_bplus_application(self):
        """练习：B+树应用 ⭐重点"""
        print(f"\n【题目】数据库索引通常用什么树？")
        user_answer = input("你的答案：")
        correct = 'B+树'
        
        self.total += 1
        if 'B+' in user_answer or 'B加' in user_answer:
            self.score += 1
            print(f"✅ 正确！数据库索引用B+树")
        else:
            print(f"❌ 错误！数据库索引用B+树")
            print(f"   B+树叶子节点链式连接，便于范围查询")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("哈希表 + B树练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 哈希查找时间复杂度")
        print("2. 哈希冲突解决方法 ⭐重点")
        print("3. 开放定址法")
        print("4. 链地址法 ⭐重点")
        print("5. 链地址法优点")
        print("6. 哈希函数设计")
        print("7. 装填因子")
        print("8. B树特点")
        print("9. B+树特点 ⭐重点")
        print("10. B+树应用")
        print("11. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_hash_complexity()
            elif choice == '2':
                self.practice_hash_conflict_methods()
            elif choice == '3':
                self.practice_open_addressing()
            elif choice == '4':
                self.practice_chaining()
            elif choice == '5':
                self.practice_chaining_advantage()
            elif choice == '6':
                self.practice_hash_function()
            elif choice == '7':
                self.practice_load_factor()
            elif choice == '8':
                self.practice_btree()
            elif choice == '9':
                self.practice_bplus_tree()
            elif choice == '10':
                self.practice_bplus_application()
            elif choice == '11':
                types = [
                    self.practice_hash_conflict_methods,
                    self.practice_chaining,
                    self.practice_bplus_tree,
                    self.practice_bplus_application,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 哈希表练习()
    practice.run()