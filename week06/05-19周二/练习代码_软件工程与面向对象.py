#!/usr/bin/env python3
"""
软件工程+面向对象错题复习练习脚本
涵盖：开发模型、测试方法、CMM、ISO 9126、OO特性、UML关系 ⭐复习重点
"""

import random

class 软件工程与面向对象复习:
    """软件工程+面向对象复习练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    # ========== 软件开发模型 ⭐重点 ==========
    
    def practice_waterfall(self):
        """练习：瀑布模型 ⭐重点"""
        print(f"\n【开发模型】瀑布模型特点？")
        user_answer = input("你的答案：")
        correct = '阶段明确、文档驱动、线性'
        
        self.total += 1
        if '阶段' in user_answer or '文档' in user_answer or '线性' in user_answer:
            self.score += 1
            print(f"✅ 正确！瀑布模型：阶段明确、文档驱动、线性顺序")
            print("💡 适用：需求明确的项目")
        else:
            print(f"❌ 错误！瀑布模型：阶段明确、文档驱动、线性顺序")
    
    def practice_spiral(self):
        """练习：螺旋模型 ⭐⭐⭐最重点"""
        print(f"\n【开发模型】螺旋模型特点？")
        user_answer = input("你的答案：")
        correct = '迭代+风险分析'
        
        self.total += 1
        if '迭代' in user_answer or '风险' in user_answer:
            self.score += 1
            print(f"✅ 正确！螺旋模型：迭代+风险分析 ⭐重点")
            print("💡 适用：大型高风险项目")
        else:
            print(f"❌ 错误！螺旋模型：迭代+风险分析")
    
    def practice_spiral_stages(self):
        """练习：螺旋模型四阶段 ⭐重点"""
        print(f"\n【开发模型】螺旋模型四阶段？")
        user_answer = input("你的答案：")
        correct = '制定计划、风险分析、工程实施、客户评估'
        
        self.total += 1
        if '风险' in user_answer or '计划' in user_answer:
            self.score += 1
            print(f"✅ 正确！四阶段：制定计划→风险分析→工程实施→客户评估")
        else:
            print(f"❌ 错误！四阶段：制定计划→风险分析→工程实施→客户评估")
    
    def practice_agile(self):
        """练习：敏捷开发 ⭐重点"""
        print(f"\n【开发模型】敏捷开发特点？")
        user_answer = input("你的答案：")
        correct = '迭代快速、拥抱变化'
        
        self.total += 1
        if '迭代' in user_answer or '变化' in user_answer or '快速' in user_answer:
            self.score += 1
            print(f"✅ 正确！敏捷开发：迭代快速、拥抱变化、用户参与")
            print("💡 适用：需求变化频繁的项目")
        else:
            print(f"❌ 错误！敏捷开发：迭代快速、拥抱变化、用户参与")
    
    def practice_model_selection(self):
        """练习：模型选择 ⭐重点"""
        print(f"\n【开发模型】需求明确选哪种模型？")
        user_answer = input("你的答案：")
        correct = '瀑布模型'
        
        self.total += 1
        if '瀑布' in user_answer:
            self.score += 1
            print(f"✅ 正确！需求明确选瀑布模型")
        else:
            print(f"❌ 错误！需求明确选瀑布模型")
    
    def practice_model_high_risk(self):
        """练习：高风险项目模型 ⭐重点"""
        print(f"\n【开发模型】大型高风险项目选哪种模型？")
        user_answer = input("你的答案：")
        correct = '螺旋模型'
        
        self.total += 1
        if '螺旋' in user_answer:
            self.score += 1
            print(f"✅ 正确！大型高风险项目选螺旋模型（有风险分析）")
        else:
            print(f"❌ 错误！大型高风险项目选螺旋模型（有风险分析）")
    
    # ========== 软件测试 ⭐重点必考 ==========
    
    def practice_whitebox_definition(self):
        """练习：白盒测试定义 ⭐重点"""
        print(f"\n【测试】白盒测试是什么？")
        user_answer = input("你的答案：")
        correct = '基于代码内部逻辑'
        
        self.total += 1
        if '内部' in user_answer or '逻辑' in user_answer or '代码' in user_answer:
            self.score += 1
            print(f"✅ 正确！白盒测试：基于代码内部逻辑的测试")
        else:
            print(f"❌ 错误！白盒测试：基于代码内部逻辑的测试")
    
    def practice_blackbox_definition(self):
        """练习：黑盒测试定义 ⭐重点"""
        print(f"\n【测试】黑盒测试是什么？")
        user_answer = input("你的答案：")
        correct = '基于功能规格，不考虑内部'
        
        self.total += 1
        if '功能' in user_answer or '规格' in user_answer or '外部' in user_answer:
            self.score += 1
            print(f"✅ 正确！黑盒测试：基于功能规格，不考虑内部实现")
        else:
            print(f"❌ 错误！黑盒测试：基于功能规格，不考虑内部实现")
    
    def practice_whitebox_coverage(self):
        """练习：白盒覆盖顺序 ⭐⭐⭐最重点"""
        print(f"\n【测试】白盒测试覆盖从弱到强？")
        user_answer = input("你的答案：")
        correct = '语句→判断→条件→路径'
        
        self.total += 1
        if '语句' in user_answer or '判断' in user_answer or '路径' in user_answer:
            self.score += 1
            print(f"✅ 正确！语句→判断→条件→判断-条件→条件组合→路径 ⭐必背")
        else:
            print(f"❌ 错误！语句→判断→条件→判断-条件→条件组合→路径")
    
    def practice_path_coverage(self):
        """练习：路径覆盖 ⭐⭐⭐最重点"""
        print(f"\n【测试】白盒测试最强覆盖？")
        user_answer = input("你的答案：")
        correct = '路径覆盖'
        
        self.total += 1
        if '路径' in user_answer:
            self.score += 1
            print(f"✅ 正确！路径覆盖是白盒最强覆盖 ⭐重点必考")
            print("💡 覆盖所有可能的执行路径")
        else:
            print(f"❌ 错误！路径覆盖是白盒最强覆盖 ⭐重点必考")
    
    def practice_blackbox_methods(self):
        """练习：黑盒方法 ⭐重点"""
        print(f"\n【测试】黑盒测试方法有哪些？")
        user_answer = input("你的答案：")
        correct = ['等价类', '边界值', '因果图', '决策表']
        
        self.total += 1
        if any(c in user_answer for c in correct):
            self.score += 1
            print(f"✅ 正确！黑盒方法：等价类划分、边界值分析、因果图、决策表")
        else:
            print(f"❌ 错误！黑盒方法：等价类划分、边界值分析、因果图、决策表")
    
    def practice_boundary_value(self):
        """练习：边界值 ⭐重点"""
        print(f"\n【测试】边界值分析测试什么？")
        user_answer = input("你的答案：")
        correct = '边界情况'
        
        self.total += 1
        if '边界' in user_answer or '边' in user_answer:
            self.score += 1
            print(f"✅ 正确！边界值分析测试边界情况")
            print("💡 如：0、1、最大值-1、最大值")
        else:
            print(f"❌ 错误！边界值分析测试边界情况")
    
    # ========== 软件质量 ⭐重点 ==========
    
    def practice_cmm_levels(self):
        """练习：CMM五个等级 ⭐重点"""
        print(f"\n【质量】CMM五个等级名称？")
        user_answer = input("你的答案：")
        correct = '初始、可重复、已定义、已管理、优化'
        
        self.total += 1
        if '初始' in user_answer or '可重复' in user_answer or '优化' in user_answer:
            self.score += 1
            print(f"✅ 正确！CMM五级：初始→可重复→已定义→已管理→优化")
        else:
            print(f"❌ 错误！CMM五级：初始→可重复→已定义→已管理→优化")
    
    def practice_cmm_level5(self):
        """练习：CMM等级5 ⭐重点"""
        print(f"\n【质量】CMM等级5是什么？")
        user_answer = input("你的答案：")
        correct = '优化级'
        
        self.total += 1
        if '优化' in user_answer:
            self.score += 1
            print(f"✅ 正确！CMM等级5：优化级（持续改进）")
        else:
            print(f"❌ 错误！CMM等级5：优化级（持续改进）")
    
    def practice_iso_9126(self):
        """练习：ISO 9126六大特性 ⭐⭐⭐最重点"""
        print(f"\n【质量】ISO 9126六大质量特性？")
        user_answer = input("你的答案：")
        correct = ['功能', '可靠', '易用', '效率', '维护', '移植']
        
        self.total += 1
        if any(c in user_answer for c in correct):
            self.score += 1
            print(f"✅ 正确！六大特性：功能性、可靠性、易用性、效率性、可维护性、可移植性 ⭐重点必考")
        else:
            print(f"❌ 错误！六大特性：功能性、可靠性、易用性、效率性、可维护性、可移植性")
    
    # ========== 面向对象基础 ⭐重点必考 ==========
    
    def practice_oo_features(self):
        """练习：OO三大特性 ⭐重点"""
        print(f"\n【面向对象】三大特性？")
        user_answer = input("你的答案：")
        correct = '封装、继承、多态'
        
        self.total += 1
        if '封装' in user_answer or '继承' in user_answer or '多态' in user_answer:
            self.score += 1
            print(f"✅ 正确！三大特性：封装、继承、多态")
        else:
            print(f"❌ 错误！三大特性：封装、继承、多态")
    
    def practice_overload_vs_override(self):
        """练习：重载vs重写 ⭐⭐⭐最重点"""
        print(f"\n【面向对象】重载和重写区别？")
        user_answer = input("你的答案：")
        correct = '重载参数不同，重写参数相同'
        
        self.total += 1
        if '参数' in user_answer and ('不同' in user_answer or '相同' in user_answer):
            self.score += 1
            print(f"✅ 正确！重载：同类参数不同；重写：子类参数相同 ⭐重点必考")
            print("💡 重载：编译时多态；重写：运行时多态")
        else:
            print(f"❌ 错误！重载：同类参数不同；重写：子类参数相同")
    
    def practice_overload(self):
        """练习：重载定义 ⭐重点"""
        print(f"\n【面向对象】重载是什么？")
        user_answer = input("你的答案：")
        correct = '同类中多个同名方法，参数不同'
        
        self.total += 1
        if '同类' in user_answer or '参数' in user_answer or '不同' in user_answer:
            self.score += 1
            print(f"✅ 正确！重载：同类中多个同名方法，参数不同")
        else:
            print(f"❌ 错误！重载：同类中多个同名方法，参数不同")
    
    def practice_override(self):
        """练习：重写定义 ⭐重点"""
        print(f"\n【面向对象】重写是什么？")
        user_answer = input("你的答案：")
        correct = '子类重新定义父类方法，参数返回类型相同'
        
        self.total += 1
        if '子类' in user_answer or '父类' in user_answer:
            self.score += 1
            print(f"✅ 正确！重写：子类重新定义父类方法，参数返回类型相同")
        else:
            print(f"❌ 错误！重写：子类重新定义父类方法，参数返回类型相同")
    
    def practice_abstract_vs_interface(self):
        """练习：抽象类vs接口 ⭐⭐⭐最重点"""
        print(f"\n【面向对象】抽象类和接口区别？")
        user_answer = input("你的答案：")
        correct = '抽象类单继承，接口多实现'
        
        self.total += 1
        if '单继承' in user_answer or '多实现' in user_answer or '继承' in user_answer and '实现' in user_answer:
            self.score += 1
            print(f"✅ 正确！抽象类：单继承；接口：多实现 ⭐重点必考")
        else:
            print(f"❌ 错误！抽象类：单继承；接口：多实现")
    
    def practice_final_override(self):
        """练习：final不能重写 ⭐重点"""
        print(f"\n【面向对象】final方法可以重写吗？")
        user_answer = input("你的答案：")
        correct = '不可以'
        
        self.total += 1
        if '不' in user_answer:
            self.score += 1
            print(f"✅ 正确！final方法不能被重写")
        else:
            print(f"❌ 错误！final方法不能被重写")
    
    # ========== UML图关系 ⭐重点必考 ==========
    
    def practice_aggregation_symbol(self):
        """练习：聚合符号 ⭐重点"""
        print(f"\n【UML】聚合关系用什么符号？")
        user_answer = input("你的答案：")
        correct = '空心菱形'
        
        self.total += 1
        if '空心' in user_answer:
            self.score += 1
            print(f"✅ 正确！聚合：空心菱形")
        else:
            print(f"❌ 错误！聚合：空心菱形")
    
    def practice_composition_symbol(self):
        """练习：组合符号 ⭐重点"""
        print(f"\n【UML】组合关系用什么符号？")
        user_answer = input("你的答案：")
        correct = '实心菱形'
        
        self.total += 1
        if '实心' in user_answer:
            self.score += 1
            print(f"✅ 正确！组合：实心菱形")
        else:
            print(f"❌ 错误！组合：实心菱形")
    
    def practice_aggregation_vs_composition(self):
        """练习：聚合vs组合 ⭐⭐⭐最重点"""
        print(f"\n【UML】聚合和组合区别？")
        user_answer = input("你的答案：")
        correct = '聚合可独立（空心），组合不可独立（实心）'
        
        self.total += 1
        if '独立' in user_answer or '空心' in user_answer or '实心' in user_answer:
            self.score += 1
            print(f"✅ 正确！聚合可独立（空心菱形），组合不可独立（实心菱形）⭐重点必考")
        else:
            print(f"❌ 错误！聚合可独立（空心），组合不可独立（实心）")
    
    def practice_company_employee(self):
        """练习：公司-员工 ⭐重点"""
        print(f"\n【UML】公司-员工是什么关系？")
        user_answer = input("你的答案：")
        correct = '聚合'
        
        self.total += 1
        if '聚合' in user_answer:
            self.score += 1
            print(f"✅ 正确！公司-员工是聚合关系（员工可独立存在）")
        else:
            print(f"❌ 错误！公司-员工是聚合关系（员工可独立存在）")
    
    def practice_person_heart(self):
        """练习：人-心脏 ⭐重点"""
        print(f"\n【UML】人-心脏是什么关系？")
        user_answer = input("你的答案：")
        correct = '组合'
        
        self.total += 1
        if '组合' in user_answer:
            self.score += 1
            print(f"✅ 正确！人-心脏是组合关系（心脏不可独立存在）")
        else:
            print(f"❌ 错误！人-心脏是组合关系（心脏不可独立存在）")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*50}")
        print(f"📊 复习完成！得分：{self.score}/{self.total}")
        if self.score == self.total:
            print("🎉 全对！软件工程与面向对象掌握很好！")
        elif self.score >= self.total * 0.8:
            print("👍 不错！继续巩固重点概念！")
        else:
            print("💪 还需努力！重点记住：螺旋模型、路径覆盖、ISO 9126、重载vs重写、聚合vs组合")
    
    def run(self):
        """运行练习"""
        print("="*50)
        print("软件工程+面向对象错题复习 ⭐重点")
        print("="*50)
        print("\n复习重点：")
        print("1. 开发模型（螺旋模型）⭐重点")
        print("2. 软件测试（白盒覆盖）⭐⭐⭐最重点")
        print("3. 软件质量（CMM、ISO 9126）⭐重点")
        print("4. 面向对象（重载vs重写）⭐⭐⭐最重点")
        print("5. UML关系（聚合vs组合）⭐⭐⭐最重点")
        print("6. 综合复习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择复习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                practices = [
                    self.practice_spiral,
                    self.practice_spiral_stages,
                    self.practice_model_high_risk,
                ]
                for p in practices:
                    p()
            elif choice == '2':
                practices = [
                    self.practice_whitebox_coverage,
                    self.practice_path_coverage,
                    self.practice_blackbox_methods,
                ]
                for p in practices:
                    p()
            elif choice == '3':
                practices = [
                    self.practice_cmm_levels,
                    self.practice_cmm_level5,
                    self.practice_iso_9126,
                ]
                for p in practices:
                    p()
            elif choice == '4':
                practices = [
                    self.practice_oo_features,
                    self.practice_overload_vs_override,
                    self.practice_abstract_vs_interface,
                ]
                for p in practices:
                    p()
            elif choice == '5':
                practices = [
                    self.practice_aggregation_vs_composition,
                    self.practice_company_employee,
                    self.practice_person_heart,
                ]
                for p in practices:
                    p()
            elif choice == '6':
                practices = [
                    self.practice_spiral,
                    self.practice_path_coverage,
                    self.practice_iso_9126,
                    self.practice_overload_vs_override,
                    self.practice_aggregation_vs_composition,
                ]
                for p in practices:
                    p()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    review = 软件工程与面向对象复习()
    review.run()