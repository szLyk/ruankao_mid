#!/usr/bin/env python3
"""
全真模拟考试练习脚本
涵盖上午题+下午题高频考点 ⭐模拟实战
"""

import random
import time

class 全真模拟考试:
    """全真模拟考试练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
        self.morning_score = 0
        self.morning_total = 0
        self.afternoon_score = 0
        self.afternoon_total = 0
    
    # ========== 上午题模拟 ⭐高频考点 ==========
    
    def morning_binary_tree(self):
        """上午题：二叉树性质 ⭐重点"""
        print(f"\n【上午题】二叉树叶子节点与度为2节点关系？")
        user_answer = input("你的答案：")
        correct = 'n2 + 1'
        
        self.morning_total += 1
        if 'n2' in user_answer and '1' in user_answer:
            self.morning_score += 1
            print(f"✅ 正确！n0 = n2 + 1")
        else:
            print(f"❌ 错误！n0 = n2 + 1")
    
    def morning_stable_sort(self):
        """上午题：稳定排序 ⭐重点"""
        print(f"\n【上午题】稳定排序有哪些？（说出一个）")
        user_answer = input("你的答案：")
        correct = ['冒泡', '插入', '归并', '基数']
        
        self.morning_total += 1
        if any(c in user_answer for c in correct):
            self.morning_score += 1
            print(f"✅ 正确！稳定排序：冒泡、插入、归并、基数")
        else:
            print(f"❌ 错误！稳定排序：冒泡、插入、归并、基数")
    
    def morning_unstable_sort(self):
        """上午题：不稳定排序 ⭐重点"""
        print(f"\n【上午题】不稳定排序有哪些？（说出一个）")
        user_answer = input("你的答案：")
        correct = ['快速', '选择', '堆']
        
        self.morning_total += 1
        if any(c in user_answer for c in correct):
            self.morning_score += 1
            print(f"✅ 正确！不稳定排序：快速、选择、堆")
        else:
            print(f"❌ 错误！不稳定排序：快速、选择、堆")
    
    def morning_stack_queue(self):
        """上午题：栈队列 ⭐重点"""
        print(f"\n【上午题】栈和队列的区别？")
        user_answer = input("你的答案：")
        correct = '栈LIFO队列FIFO'
        
        self.morning_total += 1
        if 'LIFO' in user_answer.upper() or 'FIFO' in user_answer.upper() or ('后进' in user_answer or '先进' in user_answer):
            self.morning_score += 1
            print(f"✅ 正确！栈LIFO后进先出，队列FIFO先进先出")
        else:
            print(f"❌ 错误！栈LIFO，队列FIFO")
    
    def morning_binary_search(self):
        """上午题：二分查找 ⭐重点"""
        print(f"\n【上午题】二分查找时间复杂度？")
        user_answer = input("你的答案：")
        correct = 'O(log n)'
        
        self.morning_total += 1
        if 'log' in user_answer.lower():
            self.morning_score += 1
            print(f"✅ 正确！二分查找O(log n)")
        else:
            print(f"❌ 错误！二分查找O(log n)")
    
    def morning_dfs_bfs(self):
        """上午题：DFS/BFS ⭐重点"""
        print(f"\n【上午题】DFS用什么数据结构？")
        user_answer = input("你的答案：")
        correct = '栈'
        
        self.morning_total += 1
        if '栈' in user_answer:
            self.morning_score += 1
            print(f"✅ 正确！DFS用栈")
        else:
            print(f"❌ 错误！DFS用栈")
    
    def morning_spiral_model(self):
        """上午题：螺旋模型 ⭐重点"""
        print(f"\n【上午题】螺旋模型特点？")
        user_answer = input("你的答案：")
        correct = '风险分析'
        
        self.morning_total += 1
        if '风险' in user_answer or '迭代' in user_answer:
            self.morning_score += 1
            print(f"✅ 正确！螺旋模型：迭代+风险分析")
        else:
            print(f"❌ 错误！螺旋模型：迭代+风险分析")
    
    def morning_path_coverage(self):
        """上午题：路径覆盖 ⭐重点"""
        print(f"\n【上午题】白盒测试最强覆盖？")
        user_answer = input("你的答案：")
        correct = '路径覆盖'
        
        self.morning_total += 1
        if '路径' in user_answer:
            self.morning_score += 1
            print(f"✅ 正确！路径覆盖是白盒最强覆盖")
        else:
            print(f"❌ 错误！路径覆盖是白盒最强覆盖")
    
    def morning_iso_9126(self):
        """上午题：ISO 9126 ⭐重点"""
        print(f"\n【上午题】ISO 9126六大特性？（说出两个）")
        user_answer = input("你的答案：")
        correct = ['功能', '可靠', '易用', '效率', '维护', '移植']
        
        self.morning_total += 1
        if any(c in user_answer for c in correct):
            self.morning_score += 1
            print(f"✅ 正确！六大特性：功能性、可靠性、易用性、效率性、可维护性、可移植性")
        else:
            print(f"❌ 错误！六大特性：功能性、可靠性、易用性、效率性、可维护性、可移植性")
    
    def morning_overload_vs_override(self):
        """上午题：重载vs重写 ⭐重点"""
        print(f"\n【上午题】重载和重写区别？")
        user_answer = input("你的答案：")
        correct = '参数'
        
        self.morning_total += 1
        if '参数' in user_answer:
            self.morning_score += 1
            print(f"✅ 正确！重载参数不同，重写参数相同")
        else:
            print(f"❌ 错误！重载参数不同，重写参数相同")
    
    def morning_aggregation_vs_composition(self):
        """上午题：聚合vs组合 ⭐重点"""
        print(f"\n【上午题】聚合和组合区别？")
        user_answer = input("你的答案：")
        correct = '独立'
        
        self.morning_total += 1
        if '独立' in user_answer or '空心' in user_answer or '实心' in user_answer:
            self.morning_score += 1
            print(f"✅ 正确！聚合空心可独立，组合实心不可独立")
        else:
            print(f"❌ 错误！聚合空心可独立，组合实心不可独立")
    
    def morning_3nf(self):
        """上午题：3NF ⭐重点"""
        print(f"\n【上午题】第三范式要求？")
        user_answer = input("你的答案：")
        correct = '传递依赖'
        
        self.morning_total += 1
        if '传递' in user_answer:
            self.morning_score += 1
            print(f"✅ 正确！3NF消除传递依赖")
        else:
            print(f"❌ 错误！3NF消除传递依赖")
    
    def morning_mn_convert(self):
        """上午题：M:N转换 ⭐重点"""
        print(f"\n【上午题】M:N联系如何转换？")
        user_answer = input("你的答案：")
        correct = '单独建表'
        
        self.morning_total += 1
        if '单独' in user_answer or '建表' in user_answer:
            self.morning_score += 1
            print(f"✅ 正确！M:N单独建表，含双方主码")
        else:
            print(f"❌ 错误！M:N单独建表")
    
    def morning_process_states(self):
        """上午题：进程状态 ⭐重点"""
        print(f"\n【上午题】运行→就绪的原因？")
        user_answer = input("你的答案：")
        correct = '时间片'
        
        self.morning_total += 1
        if '时间片' in user_answer or '时间' in user_answer:
            self.morning_score += 1
            print(f"✅ 正确！运行→就绪：时间片用完")
        else:
            print(f"❌ 错误！运行→就绪：时间片用完")
    
    def morning_pv_operation(self):
        """上午题：PV操作 ⭐重点"""
        print(f"\n【上午题】P操作含义？")
        user_answer = input("你的答案：")
        correct = '申请资源'
        
        self.morning_total += 1
        if '申请' in user_answer or '减' in user_answer:
            self.morning_score += 1
            print(f"✅ 正确！P操作：S=S-1，申请资源")
        else:
            print(f"❌ 错误！P操作：S=S-1，申请资源")
    
    def morning_mutex_init(self):
        """上午题：互斥初值 ⭐重点"""
        print(f"\n【上午题】互斥信号量初值？")
        user_answer = input("你的答案：")
        correct = '1'
        
        self.morning_total += 1
        if user_answer == '1':
            self.morning_score += 1
            print(f"✅ 正确！互斥初值=1")
        else:
            print(f"❌ 错误！互斥初值=1")
    
    def morning_tcp_udp(self):
        """上午题：TCP vs UDP ⭐重点"""
        print(f"\n【上午题】TCP和UDP区别？")
        user_answer = input("你的答案：")
        correct = '可靠'
        
        self.morning_total += 1
        if '可靠' in user_answer:
            self.morning_score += 1
            print(f"✅ 正确！TCP面向连接可靠慢，UDP无连接不可靠快")
        else:
            print(f"❌ 错误！TCP可靠慢，UDP不可靠快")
    
    def morning_dns_port(self):
        """上午题：DNS端口 ⭐重点"""
        print(f"\n【上午题】DNS协议端口？")
        user_answer = input("你的答案：")
        correct = '53'
        
        self.morning_total += 1
        if user_answer == '53':
            self.morning_score += 1
            print(f"✅ 正确！DNS端口53")
        else:
            print(f"❌ 错误！DNS端口53")
    
    def morning_encryption(self):
        """上午题：加密算法 ⭐重点"""
        print(f"\n【上午题】对称加密算法？（说出一个）")
        user_answer = input("你的答案：")
        correct = ['DES', 'AES']
        
        self.morning_total += 1
        if 'DES' in user_answer.upper() or 'AES' in user_answer.upper():
            self.morning_score += 1
            print(f"✅ 正确！对称加密：DES、AES")
        else:
            print(f"❌ 错误！对称加密：DES、AES")
    
    def morning_complement(self):
        """上午题：补码 ⭐重点"""
        print(f"\n【上午题】补码11111111表示？")
        user_answer = input("你的答案：")
        correct = '-1'
        
        self.morning_total += 1
        if user_answer == '-1':
            self.morning_score += 1
            print(f"✅ 正确！补码11111111=-1")
        else:
            print(f"❌ 错误！补码11111111=-1")
    
    def morning_patent_term(self):
        """上午题：专利保护期 ⭐重点"""
        print(f"\n【上午题】发明专利保护期？")
        user_answer = input("你的答案：")
        correct = '20'
        
        self.morning_total += 1
        if user_answer == '20':
            self.morning_score += 1
            print(f"✅ 正确！发明专利20年")
        else:
            print(f"❌ 错误！发明专利20年")
    
    # ========== 下午题模拟 ⭐重点必考 ==========
    
    def afternoon_dfd(self):
        """下午题：DFD图 ⭐重点"""
        print(f"\n【下午题1】DFD外部实体用什么图形？")
        user_answer = input("你的答案：")
        correct = '方框'
        
        self.afternoon_total += 1
        if '方框' in user_answer or '矩形' in user_answer:
            self.afternoon_score += 1
            print(f"✅ 正确！外部实体用方框")
            print("💡 技巧：找人/系统/部门")
        else:
            print(f"❌ 错误！外部实体用方框")
    
    def afternoon_er_mn(self):
        """下午题：ER图M:N ⭐重点"""
        print(f"\n【下午题2】M:N联系如何转换关系模式？")
        user_answer = input("你的答案：")
        correct = '单独建表'
        
        self.afternoon_total += 1
        if '单独' in user_answer or '建表' in user_answer:
            self.afternoon_score += 1
            print(f"✅ 正确！M:N单独建表，含双方主码")
            print("💡 例：选课（学号，课程号，成绩）")
        else:
            print(f"❌ 错误！M:N单独建表")
    
    def afternoon_uml_relation(self):
        """下午题：UML关系 ⭐重点"""
        print(f"\n【下午题3】公司-员工是什么关系？")
        user_answer = input("你的答案：")
        correct = '聚合'
        
        self.afternoon_total += 1
        if '聚合' in user_answer:
            self.afternoon_score += 1
            print(f"✅ 正确！公司-员工是聚合关系（员工可独立）")
        else:
            print(f"❌ 错误！公司-员工是聚合关系")
    
    def afternoon_uml_find_attribute(self):
        """下午题：找属性 ⭐重点"""
        print(f"\n【下午题3】类图属性从哪里找？")
        user_answer = input("你的答案：")
        correct = '名词'
        
        self.afternoon_total += 1
        if '名词' in user_answer:
            self.afternoon_score += 1
            print(f"✅ 正确！属性从题目描述找名词")
        else:
            print(f"❌ 错误！属性从题目描述找名词")
    
    def afternoon_java_extends(self):
        """下午题：Java继承 ⭐重点"""
        print(f"\n【下午题5】Java继承用什么关键字？")
        user_answer = input("你的答案：")
        correct = 'extends'
        
        self.afternoon_total += 1
        if 'extends' in user_answer.lower():
            self.afternoon_score += 1
            print(f"✅ 正确！Java继承用extends")
        else:
            print(f"❌ 错误！Java继承用extends")
    
    def afternoon_java_list(self):
        """下午题：Java List ⭐重点"""
        print(f"\n【下午题5】List添加元素用什么方法？")
        user_answer = input("你的答案：")
        correct = 'add'
        
        self.afternoon_total += 1
        if 'add' in user_answer.lower():
            self.afternoon_score += 1
            print(f"✅ 正确！List.add()添加元素")
        else:
            print(f"❌ 错误！List.add()添加元素")
    
    def afternoon_java_map(self):
        """下午题：Java Map ⭐重点"""
        print(f"\n【下午题5】Map添加键值对用什么方法？")
        user_answer = input("你的答案：")
        correct = 'put'
        
        self.afternoon_total += 1
        if 'put' in user_answer.lower():
            self.afternoon_score += 1
            print(f"✅ 正确！Map.put()添加键值对")
        else:
            print(f"❌ 错误！Map.put()添加键值对")
    
    # ========== 模拟考试运行 ==========
    
    def run_morning_exam(self):
        """运行上午题模拟"""
        print("="*50)
        print("上午题模拟考试 ⭐高频考点")
        print("="*50)
        print("建议时间：30分钟（模拟版）")
        print("正式考试：150分钟")
        print("="*50)
        
        self.morning_score = 0
        self.morning_total = 0
        
        questions = [
            self.morning_binary_tree,
            self.morning_stable_sort,
            self.morning_unstable_sort,
            self.morning_stack_queue,
            self.morning_binary_search,
            self.morning_dfs_bfs,
            self.morning_spiral_model,
            self.morning_path_coverage,
            self.morning_iso_9126,
            self.morning_overload_vs_override,
            self.morning_aggregation_vs_composition,
            self.morning_3nf,
            self.morning_mn_convert,
            self.morning_process_states,
            self.morning_pv_operation,
            self.morning_mutex_init,
            self.morning_tcp_udp,
            self.morning_dns_port,
            self.morning_encryption,
            self.morning_complement,
            self.morning_patent_term,
        ]
        
        for q in questions:
            q()
        
        print(f"\n{'='*50}")
        print(f"📊 上午题模拟得分：{self.morning_score}/{self.morning_total}")
        if self.morning_score >= 15:
            print("✅ 及格线以上！继续保持！")
        else:
            print("⚠️ 需要加强复习！重点巩固薄弱点")
    
    def run_afternoon_exam(self):
        """运行下午题模拟"""
        print("="*50)
        print("下午题模拟考试 ⭐重点必做")
        print("="*50)
        print("建议时间：20分钟（模拟版）")
        print("正式考试：150分钟")
        print("="*50)
        
        self.afternoon_score = 0
        self.afternoon_total = 0
        
        print("\n【第1题】DFD图")
        self.afternoon_dfd()
        
        print("\n【第2题】ER图")
        self.afternoon_er_mn()
        
        print("\n【第3题】UML图 ⭐重点")
        self.afternoon_uml_relation()
        self.afternoon_uml_find_attribute()
        
        print("\n【第5题】Java程序设计 ⭐重点")
        self.afternoon_java_extends()
        self.afternoon_java_list()
        self.afternoon_java_map()
        
        print(f"\n{'='*50}")
        print(f"📊 下午题模拟得分：{self.afternoon_score}/{self.afternoon_total}")
        if self.afternoon_score >= 5:
            print("✅ 及格线以上！继续练习！")
        else:
            print("⚠️ 需要加强复习！重点练习DFD、ER、UML、Java")
    
    def run_full_exam(self):
        """运行全真模拟"""
        print("\n" + "="*50)
        print("🎯 全真模拟考试开始")
        print("="*50)
        
        start_time = time.time()
        
        # 上午题
        self.run_morning_exam()
        
        # 下午题
        print("\n" + "="*50)
        input("按Enter继续下午题模拟...")
        self.run_afternoon_exam()
        
        end_time = time.time()
        duration = int((end_time - start_time) / 60)
        
        # 总分
        total_score = self.morning_score + self.afternoon_score
        total_questions = self.morning_total + self.afternoon_total
        
        print("\n" + "="*50)
        print("📊 全真模拟考试结果")
        print("="*50)
        print(f"上午题：{self.morning_score}/{self.morning_total}")
        print(f"下午题：{self.afternoon_score}/{self.afternoon_total}")
        print(f"总分：{total_score}/{total_questions}")
        print(f"用时：{duration}分钟")
        
        if total_score >= 20:
            print("\n✅ 优秀！模拟及格，考试有望通过！")
        elif total_score >= 15:
            print("\n👍 良好！接近及格，继续巩固！")
        else:
            print("\n⚠️ 需要加强复习！重点巩固高频考点")
            print("重点背诵：")
            print("  - n0=n2+1、稳定排序")
            print("  - 路径覆盖、重载vs重写")
            print("  - M:N单独建表、PV操作")
            print("  - DNS端口53、补码-1")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*50}")
        print(f"📊 模拟考试得分")
        print(f"上午题：{self.morning_score}/{self.morning_total}")
        print(f"下午题：{self.afternoon_score}/{self.afternoon_total}")
    
    def run(self):
        """运行练习"""
        print("="*50)
        print("全真模拟考试练习 ⭐模拟实战")
        print("="*50)
        print("\n练习模式：")
        print("1. 上午题模拟（高频考点）")
        print("2. 下午题模拟（DFD/ER/UML/Java）")
        print("3. 全真模拟（上午+下午）")
        print("4. 重点公式速记")
        print("0. 退出")
        
        while True:
            choice = input("\n选择模式（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.run_morning_exam()
            elif choice == '2':
                self.run_afternoon_exam()
            elif choice == '3':
                self.run_full_exam()
            elif choice == '4':
                print("\n" + "="*50)
                print("⭐ 考前必背公式")
                print("="*50)
                print("二叉树：n0 = n2 + 1")
                print("稳定排序：冒泡、插入、归并、基数")
                print("不稳定排序：快速、选择、堆")
                print("白盒最强：路径覆盖")
                print("重载vs重写：参数不同vs参数相同")
                print("聚合vs组合：空心可独立vs实心不可独立")
                print("3NF：消除传递依赖")
                print("M:N：单独建表")
                print("运行→就绪：时间片用完")
                print("P操作：S=S-1申请")
                print("V操作：S=S+1释放")
                print("互斥初值：1")
                print("DNS端口：53")
                print("TCP：可靠慢")
                print("UDP：不可靠快")
                print("对称加密：DES、AES")
                print("非对称加密：RSA")
                print("补码-1：11111111")
                print("发明专利：20年")
                print("著作权：50年")
                print("="*50)
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    exam = 全真模拟考试()
    exam.run()