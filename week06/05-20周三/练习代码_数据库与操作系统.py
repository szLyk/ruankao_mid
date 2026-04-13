#!/usr/bin/env python3
"""
数据库+操作系统错题复习练习脚本
涵盖：范式、ER转换、SQL、进程状态、PV操作、分页 ⭐复习重点
"""

import random

class 数据库与操作系统复习:
    """数据库+操作系统复习练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    # ========== 数据库范式 ⭐重点必考 ==========
    
    def practice_1nf(self):
        """练习：1NF"""
        print(f"\n【范式】第一范式要求？")
        user_answer = input("你的答案：")
        correct = '原子性'
        
        self.total += 1
        if '原子' in user_answer or '不可分割' in user_answer:
            self.score += 1
            print(f"✅ 正确！1NF：属性不可分割（原子性）")
        else:
            print(f"❌ 错误！1NF：属性不可分割（原子性）")
    
    def practice_2nf(self):
        """练习：2NF ⭐重点"""
        print(f"\n【范式】第二范式要求？")
        user_answer = input("你的答案：")
        correct = '消除部分依赖'
        
        self.total += 1
        if '部分' in user_answer or '依赖' in user_answer:
            self.score += 1
            print(f"✅ 正确！2NF：消除非主属性对候选码的部分依赖")
        else:
            print(f"❌ 错误！2NF：消除非主属性对候选码的部分依赖")
    
    def practice_3nf(self):
        """练习：3NF ⭐⭐⭐最重点"""
        print(f"\n【范式】第三范式要求？")
        user_answer = input("你的答案：")
        correct = '消除传递依赖'
        
        self.total += 1
        if '传递' in user_answer or '依赖' in user_answer:
            self.score += 1
            print(f"✅ 正确！3NF：消除非主属性对候选码的传递依赖 ⭐重点必考")
        else:
            print(f"❌ 错误！3NF：消除非主属性对候选码的传递依赖")
    
    def practice_partial_dependency(self):
        """练习：部分依赖"""
        print(f"\n【范式】部分依赖是什么？")
        user_answer = input("你的答案：")
        correct = '只依赖候选码的一部分'
        
        self.total += 1
        if '部分' in user_answer or '候选码' in user_answer:
            self.score += 1
            print(f"✅ 正确！部分依赖：非主属性只依赖候选码的一部分")
        else:
            print(f"❌ 错误！部分依赖：非主属性只依赖候选码的一部分")
    
    def practice_transitive_dependency(self):
        """练习：传递依赖 ⭐重点"""
        print(f"\n【范式】传递依赖是什么？")
        user_answer = input("你的答案：")
        correct = 'A→B→C间接依赖'
        
        self.total += 1
        if '传递' in user_answer or '间接' in user_answer:
            self.score += 1
            print(f"✅ 正确！传递依赖：A→B→C，C通过B间接依赖A")
        else:
            print(f"❌ 错误！传递依赖：A→B→C，C通过B间接依赖A")
    
    def practice_find_candidate_key(self):
        """练习：找候选码 ⭐重点"""
        print(f"\n【范式】找候选码第一步？")
        user_answer = input("你的答案：")
        correct = '找只出现在左边的属性'
        
        self.total += 1
        if '左边' in user_answer or '左' in user_answer:
            self.score += 1
            print(f"✅ 正确！找候选码：先找只出现在左边的属性（必在候选码）")
        else:
            print(f"❌ 错误！找候选码：先找只出现在左边的属性")
    
    # ========== ER图转关系模式 ⭐重点必考 ==========
    
    def practice_1n_convert(self):
        """练习：1:N转换 ⭐重点"""
        print(f"\n【ER转换】1:N联系如何转换？")
        user_answer = input("你的答案：")
        correct = 'N端加外码'
        
        self.total += 1
        if 'N' in user_answer or '外码' in user_answer:
            self.score += 1
            print(f"✅ 正确！1:N：在N端实体加外码（指向1端主码）")
        else:
            print(f"❌ 错误！1:N：在N端实体加外码")
    
    def practice_mn_convert(self):
        """练习：M:N转换 ⭐⭐⭐最重点"""
        print(f"\n【ER转换】M:N联系如何转换？")
        user_answer = input("你的答案：")
        correct = '单独建表'
        
        self.total += 1
        if '单独' in user_answer or '建表' in user_answer or '新建' in user_answer:
            self.score += 1
            print(f"✅ 正确！M:N：单独建关系，包含双方主码 ⭐重点必考")
            print("💡 例：选课（学号，课程号，成绩）")
        else:
            print(f"❌ 错误！M:N：单独建关系，包含双方主码")
    
    def practice_mn_example(self):
        """练习：M:N例子 ⭐重点"""
        print(f"\n【ER转换】学生-课程（M:N选课）如何转换？")
        user_answer = input("你的答案：")
        correct = '选课表含学号和课程号'
        
        self.total += 1
        if '选课' in user_answer or '学号' in user_answer and '课程号' in user_answer:
            self.score += 1
            print(f"✅ 正确！建选课表（学号，课程号，成绩）")
        else:
            print(f"❌ 错误！建选课表（学号，课程号，成绩）")
    
    def practice_er_symbols(self):
        """练习：ER图符号 ⭐重点"""
        print(f"\n【ER转换】实体用什么图形？")
        user_answer = input("你的答案：")
        correct = '矩形'
        
        self.total += 1
        if '矩形' in user_answer or '方框' in user_answer:
            self.score += 1
            print(f"✅ 正确！实体用矩形，联系用菱形，属性用椭圆")
        else:
            print(f"❌ 错误！实体用矩形")
    
    # ========== SQL语句 ⭐重点 ==========
    
    def practice_select_basic(self):
        """练习：SELECT基本语法 ⭐重点"""
        print(f"\n【SQL】SELECT基本语法？")
        user_answer = input("你的答案：")
        correct = 'SELECT 列 FROM 表 WHERE 条件'
        
        self.total += 1
        if 'SELECT' in user_answer.upper() and 'FROM' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！SELECT 列 FROM 表 WHERE 条件")
        else:
            print(f"❌ 错误！SELECT 列 FROM 表 WHERE 条件")
    
    def practice_group_by(self):
        """练习：GROUP BY ⭐重点"""
        print(f"\n【SQL】分组用什么关键字？")
        user_answer = input("你的答案：")
        correct = 'GROUP BY'
        
        self.total += 1
        if 'GROUP' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！GROUP BY 用于分组")
        else:
            print(f"❌ 错误！GROUP BY 用于分组")
    
    def practice_where_vs_having(self):
        """练习：WHERE vs HAVING ⭐重点"""
        print(f"\n【SQL】WHERE和HAVING区别？")
        user_answer = input("你的答案：")
        correct = 'WHERE过滤记录，HAVING过滤分组'
        
        self.total += 1
        if 'WHERE' in user_answer.upper() and 'HAVING' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！WHERE过滤记录，HAVING过滤分组")
        else:
            print(f"❌ 错误！WHERE过滤记录，HAVING过滤分组")
    
    # ========== 进程状态 ⭐重点必考 ==========
    
    def practice_process_states(self):
        """练习：进程三态 ⭐重点"""
        print(f"\n【进程】进程三种基本状态？")
        user_answer = input("你的答案：")
        correct = '运行、就绪、等待'
        
        self.total += 1
        if '运行' in user_answer or '就绪' in user_answer or '等待' in user_answer:
            self.score += 1
            print(f"✅ 正确！进程三态：运行、就绪、等待（阻塞）")
        else:
            print(f"❌ 错误！进程三态：运行、就绪、等待")
    
    def practice_ready_to_running(self):
        """练习：就绪→运行"""
        print(f"\n【进程】就绪→运行的原因？")
        user_answer = input("你的答案：")
        correct = '被调度选中'
        
        self.total += 1
        if '调度' in user_answer or '选中' in user_answer:
            self.score += 1
            print(f"✅ 正确！就绪→运行：进程被调度选中")
        else:
            print(f"❌ 错误！就绪→运行：进程被调度选中")
    
    def practice_running_to_ready(self):
        """练习：运行→就绪 ⭐⭐⭐最重点"""
        print(f"\n【进程】运行→就绪的原因？")
        user_answer = input("你的答案：")
        correct = '时间片用完'
        
        self.total += 1
        if '时间片' in user_answer or '时间' in user_answer:
            self.score += 1
            print(f"✅ 正确！运行→就绪：时间片用完 ⭐重点必考")
        else:
            print(f"❌ 错误！运行→就绪：时间片用完")
    
    def practice_running_to_waiting(self):
        """练习：运行→等待 ⭐重点"""
        print(f"\n【进程】运行→等待的原因？")
        user_answer = input("你的答案：")
        correct = '等待事件'
        
        self.total += 1
        if '等待' in user_answer or 'I/O' in user_answer:
            self.score += 1
            print(f"✅ 正确！运行→等待：等待I/O等事件完成")
        else:
            print(f"❌ 错误！运行→等待：等待I/O等事件完成")
    
    def practice_waiting_to_ready(self):
        """练习：等待→就绪"""
        print(f"\n【进程】等待→就绪的原因？")
        user_answer = input("你的答案：")
        correct = '事件完成'
        
        self.total += 1
        if '事件' in user_answer or '完成' in user_answer:
            self.score += 1
            print(f"✅ 正确！等待→就绪：等待的事件完成")
        else:
            print(f"❌ 错误！等待→就绪：等待的事件完成")
    
    # ========== PV操作 ⭐重点必考 ==========
    
    def practice_p_operation(self):
        """练习：P操作 ⭐⭐⭐最重点"""
        print(f"\n【PV操作】P操作含义？")
        user_answer = input("你的答案：")
        correct = 'S=S-1，申请资源'
        
        self.total += 1
        if '减' in user_answer or '-1' in user_answer or '申请' in user_answer:
            self.score += 1
            print(f"✅ 正确！P操作：S=S-1，申请资源 ⭐重点必考")
        else:
            print(f"❌ 错误！P操作：S=S-1，申请资源")
    
    def practice_v_operation(self):
        """练习：V操作 ⭐⭐⭐最重点"""
        print(f"\n【PV操作】V操作含义？")
        user_answer = input("你的答案：")
        correct = 'S=S+1，释放资源'
        
        self.total += 1
        if '加' in user_answer or '+1' in user_answer or '释放' in user_answer:
            self.score += 1
            print(f"✅ 正确！V操作：S=S+1，释放资源 ⭐重点必考")
        else:
            print(f"❌ 错误！V操作：S=S+1，释放资源")
    
    def practice_mutex_init(self):
        """练习：互斥初值 ⭐⭐⭐最重点"""
        print(f"\n【PV操作】互斥信号量初值？")
        user_answer = input("你的答案：")
        correct = '1'
        
        self.total += 1
        if user_answer == '1':
            self.score += 1
            print(f"✅ 正确！互斥信号量初值S=1 ⭐重点必考")
            print("💡 只有一个进程能进入临界区")
        else:
            print(f"❌ 错误！互斥信号量初值S=1")
    
    def practice_pv_pair(self):
        """练习：PV成对 ⭐重点"""
        print(f"\n【PV操作】P V操作原则？")
        user_answer = input("你的答案：")
        correct = '成对出现'
        
        self.total += 1
        if '成对' in user_answer or '配对' in user_answer:
            self.score += 1
            print(f"✅ 正确！P V必须成对出现，顺序正确")
        else:
            print(f"❌ 错误！P V必须成对出现")
    
    def practice_sync_example(self):
        """练习：同步例子"""
        print(f"\n【PV操作】同步实现？前趋进程执行后后继进程才能执行？")
        user_answer = input("你的答案：")
        correct = '前趋V，后继P'
        
        self.total += 1
        if 'V' in user_answer.upper() and 'P' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！前趋进程V(S)，后继进程P(S)")
        else:
            print(f"❌ 错误！前趋进程V(S)，后继进程P(S)")
    
    # ========== 分页存储 ⭐重点 ==========
    
    def practice_page_structure(self):
        """练习：分页地址结构 ⭐重点"""
        print(f"\n【分页】分页地址结构？")
        user_answer = input("你的答案：")
        correct = '页号+页内地址'
        
        self.total += 1
        if '页号' in user_answer or '页内' in user_answer or '偏移' in user_answer:
            self.score += 1
            print(f"✅ 正确！分页地址：页号 + 页内地址（偏移量）")
        else:
            print(f"❌ 错误！分页地址：页号 + 页内地址")
    
    def practice_page_offset_bits(self):
        """练习：页内地址位数 ⭐重点"""
        print(f"\n【分页】页大小4KB，页内地址多少位？")
        user_answer = input("你的答案：")
        correct = '12'
        
        self.total += 1
        if user_answer == '12':
            self.score += 1
            print(f"✅ 正确！4KB=4096，log2(4096)=12位")
        else:
            print(f"❌ 错误！4KB=4096，log2(4096)=12位")
    
    def practice_lru(self):
        """练习：LRU ⭐重点"""
        print(f"\n【分页】LRU算法淘汰什么页面？")
        user_answer = input("你的答案：")
        correct = '最近最久未使用'
        
        self.total += 1
        if '最久' in user_answer or '未使用' in user_answer:
            self.score += 1
            print(f"✅ 正确！LRU：淘汰最近最久未使用的页面")
        else:
            print(f"❌ 错误！LRU：淘汰最近最久未使用的页面")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*50}")
        print(f"📊 复习完成！得分：{self.score}/{self.total}")
        if self.score == self.total:
            print("🎉 全对！数据库与操作系统掌握很好！")
        elif self.score >= self.total * 0.8:
            print("👍 不错！继续巩固重点概念！")
        else:
            print("💪 还需努力！重点记住：3NF传递依赖、M:N转换、进程状态转换、PV操作、互斥初值=1")
    
    def run(self):
        """运行练习"""
        print("="*50)
        print("数据库+操作系统错题复习 ⭐重点")
        print("="*50)
        print("\n复习重点：")
        print("1. 范式（1NF/2NF/3NF）⭐重点")
        print("2. ER转换（M:N单独建表）⭐⭐⭐最重点")
        print("3. SQL语句 ⭐重点")
        print("4. 进程状态转换 ⭐⭐⭐最重点")
        print("5. PV操作（P减V加、互斥初值=1）⭐⭐⭐最重点")
        print("6. 分页存储 ⭐重点")
        print("7. 综合复习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择复习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                practices = [
                    self.practice_1nf,
                    self.practice_2nf,
                    self.practice_3nf,
                ]
                for p in practices:
                    p()
            elif choice == '2':
                practices = [
                    self.practice_mn_convert,
                    self.practice_mn_example,
                ]
                for p in practices:
                    p()
            elif choice == '3':
                practices = [
                    self.practice_select_basic,
                    self.practice_group_by,
                    self.practice_where_vs_having,
                ]
                for p in practices:
                    p()
            elif choice == '4':
                practices = [
                    self.practice_process_states,
                    self.practice_running_to_ready,
                    self.practice_running_to_waiting,
                ]
                for p in practices:
                    p()
            elif choice == '5':
                practices = [
                    self.practice_p_operation,
                    self.practice_v_operation,
                    self.practice_mutex_init,
                ]
                for p in practices:
                    p()
            elif choice == '6':
                practices = [
                    self.practice_page_structure,
                    self.practice_page_offset_bits,
                    self.practice_lru,
                ]
                for p in practices:
                    p()
            elif choice == '7':
                practices = [
                    self.practice_3nf,
                    self.practice_mn_convert,
                    self.practice_running_to_ready,
                    self.practice_p_operation,
                    self.practice_v_operation,
                    self.practice_mutex_init,
                ]
                for p in practices:
                    p()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    review = 数据库与操作系统复习()
    review.run()