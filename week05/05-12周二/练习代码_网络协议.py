#!/usr/bin/env python3
"""
网络协议练习脚本
用于练习TCP/UDP/IP等协议
"""

import random

class 网络协议练习:
    """网络协议练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_tcp_vs_udp(self):
        """练习：TCP vs UDP对比 ⭐重点必考"""
        print(f"\n【题目】TCP和UDP的主要区别？")
        print("请选择正确的说法：")
        print("A. TCP面向连接可靠，UDP无连接不可靠")
        print("B. TCP无连接不可靠，UDP面向连接可靠")
        user_answer = input("你的答案（A或B）：")
        correct = 'A'
        
        self.total += 1
        if user_answer.upper() == correct:
            self.score += 1
            print(f"✅ 正确！TCP面向连接可靠，UDP无连接不可靠")
        else:
            print(f"❌ 错误！TCP面向连接可靠，UDP无连接不可靠")
    
    def practice_tcp_connection(self):
        """练习：TCP面向连接 ⭐重点"""
        print(f"\n【题目】TCP是面向连接还是无连接？")
        user_answer = input("你的答案：")
        correct = '面向连接'
        
        self.total += 1
        if '面向' in user_answer or '连接' in user_answer:
            self.score += 1
            print(f"✅ 正确！TCP是面向连接的协议")
            print(f"   需要三次握手建立连接")
        else:
            print(f"❌ 错误！TCP是面向连接的协议")
    
    def practice_udp_connection(self):
        """练习：UDP无连接"""
        print(f"\n【题目】UDP是面向连接还是无连接？")
        user_answer = input("你的答案：")
        correct = '无连接'
        
        self.total += 1
        if '无' in user_answer:
            self.score += 1
            print(f"✅ 正确！UDP是无连接的协议")
            print(f"   直接发送，不建立连接")
        else:
            print(f"❌ 错误！UDP是无连接的协议")
    
    def practice_tcp_reliable(self):
        """练习：TCP可靠性 ⭐重点"""
        print(f"\n【题目】TCP是可靠还是不可靠传输？")
        user_answer = input("你的答案：")
        correct = '可靠'
        
        self.total += 1
        if '可靠' in user_answer:
            self.score += 1
            print(f"✅ 正确！TCP是可靠传输")
            print(f"   有确认、重传机制")
        else:
            print(f"❌ 错误！TCP是可靠传输")
    
    def practice_udp_reliable(self):
        """练习：UDP可靠性"""
        print(f"\n【题目】UDP是可靠还是不可靠传输？")
        user_answer = input("你的答案：")
        correct = '不可靠'
        
        self.total += 1
        if '不可靠' in user_answer:
            self.score += 1
            print(f"✅ 正确！UDP是不可靠传输")
            print(f"   无确认、无重传")
        else:
            print(f"❌ 错误！UDP是不可靠传输")
    
    def practice_tcp_speed(self):
        """练习：TCP速度"""
        print(f"\n【题目】TCP和UDP哪个传输速度更快？")
        user_answer = input("你的答案：")
        correct = 'UDP'
        
        self.total += 1
        if 'UDP' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！UDP更快")
            print(f"   无连接建立、无确认，开销小")
        else:
            print(f"❌ 错误！UDP更快")
    
    def practice_tcp_handshake(self):
        """练习：TCP三次握手 ⭐重点"""
        print(f"\n【题目】TCP建立连接用什么方法？")
        user_answer = input("你的答案：")
        correct = '三次握手'
        
        self.total += 1
        if '三次' in user_answer or '握手' in user_answer:
            self.score += 1
            print(f"✅ 正确！TCP用三次握手建立连接")
            print(f"   SYN → SYN+ACK → ACK")
        else:
            print(f"❌ 错误！TCP用三次握手建立连接")
    
    def practice_dns_protocol(self):
        """练习：DNS协议 ⭐重点"""
        print(f"\n【题目】DNS使用什么协议？")
        user_answer = input("你的答案：")
        correct = 'UDP'
        
        self.total += 1
        if 'UDP' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！DNS主要使用UDP")
            print(f"   快速查询，UDP开销小")
        else:
            print(f"❌ 错误！DNS主要使用UDP")
    
    def practice_http_protocol(self):
        """练习：HTTP协议 ⭐重点"""
        print(f"\n【题目】HTTP使用什么协议？")
        user_answer = input("你的答案：")
        correct = 'TCP'
        
        self.total += 1
        if 'TCP' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！HTTP使用TCP")
            print(f"   需要可靠传输")
        else:
            print(f"❌ 错误！HTTP使用TCP")
    
    def practice_tcp_port(self):
        """练习：TCP端口"""
        print(f"\n【题目】TCP用什么标识应用？")
        user_answer = input("你的答案：")
        correct = '端口'
        
        self.total += 1
        if '端口' in user_answer:
            self.score += 1
            print(f"✅ 正确！TCP用端口标识应用")
        else:
            print(f"❌ 错误！TCP用端口标识应用")
    
    def practice_http_port(self):
        """练习：HTTP默认端口 ⭐重点"""
        print(f"\n【题目】HTTP默认端口是？")
        user_answer = input("你的答案：")
        correct = '80'
        
        self.total += 1
        if user_answer == '80':
            self.score += 1
            print(f"✅ 正确！HTTP默认端口是80")
        else:
            print(f"❌ 错误！HTTP默认端口是80")
    
    def practice_https_port(self):
        """练习：HTTPS默认端口 ⭐重点"""
        print(f"\n【题目】HTTPS默认端口是？")
        user_answer = input("你的答案：")
        correct = '443'
        
        self.total += 1
        if user_answer == '443':
            self.score += 1
            print(f"✅ 正确！HTTPS默认端口是443")
        else:
            print(f"❌ 错误！HTTPS默认端口是443")
    
    def practice_tcp_udp_application(self):
        """练习：TCP/UDP应用场景 ⭐重点"""
        questions = [
            ('HTTP用TCP还是UDP？', 'TCP'),
            ('DNS用TCP还是UDP？', 'UDP'),
            ('视频流用TCP还是UDP？', 'UDP'),
            ('文件传输用TCP还是UDP？', 'TCP'),
            ('邮件传输用TCP还是UDP？', 'TCP'),
        ]
        
        question, correct = random.choice(questions)
        
        print(f"\n【题目】{question}")
        user_answer = input("你的答案：")
        
        self.total += 1
        if user_answer.upper().strip() == correct.upper().strip():
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct}")
        else:
            print(f"❌ 错误！正确答案是 {correct}")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("网络协议练习（TCP/UDP/IP）")
        print("="*40)
        print("\n练习内容：")
        print("1. TCP vs UDP对比 ⭐重点必考")
        print("2. TCP面向连接 ⭐重点")
        print("3. UDP无连接")
        print("4. TCP可靠性 ⭐重点")
        print("5. UDP不可靠")
        print("6. TCP vs UDP速度")
        print("7. TCP三次握手 ⭐重点")
        print("8. DNS协议 ⭐重点")
        print("9. HTTP协议 ⭐重点")
        print("10. TCP端口")
        print("11. HTTP默认端口 ⭐重点")
        print("12. HTTPS默认端口 ⭐重点")
        print("13. TCP/UDP应用场景 ⭐重点")
        print("14. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_tcp_vs_udp()
            elif choice == '2':
                self.practice_tcp_connection()
            elif choice == '3':
                self.practice_udp_connection()
            elif choice == '4':
                self.practice_tcp_reliable()
            elif choice == '5':
                self.practice_udp_reliable()
            elif choice == '6':
                self.practice_tcp_speed()
            elif choice == '7':
                self.practice_tcp_handshake()
            elif choice == '8':
                self.practice_dns_protocol()
            elif choice == '9':
                self.practice_http_protocol()
            elif choice == '10':
                self.practice_tcp_port()
            elif choice == '11':
                self.practice_http_port()
            elif choice == '12':
                self.practice_https_port()
            elif choice == '13':
                self.practice_tcp_udp_application()
            elif choice == '14':
                types = [
                    self.practice_tcp_vs_udp,
                    self.practice_dns_protocol,
                    self.practice_http_port,
                    self.practice_tcp_udp_application,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 网络协议练习()
    practice.run()