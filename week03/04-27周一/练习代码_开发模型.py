#!/usr/bin/env python3
"""
软件开发模型练习脚本
用于练习瀑布、增量、螺旋、敏捷等开发模型
"""

import random

class 开发模型练习:
    """软件开发模型练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
        
        # 开发模型特点
        self.models = {
            '瀑布模型': {'特点': '线性顺序、文档驱动', '适用': '需求明确的项目'},
            '增量模型': {'特点': '分批交付、逐步完善', '适用': '大型项目分模块'},
            '螺旋模型': {'特点': '风险驱动、迭代开发', '适用': '高风险大型项目'},
            '喷泉模型': {'特点': '面向对象、无缝迭代', '适用': 'OO软件开发'},
            '敏捷开发': {'特点': '快速迭代、用户参与', '适用': '需求变化快的项目'},
            'V模型': {'特点': '测试与开发对应', '适用': '测试重要的项目'},
        }
    
    def practice_waterfall(self):
        """练习：瀑布模型"""
        print(f"\n【题目】瀑布模型的特点是什么？")
        user_answer = input("你的答案：")
        correct = '线性顺序、文档驱动'
        
        self.total += 1
        if '线性' in user_answer or '文档' in user_answer:
            self.score += 1
            print(f"✅ 正确！瀑布模型：线性顺序、文档驱动")
            print(f"   适用场景：需求明确的项目")
        else:
            print(f"❌ 错误！瀑布模型：线性顺序、文档驱动")
            print(f"   适用场景：需求明确的项目")
    
    def practice_waterfall_application(self):
        """练习：瀑布模型适用场景 ⭐重点"""
        print(f"\n【题目】瀑布模型适用于什么项目？")
        user_answer = input("你的答案：")
        correct = '需求明确的项目'
        
        self.total += 1
        if '需求明确' in user_answer or '明确' in user_answer:
            self.score += 1
            print(f"✅ 正确！瀑布模型适用于需求明确的项目")
        else:
            print(f"❌ 错误！瀑布模型适用于需求明确的项目")
    
    def practice_spiral(self):
        """练习：螺旋模型 ⭐重点"""
        print(f"\n【题目】螺旋模型的特点是什么？")
        user_answer = input("你的答案：")
        correct = '风险驱动'
        
        self.total += 1
        if '风险' in user_answer:
            self.score += 1
            print(f"✅ 正确！螺旋模型：风险驱动")
            print(f"   适用场景：高风险大型项目")
        else:
            print(f"❌ 错误！螺旋模型：风险驱动")
            print(f"   适用场景：高风险大型项目")
    
    def practice_spiral_application(self):
        """练习：螺旋模型适用场景"""
        print(f"\n【题目】螺旋模型适用于什么项目？")
        user_answer = input("你的答案：")
        correct = '高风险大型项目'
        
        self.total += 1
        if '高风险' in user_answer or '风险' in user_answer:
            self.score += 1
            print(f"✅ 正确！螺旋模型适用于高风险大型项目")
        else:
            print(f"❌ 错误！螺旋模型适用于高风险大型项目")
    
    def practice_agile(self):
        """练习：敏捷开发"""
        print(f"\n【题目】敏捷开发的特点是什么？")
        user_answer = input("你的答案：")
        correct = '快速迭代、用户参与'
        
        self.total += 1
        if '快速' in user_answer or '迭代' in user_answer or '敏捷' in user_answer:
            self.score += 1
            print(f"✅ 正确！敏捷开发：快速迭代、用户参与")
            print(f"   适用场景：需求变化快的项目")
        else:
            print(f"❌ 错误！敏捷开发：快速迭代、用户参与")
    
    def practice_agile_application(self):
        """练习：敏捷开发适用场景"""
        print(f"\n【题目】敏捷开发适用于什么项目？")
        user_answer = input("你的答案：")
        correct = '需求变化快的项目'
        
        self.total += 1
        if '变化' in user_answer or '快' in user_answer:
            self.score += 1
            print(f"✅ 正确！敏捷开发适用于需求变化快的项目")
        else:
            print(f"❌ 错误！敏捷开发适用于需求变化快的项目")
    
    def practice_v_model(self):
        """练习：V模型"""
        print(f"\n【题目】V模型的特点是什么？")
        user_answer = input("你的答案：")
        correct = '测试与开发对应'
        
        self.total += 1
        if '测试' in user_answer and '对应' in user_answer:
            self.score += 1
            print(f"✅ 正确！V模型：测试与开发对应")
        else:
            print(f"❌ 错误！V模型：测试与开发对应")
            print(f"   每个开发阶段都有对应的测试阶段")
    
    def practice_model_comparison(self):
        """练习：模型对比 ⭐重点"""
        questions = [
            ('需求明确用什么模型？', '瀑布模型'),
            ('高风险用什么模型？', '螺旋模型'),
            ('需求变化快用什么模型？', '敏捷开发'),
            ('测试重要用什么模型？', 'V模型'),
            ('面向对象用什么模型？', '喷泉模型'),
            ('大型项目分模块用什么模型？', '增量模型'),
        ]
        
        question, correct = random.choice(questions)
        
        print(f"\n【题目】{question}")
        user_answer = input("你的答案：")
        
        self.total += 1
        if user_answer.strip() in correct:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
    
    def practice_all_models(self):
        """练习：所有模型特点"""
        models_list = list(self.models.keys())
        model = random.choice(models_list)
        
        print(f"\n【题目】{model}的特点是？")
        user_answer = input("你的答案：")
        correct = self.models[model]['特点']
        
        self.total += 1
        if user_answer.strip() in correct:
            self.score += 1
            print(f"✅ 正确！{model}：{correct}")
        else:
            print(f"❌ 错误！{model}：{correct}")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("软件开发模型练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 瀑布模型特点")
        print("2. 瀑布模型适用场景 ⭐重点")
        print("3. 螺旋模型特点 ⭐重点")
        print("4. 螺旋模型适用场景")
        print("5. 敏捷开发特点")
        print("6. 敏捷开发适用场景")
        print("7. V模型特点")
        print("8. 模型对比 ⭐重点")
        print("9. 所有模型特点")
        print("10. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_waterfall()
            elif choice == '2':
                self.practice_waterfall_application()
            elif choice == '3':
                self.practice_spiral()
            elif choice == '4':
                self.practice_spiral_application()
            elif choice == '5':
                self.practice_agile()
            elif choice == '6':
                self.practice_agile_application()
            elif choice == '7':
                self.practice_v_model()
            elif choice == '8':
                self.practice_model_comparison()
            elif choice == '9':
                self.practice_all_models()
            elif choice == '10':
                types = [
                    self.practice_model_comparison,
                    self.practice_spiral,
                    self.practice_waterfall_application,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 开发模型练习()
    practice.run()