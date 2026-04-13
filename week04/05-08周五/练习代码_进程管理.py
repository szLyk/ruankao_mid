#!/usr/bin/env python3
"""
进程管理练习脚本
用于练习进程状态、PV操作
"""

import random

class 进程管理练习:
    """进程管理练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_running(self):
        """练习：运行态"""
        print(f"\n【题目】运行态的含义？")
        user_answer = input("你的答案：")
        correct = '占用CPU执行'
        
        self.total += 1
        if 'CPU' in user_answer or '执行' in user_answer:
            self.score += 1
            print(f"✅ 正确！运行态：占用CPU执行")
        else:
            print(f"❌ 错误！运行态：占用CPU执行")
    
    def practice_ready(self):
        """练习：就绪态"""
        print(f"\n【题目】就绪态的含义？")
        user_answer = input("你的答案：")
        correct = '等待CPU分配'
        
        self.total += 1
        if '等待' in user_answer and 'CPU' in user_answer:
            self.score += 1
            print(f"✅ 正确！就绪态：等待CPU分配")
        else:
            print(f"❌ 错误！就绪态：等待CPU分配")
    
    def practice_blocked(self):
        """练习：阻塞态"""
        print(f"\n【题目】阻塞态的含义？")
        user_answer = input("你的答案：")
        correct = '等待I/O或其他事件'
        
        self.total += 1
        if '等待' in user_answer and 'I/O' in user_answer or '事件' in user_answer:
            self.score += 1
            print(f"✅ 正确！阻塞态：等待I/O或其他事件")
        else:
            print(f"❌ 错误！阻塞态：等待I/O或其他事件")
    
    def practice_ready_to_running(self):
        """练习：就绪→运行"""
        print(f"\n【题目】就绪态→运行态的条件？")
        user_answer = input("你的答案：")
        correct = '被调度选中'
        
        self.total += 1
        if '调度' in user_answer or '选中' in user_answer:
            self.score += 1
            print(f"✅ 正确！就绪→运行：被调度选中")
        else:
            print(f"❌ 错误！就绪→运行：被调度选中")
    
    def practice_running_to_ready(self):
        """练习：运行→就绪"""
        print(f"\n【题目】运行态→就绪态的条件？")
        user_answer = input("你的答案：")
        correct = '时间片用完'
        
        self.total += 1
        if '时间片' in user_answer:
            self.score += 1
            print(f"✅ 正确！运行→就绪：时间片用完")
        else:
            print(f"❌ 错误！运行→就绪：时间片用完")
    
    def practice_running_to_blocked(self):
        """练习：运行→阻塞"""
        print(f"\n【题目】运行态→阻塞态的条件？")
        user_answer = input("你的答案：")
        correct = '等待资源'
        
        self.total += 1
        if '等待' in user_answer and '资源' in user_answer:
            self.score += 1
            print(f"✅ 正确！运行→阻塞：等待资源（I/O等）")
        else:
            print(f"❌ 错误！运行→阻塞：等待资源（I/O等）")
    
    def practice_blocked_to_ready(self):
        """练习：阻塞→就绪"""
        print(f"\n【题目】阻塞态→就绪态的条件？")
        user_answer = input("你的答案：")
        correct = '资源就绪'
        
        self.total += 1
        if '就绪' in user_answer or '资源' in user_answer:
            self.score += 1
            print(f"✅ 正确！阻塞→就绪：资源就绪")
        else:
            print(f"❌ 错误！阻塞→就绪：资源就绪")
    
    def practice_p_operation(self):
        """练习：P操作 ⭐重点"""
        print(f"\n【题目】P操作的含义？")
        user_answer = input("你的答案：")
        correct = '申请资源，S = S - 1'
        
        self.total += 1
        if '申请' in user_answer or 'S-1' in user_answer.replace(' ', ''):
            self.score += 1
            print(f"✅ 正确！P操作：申请资源，S = S - 1")
        else:
            print(f"❌ 错误！P操作：申请资源，S = S - 1")
    
    def practice_v_operation(self):
        """练习：V操作 ⭐重点"""
        print(f"\n【题目】V操作的含义？")
        user_answer = input("你的答案：")
        correct = '释放资源，S = S + 1'
        
        self.total += 1
        if '释放' in user_answer or 'S+1' in user_answer.replace(' ', ''):
            self.score += 1
            print(f"✅ 正确！V操作：释放资源，S = S + 1")
        else:
            print(f"❌ 错误！V操作：释放资源，S = S + 1")
    
    def practice_mutex_s(self):
        """练习：互斥信号量初值 ⭐重点"""
        print(f"\n【题目】互斥信号量S的初值是？")
        user_answer = input("你的答案：")
        correct = '1'
        
        self.total += 1
        if user_answer == '1':
            self.score += 1
            print(f"✅ 正确！互斥信号量初值S = 1")
            print(f"   表示一次只能一个进程访问")
        else:
            print(f"❌ 错误！互斥信号量初值S = 1")
    
    def practice_sync_s(self):
        """练习：同步信号量初值 ⭐重点"""
        print(f"\n【题目】同步信号量S的初值是？")
        user_answer = input("你的答案：")
        correct = '0或N'
        
        self.total += 1
        if user_answer == '0' or 'N' in user_answer:
            self.score += 1
            print(f"✅ 正确！同步信号量初值S = 0 或 N")
            print(f"   S=0：前驱未完成时等待")
            print(f"   S=N：初始有N个资源")
        else:
            print(f"❌ 错误！同步信号量初值S = 0 或 N")
    
    def practice_mutex_vs_sync(self):
        """练习：互斥vs同步 ⭐重点"""
        print(f"\n【题目】互斥和同步的区别？")
        print("请选择：")
        print("A. 互斥：一次只能一个进程访问（S=1）")
        print("B. 同步：前驱完成通知后继（S=0或N）")
        print("C. 以上都是")
        user_answer = input("你的答案（A/B/C）：")
        correct = 'C'
        
        self.total += 1
        if user_answer.upper() == correct:
            self.score += 1
            print(f"✅ 正确！")
            print(f"   互斥：一次只能一个访问（S=1）")
            print(f"   同步：前驱通知后继（S=0或N）")
        else:
            print(f"❌ 错误！")
            print(f"   互斥：一次只能一个访问（S=1）")
            print(f"   同步：前驱通知后继（S=0或N）")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("进程管理 + PV操作练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 运行态")
        print("2. 就绪态")
        print("3. 阻塞态")
        print("4. 就绪→运行")
        print("5. 运行→就绪")
        print("6. 运行→阻塞")
        print("7. 阻塞→就绪")
        print("8. P操作 ⭐重点")
        print("9. V操作 ⭐重点")
        print("10. 互斥信号量初值 ⭐重点")
        print("11. 同步信号量初值 ⭐重点")
        print("12. 互斥vs同步 ⭐重点")
        print("13. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_running()
            elif choice == '2':
                self.practice_ready()
            elif choice == '3':
                self.practice_blocked()
            elif choice == '4':
                self.practice_ready_to_running()
            elif choice == '5':
                self.practice_running_to_ready()
            elif choice == '6':
                self.practice_running_to_blocked()
            elif choice == '7':
                self.practice_blocked_to_ready()
            elif choice == '8':
                self.practice_p_operation()
            elif choice == '9':
                self.practice_v_operation()
            elif choice == '10':
                self.practice_mutex_s()
            elif choice == '11':
                self.practice_sync_s()
            elif choice == '12':
                self.practice_mutex_vs_sync()
            elif choice == '13':
                types = [
                    self.practice_p_operation,
                    self.practice_v_operation,
                    self.practice_mutex_s,
                    self.practice_mutex_vs_sync,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 进程管理练习()
    practice.run()