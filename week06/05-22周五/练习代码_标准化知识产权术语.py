#!/usr/bin/env python3
"""
标准化/知识产权/术语错题复习练习脚本
考前记忆强化 ⭐重点背诵
"""

import random

class 标准化知识产权术语复习:
    """标准化/知识产权/术语复习练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    # ========== 标准化知识 ⭐背诵 ==========
    
    def practice_iso(self):
        """练习：ISO ⭐重点"""
        print(f"\n【标准化】ISO是什么？")
        user_answer = input("你的答案：")
        correct = '国际标准化组织'
        
        self.total += 1
        if '国际' in user_answer or '标准' in user_answer:
            self.score += 1
            print(f"✅ 正确！ISO：国际标准化组织")
        else:
            print(f"❌ 错误！ISO：国际标准化组织")
    
    def practice_gb(self):
        """练习：GB ⭐⭐⭐最重点"""
        print(f"\n【标准化】GB是什么标准？")
        user_answer = input("你的答案：")
        correct = '国家标准强制性'
        
        self.total += 1
        if '国家' in user_answer and ('强制' in user_answer or '强制' in user_answer):
            self.score += 1
            print(f"✅ 正确！GB：国家标准（强制性）⭐重点必考")
        else:
            print(f"❌ 错误！GB：国家标准（强制性）")
    
    def practice_gb_t(self):
        """练习：GB/T ⭐⭐⭐最重点"""
        print(f"\n【标准化】GB/T是什么标准？")
        user_answer = input("你的答案：")
        correct = '国家标准推荐性'
        
        self.total += 1
        if '推荐' in user_answer or 'T' in user_answer:
            self.score += 1
            print(f"✅ 正确！GB/T：国家标准（推荐性）T表示推荐 ⭐重点必考")
        else:
            print(f"❌ 错误！GB/T：国家标准（推荐性）")
    
    def practice_gb_mandatory(self):
        """练习：GB强制 ⭐重点"""
        print(f"\n【标准化】GB标准必须执行吗？")
        user_answer = input("你的答案：")
        correct = '必须'
        
        self.total += 1
        if '必须' in user_answer or '强制' in user_answer:
            self.score += 1
            print(f"✅ 正确！GB强制性标准必须执行")
        else:
            print(f"❌ 错误！GB强制性标准必须执行")
    
    def practice_iec(self):
        """练习：IEC"""
        print(f"\n【标准化】IEC是什么？")
        user_answer = input("你的答案：")
        correct = '国际电工委员会'
        
        self.total += 1
        if '电工' in user_answer or '电气' in user_answer:
            self.score += 1
            print(f"✅ 正确！IEC：国际电工委员会")
        else:
            print(f"❌ 错误！IEC：国际电工委员会")
    
    # ========== 知识产权 ⭐背诵必考 ==========
    
    def practice_copyright_term(self):
        """练习：著作权保护期 ⭐⭐⭐最重点"""
        print(f"\n【知识产权】著作权保护期？")
        user_answer = input("你的答案：")
        correct = '50年'
        
        self.total += 1
        if user_answer == '50' or '50年' in user_answer:
            self.score += 1
            print(f"✅ 正确！著作权保护期50年 ⭐重点必考")
            print("💡 发表后自动保护，无需注册")
        else:
            print(f"❌ 错误！著作权保护期50年")
    
    def practice_copyright_auto(self):
        """练习：著作权自动 ⭐重点"""
        print(f"\n【知识产权】著作权需要注册吗？")
        user_answer = input("你的答案：")
        correct = '不需要'
        
        self.total += 1
        if '不' in user_answer or '自动' in user_answer:
            self.score += 1
            print(f"✅ 正确！著作权发表后自动产生，无需注册")
        else:
            print(f"❌ 错误！著作权发表后自动产生，无需注册")
    
    def practice_invention_patent_term(self):
        """练习：发明专利保护期 ⭐⭐⭐最重点"""
        print(f"\n【知识产权】发明专利保护期？")
        user_answer = input("你的答案：")
        correct = '20年'
        
        self.total += 1
        if user_answer == '20' or '20年' in user_answer:
            self.score += 1
            print(f"✅ 正确！发明专利保护期20年 ⭐重点必考")
        else:
            print(f"❌ 错误！发明专利保护期20年")
    
    def practice_utility_model_term(self):
        """练习：实用新型保护期 ⭐⭐⭐最重点"""
        print(f"\n【知识产权】实用新型专利保护期？")
        user_answer = input("你的答案：")
        correct = '10年'
        
        self.total += 1
        if user_answer == '10' or '10年' in user_answer:
            self.score += 1
            print(f"✅ 正确！实用新型专利保护期10年 ⭐重点必考")
        else:
            print(f"❌ 错误！实用新型专利保护期10年")
    
    def practice_design_patent_term(self):
        """练习：外观设计保护期 ⭐⭐⭐最重点"""
        print(f"\n【知识产权】外观设计专利保护期？")
        user_answer = input("你的答案：")
        correct = '15年'
        
        self.total += 1
        if user_answer == '15' or '15年' in user_answer:
            self.score += 1
            print(f"✅ 正确！外观设计专利保护期15年 ⭐重点必考")
        else:
            print(f"❌ 错误！外观设计专利保护期15年")
    
    def practice_patent_summary(self):
        """练习：专利总结 ⭐⭐⭐最重点"""
        print(f"\n【知识产权】专利保护期总结：发明？实用新型？外观设计？")
        user_answer = input("你的答案（按顺序）：")
        correct = '20年、10年、15年'
        
        self.total += 1
        if '20' in user_answer and '10' in user_answer and '15' in user_answer:
            self.score += 1
            print(f"✅ 正确！发明20年、实用新型10年、外观设计15年 ⭐重点必考")
        else:
            print(f"❌ 错误！发明20年、实用新型10年、外观设计15年")
    
    def practice_trademark_term(self):
        """练习：商标保护期 ⭐重点"""
        print(f"\n【知识产权】商标保护期？")
        user_answer = input("你的答案：")
        correct = '10年，可续展'
        
        self.total += 1
        if '10' in user_answer:
            self.score += 1
            print(f"✅ 正确！商标保护期10年，可续展无限期")
        else:
            print(f"❌ 错误！商标保护期10年，可续展无限期")
    
    def practice_job_invention(self):
        """练习：职务发明 ⭐重点"""
        print(f"\n【知识产权】职务发明归谁？")
        user_answer = input("你的答案：")
        correct = '单位'
        
        self.total += 1
        if '单位' in user_answer or '公司' in user_answer or '企业' in user_answer:
            self.score += 1
            print(f"✅ 正确！职务发明归单位（执行本单位任务完成）")
        else:
            print(f"❌ 错误！职务发明归单位")
    
    # ========== 常用英文术语 ⭐背诵 ==========
    
    def practice_software(self):
        """练习：Software ⭐重点"""
        print(f"\n【术语】Software是什么？")
        user_answer = input("你的答案：")
        correct = '软件'
        
        self.total += 1
        if '软件' in user_answer:
            self.score += 1
            print(f"✅ 正确！Software = 软件 ⭐重点")
        else:
            print(f"❌ 错误！Software = 软件")
    
    def practice_engineering(self):
        """练习：Engineering ⭐重点"""
        print(f"\n【术语】Engineering是什么？")
        user_answer = input("你的答案：")
        correct = '工程'
        
        self.total += 1
        if '工程' in user_answer:
            self.score += 1
            print(f"✅ 正确！Engineering = 工程 ⭐重点")
        else:
            print(f"❌ 错误！Engineering = 工程")
    
    def practice_requirement(self):
        """练习：Requirement ⭐重点"""
        print(f"\n【术语】Requirement是什么？")
        user_answer = input("你的答案：")
        correct = '需求'
        
        self.total += 1
        if '需求' in user_answer:
            self.score += 1
            print(f"✅ 正确！Requirement = 需求 ⭐重点")
        else:
            print(f"❌ 错误！Requirement = 需求")
    
    def practice_design(self):
        """练习：Design ⭐重点"""
        print(f"\n【术语】Design是什么？")
        user_answer = input("你的答案：")
        correct = '设计'
        
        self.total += 1
        if '设计' in user_answer:
            self.score += 1
            print(f"✅ 正确！Design = 设计 ⭐重点")
        else:
            print(f"❌ 错误！Design = 设计")
    
    def practice_testing(self):
        """练习：Testing ⭐重点"""
        print(f"\n【术语】Testing是什么？")
        user_answer = input("你的答案：")
        correct = '测试'
        
        self.total += 1
        if '测试' in user_answer:
            self.score += 1
            print(f"✅ 正确！Testing = 测试 ⭐重点")
        else:
            print(f"❌ 错误！Testing = 测试")
    
    def practice_maintenance(self):
        """练习：Maintenance ⭐重点"""
        print(f"\n【术语】Maintenance是什么？")
        user_answer = input("你的答案：")
        correct = '维护'
        
        self.total += 1
        if '维护' in user_answer:
            self.score += 1
            print(f"✅ 正确！Maintenance = 维护 ⭐重点")
        else:
            print(f"❌ 错误！Maintenance = 维护")
    
    def practice_module(self):
        """练习：Module ⭐重点"""
        print(f"\n【术语】Module是什么？")
        user_answer = input("你的答案：")
        correct = '模块'
        
        self.total += 1
        if '模块' in user_answer:
            self.score += 1
            print(f"✅ 正确！Module = 模块 ⭐重点")
        else:
            print(f"❌ 错误！Module = 模块")
    
    def practice_interface(self):
        """练习：Interface ⭐重点"""
        print(f"\n【术语】Interface是什么？")
        user_answer = input("你的答案：")
        correct = '接口'
        
        self.total += 1
        if '接口' in user_answer:
            self.score += 1
            print(f"✅ 正确！Interface = 接口 ⭐重点")
        else:
            print(f"❌ 错误！Interface = 接口")
    
    def practice_class(self):
        """练习：Class ⭐重点"""
        print(f"\n【术语】Class是什么？")
        user_answer = input("你的答案：")
        correct = '类'
        
        self.total += 1
        if '类' in user_answer:
            self.score += 1
            print(f"✅ 正确！Class = 类 ⭐重点")
        else:
            print(f"❌ 错误！Class = 类")
    
    def practice_object(self):
        """练习：Object ⭐重点"""
        print(f"\n【术语】Object是什么？")
        user_answer = input("你的答案：")
        correct = '对象'
        
        self.total += 1
        if '对象' in user_answer:
            self.score += 1
            print(f"✅ 正确！Object = 对象 ⭐重点")
        else:
            print(f"❌ 错误！Object = 对象")
    
    def practice_algorithm(self):
        """练习：Algorithm ⭐重点"""
        print(f"\n【术语】Algorithm是什么？")
        user_answer = input("你的答案：")
        correct = '算法'
        
        self.total += 1
        if '算法' in user_answer:
            self.score += 1
            print(f"✅ 正确！Algorithm = 算法")
        else:
            print(f"❌ 错误！Algorithm = 算法")
    
    def practice_database(self):
        """练习：Database ⭐重点"""
        print(f"\n【术语】Database是什么？")
        user_answer = input("你的答案：")
        correct = '数据库'
        
        self.total += 1
        if '数据库' in user_answer:
            self.score += 1
            print(f"✅ 正确！Database = 数据库")
        else:
            print(f"❌ 错误！Database = 数据库")
    
    def practice_terms_quiz(self):
        """练习：术语快速测试 ⭐重点"""
        terms = [
            ('Software', '软件'),
            ('Requirement', '需求'),
            ('Testing', '测试'),
            ('Interface', '接口'),
            ('Class', '类'),
            ('Object', '对象'),
        ]
        
        for eng, chn in random.sample(terms, 4):
            print(f"\n【术语】{eng}是什么？")
            user_answer = input("你的答案：")
            
            self.total += 1
            if chn in user_answer:
                self.score += 1
                print(f"✅ 正确！{eng} = {chn}")
            else:
                print(f"❌ 错误！{eng} = {chn}")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*50}")
        print(f"📊 复习完成！得分：{self.score}/{self.total}")
        if self.score == self.total:
            print("🎉 全对！标准化/知识产权/术语记忆牢固！")
        elif self.score >= self.total * 0.8:
            print("👍 不错！考前再背一遍重点！")
        else:
            print("💪 还需努力！重点背诵：")
            print("   GB强制性、GB/T推荐性")
            print("   发明20年、实用新型10年、外观设计15年")
            print("   Software=软件、Testing=测试、Interface=接口")
    
    def run(self):
        """运行练习"""
        print("="*50)
        print("标准化/知识产权/术语复习 ⭐考前记忆")
        print("="*50)
        print("\n复习重点：")
        print("1. 标准化（GB强制/GB/T推荐）⭐重点")
        print("2. 知识产权（专利保护期）⭐⭐⭐最重点")
        print("3. 英文术语（Software/Testing等）⭐重点")
        print("4. 综合测试")
        print("0. 退出")
        
        while True:
            choice = input("\n选择复习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                practices = [
                    self.practice_gb,
                    self.practice_gb_t,
                    self.practice_gb_mandatory,
                ]
                for p in practices:
                    p()
            elif choice == '2':
                practices = [
                    self.practice_copyright_term,
                    self.practice_copyright_auto,
                    self.practice_invention_patent_term,
                    self.practice_utility_model_term,
                    self.practice_design_patent_term,
                    self.practice_patent_summary,
                ]
                for p in practices:
                    p()
            elif choice == '3':
                practices = [
                    self.practice_software,
                    self.practice_requirement,
                    self.practice_testing,
                    self.practice_interface,
                    self.practice_class,
                    self.practice_object,
                ]
                for p in practices:
                    p()
            elif choice == '4':
                practices = [
                    self.practice_gb_t,
                    self.practice_invention_patent_term,
                    self.practice_utility_model_term,
                    self.practice_design_patent_term,
                    self.practice_terms_quiz,
                ]
                for p in practices:
                    p()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    review = 标准化知识产权术语复习()
    review.run()