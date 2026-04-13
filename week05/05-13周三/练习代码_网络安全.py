#!/usr/bin/env python3
"""
网络安全练习脚本
用于练习加密技术、认证技术
"""

import random

class 网络安全练习:
    """网络安全练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def practice_symmetric_encryption(self):
        """练习：对称加密 ⭐重点"""
        print(f"\n【题目】对称加密算法有哪些？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['DES', 'AES']
        
        self.total += 1
        if 'DES' in user_answer.upper() or 'AES' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！对称加密算法：DES、AES")
            print(f"   特点：加密解密用同一密钥，速度快")
        else:
            print(f"❌ 错误！对称加密算法：DES、AES")
    
    def practice_asymmetric_encryption(self):
        """练习：非对称加密 ⭐重点"""
        print(f"\n【题目】非对称加密算法有哪些？")
        user_answer = input("你的答案（说出一个）：")
        correct = ['RSA', 'ECC']
        
        self.total += 1
        if 'RSA' in user_answer.upper() or 'ECC' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！非对称加密算法：RSA、ECC")
            print(f"   特点：公钥加密私钥解密，速度慢")
        else:
            print(f"❌ 错误！非对称加密算法：RSA、ECC")
    
    def practice_symmetric_vs_asymmetric(self):
        """练习：对称vs非对称 ⭐重点必考"""
        print(f"\n【题目】对称加密和非对称加密的区别？")
        print("请选择：")
        print("A. 对称用同一密钥快，非对称用公私钥慢")
        print("B. 对称用公私钥慢，非对称用同一密钥快")
        user_answer = input("你的答案（A或B）：")
        correct = 'A'
        
        self.total += 1
        if user_answer.upper() == correct:
            self.score += 1
            print(f"✅ 正确！")
            print(f"   对称：同一密钥，速度快")
            print(f"   非对称：公钥加密私钥解密，速度慢")
        else:
            print(f"❌ 错误！正确答案是A")
    
    def practice_symmetric_speed(self):
        """练习：对称加密速度 ⭐重点"""
        print(f"\n【题目】对称加密和非对称加密哪个更快？")
        user_answer = input("你的答案：")
        correct = '对称加密'
        
        self.total += 1
        if '对称' in user_answer:
            self.score += 1
            print(f"✅ 正确！对称加密更快")
            print(f"   算法简单，效率高")
        else:
            print(f"❌ 错误！对称加密更快")
    
    def practice_asymmetric_key_management(self):
        """练习：非对称密钥管理 ⭐重点"""
        print(f"\n【题目】哪种加密密钥管理更方便？")
        user_answer = input("你的答案：")
        correct = '非对称加密'
        
        self.total += 1
        if '非对称' in user_answer or 'RSA' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！非对称加密密钥管理更方便")
            print(f"   公钥公开，私钥自己保存")
        else:
            print(f"❌ 错误！非对称加密密钥管理更方便")
    
    def practice_hybrid_encryption(self):
        """练习：混合加密 ⭐重点"""
        print(f"\n【题目】实际应用中如何结合两种加密？")
        user_answer = input("你的答案：")
        correct = '用非对称加密密钥，用对称加密数据'
        
        self.total += 1
        if '对称加密数据' in user_answer:
            self.score += 1
            print(f"✅ 正确！混合加密：")
            print(f"   用非对称加密密钥（解决密钥管理）")
            print(f"   用对称加密数据（解决速度问题）")
        else:
            print(f"❌ 错误！混合加密：")
            print(f"   用非对称加密密钥")
            print(f"   用对称加密数据")
    
    def practice_digital_signature(self):
        """练习：数字签名 ⭐重点"""
        print(f"\n【题目】数字签名用什么加密？")
        user_answer = input("你的答案：")
        correct = '私钥签名，公钥验证'
        
        self.total += 1
        if '私钥' in user_answer and '公钥' in user_answer:
            self.score += 1
            print(f"✅ 正确！数字签名：私钥签名，公钥验证")
            print(f"   功能：验证身份、防篡改")
        else:
            print(f"❌ 错误！数字签名：私钥签名，公钥验证")
    
    def practice_digital_certificate(self):
        """练习：数字证书 ⭐重点"""
        print(f"\n【题目】数字证书由谁颁发？")
        user_answer = input("你的答案：")
        correct = 'CA（证书颁发机构）'
        
        self.total += 1
        if 'CA' in user_answer.upper() or '证书' in user_answer:
            self.score += 1
            print(f"✅ 正确！数字证书由CA颁发")
            print(f"   包含公钥和身份信息")
        else:
            print(f"❌ 错误！数字证书由CA颁发")
    
    def practice_ssl_tls(self):
        """练习：SSL/TLS ⭐重点"""
        print(f"\n【题目】SSL/TLS的作用？")
        user_answer = input("你的答案：")
        correct = '传输层安全加密'
        
        self.total += 1
        if '安全' in user_answer or '加密' in user_answer:
            self.score += 1
            print(f"✅ 正确！SSL/TLS：传输层安全加密")
        else:
            print(f"❌ 错误！SSL/TLS：传输层安全加密")
    
    def practice_https(self):
        """练习：HTTPS ⭐重点"""
        print(f"\n【题目】HTTPS = ？")
        user_answer = input("你的答案：")
        correct = 'HTTP + SSL/TLS'
        
        self.total += 1
        if 'SSL' in user_answer.upper() or 'TLS' in user_answer.upper():
            self.score += 1
            print(f"✅ 正确！HTTPS = HTTP + SSL/TLS")
        else:
            print(f"❌ 错误！HTTPS = HTTP + SSL/TLS")
    
    def practice_http_vs_https(self):
        """练习：HTTP vs HTTPS"""
        print(f"\n【题目】HTTP和HTTPS的区别？")
        user_answer = input("你的答案：")
        correct = 'HTTP无加密，HTTPS有SSL加密'
        
        self.total += 1
        if '加密' in user_answer:
            self.score += 1
            print(f"✅ 正确！HTTP无加密，HTTPS有SSL加密")
        else:
            print(f"❌ 错误！HTTP无加密，HTTPS有SSL加密")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("网络安全练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 对称加密算法 ⭐重点")
        print("2. 非对称加密算法 ⭐重点")
        print("3. 对称vs非对称区别 ⭐重点必考")
        print("4. 对称加密速度 ⭐重点")
        print("5. 非对称密钥管理 ⭐重点")
        print("6. 混合加密 ⭐重点")
        print("7. 数字签名 ⭐重点")
        print("8. 数字证书 ⭐重点")
        print("9. SSL/TLS ⭐重点")
        print("10. HTTPS ⭐重点")
        print("11. HTTP vs HTTPS")
        print("12. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_symmetric_encryption()
            elif choice == '2':
                self.practice_asymmetric_encryption()
            elif choice == '3':
                self.practice_symmetric_vs_asymmetric()
            elif choice == '4':
                self.practice_symmetric_speed()
            elif choice == '5':
                self.practice_asymmetric_key_management()
            elif choice == '6':
                self.practice_hybrid_encryption()
            elif choice == '7':
                self.practice_digital_signature()
            elif choice == '8':
                self.practice_digital_certificate()
            elif choice == '9':
                self.practice_ssl_tls()
            elif choice == '10':
                self.practice_https()
            elif choice == '11':
                self.practice_http_vs_https()
            elif choice == '12':
                types = [
                    self.practice_symmetric_vs_asymmetric,
                    self.practice_hybrid_encryption,
                    self.practice_digital_signature,
                    self.practice_https,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 网络安全练习()
    practice.run()