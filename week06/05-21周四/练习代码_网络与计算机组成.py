#!/usr/bin/env python3
"""
网络+计算机组成错题复习练习脚本
涵盖：OSI模型、TCP/UDP、加密算法、数制转换、补码 ⭐复习重点
"""

import random

class 网络与计算机组成复习:
    """网络+计算机组成复习练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    # ========== OSI七层模型 ⭐重点必考 ==========
    
    def practice_osi_layers(self):
        """练习：OSI七层 ⭐⭐⭐最重点"""
        print(f"\n【OSI】七层模型从上到下？")
        user_answer = input("你的答案（说出3个以上）：")
        correct = ['应用', '表示', '会话', '传输', '网络', '数据链路', '物理']
        
        self.total += 1
        if any(c in user_answer for c in correct[:3]):
            self.score += 1
            print(f"✅ 正确！应用→表示→会话→传输→网络→数据链路→物理")
        else:
            print(f"❌ 错误！应用→表示→会话→传输→网络→数据链路→物理")
    
    def practice_transport_layer(self):
        """练习：传输层协议 ⭐⭐⭐最重点"""
        print(f"\n【OSI】传输层协议有哪些？")
        user_answer = input("你的答案：")
        correct = ['TCP', 'UDP']
        
        self.total += 1
        if 'TCP' in user_answer.upper() or 'UDP' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！传输层协议：TCP、UDP ⭐重点必考")
        else:
            print(f"❌ 错误！传输层协议：TCP、UDP")
    
    def practice_network_layer(self):
        """练习：网络层 ⭐重点"""
        print(f"\n【OSI】网络层功能？")
        user_answer = input("你的答案：")
        correct = '路由选择'
        
        self.total += 1
        if '路由' in user_answer or '寻址' in user_answer:
            self.score += 1
            print(f"✅ 正确！网络层：路由选择、拥塞控制")
        else:
            print(f"❌ 错误！网络层：路由选择、拥塞控制")
    
    def practice_network_device(self):
        """练习：网络层设备 ⭐重点"""
        print(f"\n【OSI】网络层设备？")
        user_answer = input("你的答案：")
        correct = '路由器'
        
        self.total += 1
        if '路由' in user_answer:
            self.score += 1
            print(f"✅ 正确！网络层设备：路由器")
        else:
            print(f"❌ 错误！网络层设备：路由器")
    
    def practice_data_link_device(self):
        """练习：数据链路层设备 ⭐重点"""
        print(f"\n【OSI】数据链路层设备？")
        user_answer = input("你的答案：")
        correct = '交换机'
        
        self.total += 1
        if '交换' in user_answer:
            self.score += 1
            print(f"✅ 正确！数据链路层设备：交换机")
        else:
            print(f"❌ 错误！数据链路层设备：交换机")
    
    def practice_application_layer(self):
        """练习：应用层协议 ⭐重点"""
        print(f"\n【OSI】应用层协议有哪些？")
        user_answer = input("你的答案：")
        correct = ['HTTP', 'FTP', 'SMTP', 'DNS']
        
        self.total += 1
        if any(c in user_answer.upper() for c in correct):
            self.score += 1
            print(f"✅ 正确！应用层：HTTP、FTP、SMTP、DNS")
        else:
            print(f"❌ 错误！应用层：HTTP、FTP、SMTP、DNS")
    
    # ========== TCP vs UDP ⭐重点必考 ==========
    
    def practice_tcp_features(self):
        """练习：TCP特点 ⭐⭐⭐最重点"""
        print(f"\n【TCP】TCP特点？")
        user_answer = input("你的答案：")
        correct = '面向连接、可靠'
        
        self.total += 1
        if '连接' in user_answer or '可靠' in user_answer:
            self.score += 1
            print(f"✅ 正确！TCP：面向连接、可靠传输、三次握手 ⭐重点必考")
        else:
            print(f"❌ 错误！TCP：面向连接、可靠传输")
    
    def practice_udp_features(self):
        """练习：UDP特点 ⭐⭐⭐最重点"""
        print(f"\n【UDP】UDP特点？")
        user_answer = input("你的答案：")
        correct = '无连接、快'
        
        self.total += 1
        if '无连接' in user_answer or '不可靠' in user_answer or '快' in user_answer:
            self.score += 1
            print(f"✅ 正确！UDP：无连接、不可靠、快 ⭐重点必考")
        else:
            print(f"❌ 错误！UDP：无连接、不可靠、快")
    
    def practice_tcp_vs_udp(self):
        """练习：TCP vs UDP ⭐⭐⭐最重点"""
        print(f"\n【TCP/UDP】TCP和UDP主要区别？")
        user_answer = input("你的答案：")
        correct = 'TCP可靠慢，UDP不可靠快'
        
        self.total += 1
        if '可靠' in user_answer and ('快' in user_answer or '慢' in user_answer):
            self.score += 1
            print(f"✅ 正确！TCP面向连接可靠慢，UDP无连接不可靠快 ⭐重点必考")
        else:
            print(f"❌ 错误！TCP面向连接可靠慢，UDP无连接不可靠快")
    
    def practice_tcp_application(self):
        """练习：TCP应用 ⭐重点"""
        print(f"\n【TCP】TCP适用场景？")
        user_answer = input("你的答案：")
        correct = ['HTTP', 'FTP', '邮件']
        
        self.total += 1
        if any(c in user_answer.upper() for c in correct):
            self.score += 1
            print(f"✅ 正确！TCP应用：HTTP、FTP、邮件（需要可靠传输）")
        else:
            print(f"❌ 错误！TCP应用：HTTP、FTP、邮件")
    
    def practice_udp_application(self):
        """练习：UDP应用 ⭐重点"""
        print(f"\n【UDP】UDP适用场景？")
        user_answer = input("你的答案：")
        correct = ['DNS', '视频', '流']
        
        self.total += 1
        if any(c in user_answer.upper() for c in correct):
            self.score += 1
            print(f"✅ 正确！UDP应用：DNS、视频流（实时性优先）")
        else:
            print(f"❌ 错误！UDP应用：DNS、视频流")
    
    # ========== 网络协议端口 ⭐重点 ==========
    
    def practice_dns_port(self):
        """练习：DNS端口 ⭐⭐⭐最重点"""
        print(f"\n【协议】DNS协议端口？")
        user_answer = input("你的答案：")
        correct = '53'
        
        self.total += 1
        if user_answer == '53':
            self.score += 1
            print(f"✅ 正确！DNS端口53 ⭐重点必考")
        else:
            print(f"❌ 错误！DNS端口53")
    
    def practice_http_port(self):
        """练习：HTTP端口 ⭐重点"""
        print(f"\n【协议】HTTP协议端口？")
        user_answer = input("你的答案：")
        correct = '80'
        
        self.total += 1
        if user_answer == '80':
            self.score += 1
            print(f"✅ 正确！HTTP端口80")
        else:
            print(f"❌ 错误！HTTP端口80")
    
    def practice_https_port(self):
        """练习：HTTPS端口 ⭐重点"""
        print(f"\n【协议】HTTPS协议端口？")
        user_answer = input("你的答案：")
        correct = '443'
        
        self.total += 1
        if user_answer == '443':
            self.score += 1
            print(f"✅ 正确！HTTPS端口443")
        else:
            print(f"❌ 错误！HTTPS端口443")
    
    def practice_ftp_port(self):
        """练习：FTP端口"""
        print(f"\n【协议】FTP协议端口？")
        user_answer = input("你的答案：")
        correct = ['20', '21']
        
        self.total += 1
        if '20' in user_answer or '21' in user_answer:
            self.score += 1
            print(f"✅ 正确！FTP端口20(数据)+21(控制)")
        else:
            print(f"❌ 错误！FTP端口20(数据)+21(控制)")
    
    # ========== 加密算法 ⭐重点必考 ==========
    
    def practice_symmetric_algorithms(self):
        """练习：对称加密算法 ⭐⭐⭐最重点"""
        print(f"\n【加密】对称加密算法有哪些？")
        user_answer = input("你的答案：")
        correct = ['DES', 'AES']
        
        self.total += 1
        if 'DES' in user_answer.upper() or 'AES' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！对称加密：DES、AES、3DES ⭐重点必考")
            print("💡 特点：快，密钥管理难")
        else:
            print(f"❌ 错误！对称加密：DES、AES、3DES")
    
    def practice_asymmetric_algorithms(self):
        """练习：非对称加密算法 ⭐⭐⭐最重点"""
        print(f"\n【加密】非对称加密算法有哪些？")
        user_answer = input("你的答案：")
        correct = ['RSA', 'ECC']
        
        self.total += 1
        if 'RSA' in user_answer.upper() or 'ECC' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！非对称加密：RSA、ECC ⭐重点必考")
            print("💡 特点：慢，密钥管理易")
        else:
            print(f"❌ 错误！非对称加密：RSA、ECC")
    
    def practice_symmetric_vs_asymmetric(self):
        """练习：对称vs非对称 ⭐重点"""
        print(f"\n【加密】对称加密和非对称加密区别？")
        user_answer = input("你的答案：")
        correct = '对称快密钥难，非对称慢密钥易'
        
        self.total += 1
        if '快' in user_answer or '慢' in user_answer or '密钥' in user_answer:
            self.score += 1
            print(f"✅ 正确！")
            print("对称加密：快、密钥管理难、DES/AES")
            print("非对称加密：慢、密钥管理易、RSA/ECC")
        else:
            print(f"❌ 错误！对称快密钥难，非对称慢密钥易")
    
    def practice_digital_signature(self):
        """练习：数字签名 ⭐重点"""
        print(f"\n【加密】数字签名用什么加密？")
        user_answer = input("你的答案：")
        correct = '私钥签名'
        
        self.total += 1
        if '私钥' in user_answer:
            self.score += 1
            print(f"✅ 正确！数字签名：私钥签名、公钥验证")
        else:
            print(f"❌ 错误！数字签名：私钥签名、公钥验证")
    
    # ========== 数制转换 ⭐重点必考 ==========
    
    def practice_binary_to_decimal(self):
        """练习：二进制转十进制 ⭐⭐⭐最重点"""
        print(f"\n【数制】二进制1011转十进制？")
        user_answer = input("你的答案：")
        correct = '11'
        
        self.total += 1
        if user_answer == '11':
            self.score += 1
            print(f"✅ 正确！1011₂ = 1×8 + 0×4 + 1×2 + 1×1 = 11 ⭐重点必考")
        else:
            print(f"❌ 错误！1011₂ = 11（按权展开）")
    
    def practice_decimal_to_binary(self):
        """练习：十进制转二进制 ⭐重点"""
        print(f"\n【数制】十进制13转二进制？")
        user_answer = input("你的答案：")
        correct = '1101'
        
        self.total += 1
        if user_answer == '1101':
            self.score += 1
            print(f"✅ 正确！13 = 1101₂（除2取余）")
        else:
            print(f"❌ 错误！13 = 1101₂")
    
    def practice_binary_to_octal(self):
        """练习：二进制转八进制 ⭐⭐⭐最重点"""
        print(f"\n【数制】二进制1011转八进制？")
        user_answer = input("你的答案：")
        correct = '13'
        
        self.total += 1
        if user_answer == '13':
            self.score += 1
            print(f"✅ 正确！1011₂ = 001 011 = 13₈（三位一组）⭐重点必考")
        else:
            print(f"❌ 错误！1011₂ = 13₈（三位一组）")
    
    def practice_binary_to_hex(self):
        """练习：二进制转十六进制 ⭐⭐⭐最重点"""
        print(f"\n【数制】二进制1011转十六进制？")
        user_answer = input("你的答案：")
        correct = 'B'
        
        self.total += 1
        if user_answer.upper() == 'B':
            self.score += 1
            print(f"✅ 正确！1011₂ = B₁₆（四位一组）⭐重点必考")
        else:
            print(f"❌ 错误！1011₂ = B₁₆（四位一组）")
    
    def practice_hex_digits(self):
        """练习：十六进制数字 ⭐重点"""
        print(f"\n【数制】十六进制A等于十进制多少？")
        user_answer = input("你的答案：")
        correct = '10'
        
        self.total += 1
        if user_answer == '10':
            self.score += 1
            print(f"✅ 正确！A=10, B=11, C=12, D=13, E=14, F=15")
        else:
            print(f"❌ 错误！A=10")
    
    # ========== 补码运算 ⭐重点必考 ==========
    
    def practice_complement_negative1(self):
        """练习：补码-1 ⭐⭐⭐最重点"""
        print(f"\n【补码】8位补码11111111表示？")
        user_answer = input("你的答案：")
        correct = '-1'
        
        self.total += 1
        if user_answer == '-1':
            self.score += 1
            print(f"✅ 正确！11111111表示-1 ⭐重点必考")
            print("💡 解析：符号位1，数值位取反+1 → 00000000+1=1 → -1")
        else:
            print(f"❌ 错误！11111111表示-1")
    
    def practice_complement_negative128(self):
        """练习：补码-128 ⭐⭐⭐最重点"""
        print(f"\n【补码】8位补码10000000表示？")
        user_answer = input("你的答案：")
        correct = '-128'
        
        self.total += 1
        if user_answer == '-128':
            self.score += 1
            print(f"✅ 正确！10000000表示-128 ⭐重点必考")
            print("💡 特殊值：补码负数范围比正数多一个")
        else:
            print(f"❌ 错误！10000000表示-128")
    
    def practice_complement_positive1(self):
        """练习：补码+1"""
        print(f"\n【补码】8位补码00000001表示？")
        user_answer = input("你的答案：")
        correct = '+1'
        
        self.total += 1
        if user_answer == '1' or user_answer == '+1':
            self.score += 1
            print(f"✅ 正确！00000001表示+1（正数补码等于原码）")
        else:
            print(f"❌ 错误！00000001表示+1")
    
    def practice_complement_range(self):
        """练习：补码范围 ⭐重点"""
        print(f"\n【补码】8位补码范围？")
        user_answer = input("你的答案：")
        correct = '-128到127'
        
        self.total += 1
        if '128' in user_answer and '127' in user_answer:
            self.score += 1
            print(f"✅ 正确！8位补码范围：-128到+127")
        else:
            print(f"❌ 错误！8位补码范围：-128到+127")
    
    def practice_negative_rule(self):
        """练习：负数补码规则 ⭐重点"""
        print(f"\n【补码】负数补码如何计算？")
        user_answer = input("你的答案：")
        correct = '原码取反+1'
        
        self.total += 1
        if '取反' in user_answer and '1' in user_answer:
            self.score += 1
            print(f"✅ 正确！负数补码：原码→符号位不变其余取反→+1")
        else:
            print(f"❌ 错误！负数补码：原码→符号位不变其余取反→+1")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*50}")
        print(f"📊 复习完成！得分：{self.score}/{self.total}")
        if self.score == self.total:
            print("🎉 全对！网络与计算机组成掌握很好！")
        elif self.score >= self.total * 0.8:
            print("👍 不错！继续巩固重点概念！")
        else:
            print("💪 还需努力！重点记住：TCP可靠慢UDP快、DNS端口53、对称AES非对称RSA、补码-1=11111111")
    
    def run(self):
        """运行练习"""
        print("="*50)
        print("网络+计算机组成错题复习 ⭐重点")
        print("="*50)
        print("\n复习重点：")
        print("1. OSI传输层（TCP/UDP）⭐⭐⭐最重点")
        print("2. TCP vs UDP区别 ⭐⭐⭐最重点")
        print("3. 协议端口（DNS=53）⭐重点")
        print("4. 加密算法（对称AES/非对称RSA）⭐⭐⭐最重点")
        print("5. 数制转换 ⭐重点")
        print("6. 补码运算 ⭐⭐⭐最重点")
        print("7. 综合复习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择复习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                practices = [
                    self.practice_transport_layer,
                    self.practice_network_layer,
                    self.practice_network_device,
                ]
                for p in practices:
                    p()
            elif choice == '2':
                practices = [
                    self.practice_tcp_features,
                    self.practice_udp_features,
                    self.practice_tcp_vs_udp,
                ]
                for p in practices:
                    p()
            elif choice == '3':
                practices = [
                    self.practice_dns_port,
                    self.practice_http_port,
                ]
                for p in practices:
                    p()
            elif choice == '4':
                practices = [
                    self.practice_symmetric_algorithms,
                    self.practice_asymmetric_algorithms,
                    self.practice_symmetric_vs_asymmetric,
                ]
                for p in practices:
                    p()
            elif choice == '5':
                practices = [
                    self.practice_binary_to_decimal,
                    self.practice_binary_to_octal,
                    self.practice_binary_to_hex,
                ]
                for p in practices:
                    p()
            elif choice == '6':
                practices = [
                    self.practice_complement_negative1,
                    self.practice_complement_negative128,
                    self.practice_complement_range,
                ]
                for p in practices:
                    p()
            elif choice == '7':
                practices = [
                    self.practice_tcp_vs_udp,
                    self.practice_dns_port,
                    self.practice_symmetric_algorithms,
                    self.practice_asymmetric_algorithms,
                    self.practice_binary_to_decimal,
                    self.practice_complement_negative1,
                ]
                for p in practices:
                    p()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    review = 网络与计算机组成复习()
    review.run()