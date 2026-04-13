#!/usr/bin/env python3
"""
OSI/TCP/IP模型练习脚本
用于练习网络层次模型
"""

import random

class 网络模型练习:
    """网络模型练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
        
        # OSI七层模型
        self.osi_layers = [
            ('应用层', 7, 'HTTP、FTP、SMTP'),
            ('表示层', 6, 'SSL/TLS'),
            ('会话层', 5, 'RPC'),
            ('传输层', 4, 'TCP、UDP'),
            ('网络层', 3, 'IP、ICMP、路由器'),
            ('数据链路层', 2, 'Ethernet、交换机'),
            ('物理层', 1, '网线、集线器'),
        ]
        
        # TCP/IP四层模型
        self.tcpip_layers = [
            ('应用层', '对应OSI 5-7层'),
            ('传输层', 'TCP、UDP'),
            ('网际层', 'IP'),
            ('网络接口层', '对应OSI 1-2层'),
        ]
    
    def practice_osi_7layers(self):
        """练习：OSI七层 ⭐重点"""
        print(f"\n【题目】OSI模型有几层？")
        user_answer = input("你的答案：")
        correct = '7'
        
        self.total += 1
        if user_answer == '7' or '七层' in user_answer:
            self.score += 1
            print(f"✅ 正确！OSI模型有7层")
        else:
            print(f"❌ 错误！OSI模型有7层")
    
    def practice_tcpip_4layers(self):
        """练习：TCP/IP四层 ⭐重点"""
        print(f"\n【题目】TCP/IP模型有几层？")
        user_answer = input("你的答案：")
        correct = '4'
        
        self.total += 1
        if user_answer == '4' or '四层' in user_answer:
            self.score += 1
            print(f"✅ 正确！TCP/IP模型有4层")
        else:
            print(f"❌ 错误！TCP/IP模型有4层")
    
    def practice_application_layer(self):
        """练习：应用层 ⭐重点"""
        print(f"\n【题目】应用层对应OSI第几层？")
        user_answer = input("你的答案：")
        correct = '7'
        
        self.total += 1
        if user_answer == '7':
            self.score += 1
            print(f"✅ 正确！应用层是第7层")
            print(f"   协议：HTTP、FTP、SMTP")
        else:
            print(f"❌ 错误！应用层是第7层")
    
    def practice_transport_layer(self):
        """练习：传输层 ⭐重点"""
        print(f"\n【题目】传输层对应OSI第几层？")
        user_answer = input("你的答案：")
        correct = '4'
        
        self.total += 1
        if user_answer == '4':
            self.score += 1
            print(f"✅ 正确！传输层是第4层")
            print(f"   协议：TCP、UDP")
        else:
            print(f"❌ 错误！传输层是第4层")
    
    def practice_network_layer(self):
        """练习：网络层 ⭐重点"""
        print(f"\n【题目】网络层对应OSI第几层？")
        user_answer = input("你的答案：")
        correct = '3'
        
        self.total += 1
        if user_answer == '3':
            self.score += 1
            print(f"✅ 正确！网络层是第3层")
            print(f"   协议：IP、ICMP")
            print(f"   设备：路由器")
        else:
            print(f"❌ 错误！网络层是第3层")
    
    def practice_data_link_layer(self):
        """练习：数据链路层 ⭐重点"""
        print(f"\n【题目】数据链路层对应OSI第几层？")
        user_answer = input("你的答案：")
        correct = '2'
        
        self.total += 1
        if user_answer == '2':
            self.score += 1
            print(f"✅ 正确！数据链路层是第2层")
            print(f"   协议：Ethernet")
            print(f"   设备：交换机")
        else:
            print(f"❌ 错误！数据链路层是第2层")
    
    def practice_physical_layer(self):
        """练习：物理层"""
        print(f"\n【题目】物理层对应OSI第几层？")
        user_answer = input("你的答案：")
        correct = '1'
        
        self.total += 1
        if user_answer == '1':
            self.score += 1
            print(f"✅ 正确！物理层是第1层")
            print(f"   设备：网线、集线器")
        else:
            print(f"❌ 错误！物理层是第1层")
    
    def practice_router_layer(self):
        """练习：路由器工作层 ⭐重点"""
        print(f"\n【题目】路由器工作在OSI哪层？")
        user_answer = input("你的答案：")
        correct = '网络层（第3层）'
        
        self.total += 1
        if '网络' in user_answer or '3' in user_answer:
            self.score += 1
            print(f"✅ 正确！路由器工作在网络层（第3层）")
        else:
            print(f"❌ 错误！路由器工作在网络层（第3层）")
    
    def practice_switch_layer(self):
        """练习：交换机工作层 ⭐重点"""
        print(f"\n【题目】交换机工作在OSI哪层？")
        user_answer = input("你的答案：")
        correct = '数据链路层（第2层）'
        
        self.total += 1
        if '链路' in user_answer or '2' in user_answer:
            self.score += 1
            print(f"✅ 正确！交换机工作在数据链路层（第2层）")
        else:
            print(f"❌ 错误！交换机工作在数据链路层（第2层）")
    
    def practice_hub_layer(self):
        """练习：集线器工作层"""
        print(f"\n【题目】集线器工作在OSI哪层？")
        user_answer = input("你的答案：")
        correct = '物理层（第1层）'
        
        self.total += 1
        if '物理' in user_answer or '1' in user_answer:
            self.score += 1
            print(f"✅ 正确！集线器工作在物理层（第1层）")
        else:
            print(f"❌ 错误！集线器工作在物理层（第1层）")
    
    def practice_tcp_layer(self):
        """练习：TCP工作层 ⭐重点"""
        print(f"\n【题目】TCP工作在OSI哪层？")
        user_answer = input("你的答案：")
        correct = '传输层（第4层）'
        
        self.total += 1
        if '传输' in user_answer or '4' in user_answer:
            self.score += 1
            print(f"✅ 正确！TCP工作在传输层（第4层）")
        else:
            print(f"❌ 错误！TCP工作在传输层（第4层）")
    
    def practice_ip_layer(self):
        """练习：IP工作层 ⭐重点"""
        print(f"\n【题目】IP工作在OSI哪层？")
        user_answer = input("你的答案：")
        correct = '网络层（第3层）'
        
        self.total += 1
        if '网络' in user_answer or '3' in user_answer:
            self.score += 1
            print(f"✅ 正确！IP工作在网络层（第3层）")
        else:
            print(f"❌ 错误！IP工作在网络层（第3层）")
    
    def practice_http_layer(self):
        """练习：HTTP工作层 ⭐重点"""
        print(f"\n【题目】HTTP工作在OSI哪层？")
        user_answer = input("你的答案：")
        correct = '应用层（第7层）'
        
        self.total += 1
        if '应用' in user_answer or '7' in user_answer:
            self.score += 1
            print(f"✅ 正确！HTTP工作在应用层（第7层）")
        else:
            print(f"❌ 错误！HTTP工作在应用层（第7层）")
    
    def practice_layer_order(self):
        """练习：OSI层次顺序 ⭐重点"""
        print(f"\n【题目】OSI七层从上到下顺序？")
        user_answer = input("你的答案（说出一层）：")
        
        layers = ['应用', '表示', '会话', '传输', '网络', '链路', '物理']
        
        self.total += 1
        if any(layer in user_answer for layer in layers):
            self.score += 1
            print(f"✅ 正确！OSI七层顺序：")
            print(f"   7 应用层 → 6 表示层 → 5 会话层")
            print(f"   4 传输层 → 3 网络层 → 2 链路层 → 1 物理层")
        else:
            print(f"❌ OSI七层顺序：")
            print(f"   7 应用层 → 6 表示层 → 5 会话层")
            print(f"   4 传输层 → 3 网络层 → 2 链路层 → 1 物理层")
    
    def practice_tcpip_vs_osi(self):
        """练习：TCP/IP vs OSI对比 ⭐重点"""
        print(f"\n【题目】TCP/IP应用层对应OSI哪几层？")
        user_answer = input("你的答案：")
        correct = '5-7层'
        
        self.total += 1
        if '5' in user_answer and '7' in user_answer:
            self.score += 1
            print(f"✅ 正确！TCP/IP应用层对应OSI 5-7层")
            print(f"   OSI: 会话层 + 表示层 + 应用层")
        else:
            print(f"❌ 错误！TCP/IP应用层对应OSI 5-7层")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("OSI/TCP/IP网络模型练习")
        print("="*40)
        print("\n练习内容：")
        print("1. OSI七层 ⭐重点")
        print("2. TCP/IP四层 ⭐重点")
        print("3. 应用层（第7层）⭐重点")
        print("4. 传输层（第4层）⭐重点")
        print("5. 网络层（第3层）⭐重点")
        print("6. 数据链路层（第2层）⭐重点")
        print("7. 物理层（第1层）")
        print("8. 路由器工作层 ⭐重点")
        print("9. 交换机工作层 ⭐重点")
        print("10. TCP工作层 ⭐重点")
        print("11. IP工作层 ⭐重点")
        print("12. HTTP工作层 ⭐重点")
        print("13. OSI层次顺序 ⭐重点")
        print("14. TCP/IP vs OSI对比 ⭐重点")
        print("15. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_osi_7layers()
            elif choice == '2':
                self.practice_tcpip_4layers()
            elif choice == '3':
                self.practice_application_layer()
            elif choice == '4':
                self.practice_transport_layer()
            elif choice == '5':
                self.practice_network_layer()
            elif choice == '6':
                self.practice_data_link_layer()
            elif choice == '7':
                self.practice_physical_layer()
            elif choice == '8':
                self.practice_router_layer()
            elif choice == '9':
                self.practice_switch_layer()
            elif choice == '10':
                self.practice_tcp_layer()
            elif choice == '11':
                self.practice_ip_layer()
            elif choice == '12':
                self.practice_http_layer()
            elif choice == '13':
                self.practice_layer_order()
            elif choice == '14':
                self.practice_tcpip_vs_osi()
            elif choice == '15':
                types = [
                    self.practice_router_layer,
                    self.practice_switch_layer,
                    self.practice_tcp_layer,
                    self.practice_ip_layer,
                    self.practice_network_layer,
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


if __name__ == '__main__':
    practice = 网络模型练习()
    practice.run()