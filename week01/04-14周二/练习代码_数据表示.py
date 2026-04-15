#!/usr/bin/env python3
"""
数据表示练习脚本
用于练习原码、反码、补码转换和字符编码
"""

import random

class 数据表示练习:
    """数据表示练习类"""
    
    def __init__(self):
        self.score = 0
        self.total = 0
    
    def decimal_to_binary_8bit(self, decimal):
        """十进制转8位二进制"""
        return format(decimal, '08b')
    
    def get_original_code(self, decimal):
        """获取原码（8位）"""
        if decimal >= 0:
            return format(decimal, '08b')
        else:
            # 负数：符号位为1，其余位为绝对值的二进制
            return '1' + format(abs(decimal), '07b')
    
    def get_inverse_code(self, original_code):
        """获取反码"""
        if original_code[0] == '0':  # 正数
            return original_code
        else:  # 负数：符号位不变，数值位取反
            result = '1'
            for bit in original_code[1:]:
                result += '1' if bit == '0' else '0'
            return result
    
    def get_complement_code(self, inverse_code):
        """获取补码"""
        if inverse_code[0] == '0':  # 正数
            return inverse_code
        else:  # 负数：反码+1
            # 从右往左找第一个0，从该位开始取反
            binary = inverse_code[1:]
            result = list(binary)
            i = len(result) - 1  # 修复：7 位数值，索引从 6 开始
            while i >= 0 and result[i] == '1':
                result[i] = '0'
                i -= 1
            if i >= 0:
                result[i] = '1'
            return '1' + ''.join(result)
    
    def complement_to_decimal(self, complement_code):
        """补码转十进制真值"""
        if complement_code[0] == '0':  # 正数
            return int(complement_code, 2)
        else:  # 负数
            if complement_code == '10000000':  # 特殊值 -128
                return -128
            # 补码 -1 得反码，反码取反得原码，原码转十进制
            inverse = self.complement_minus_one(complement_code)
            original = self.inverse_to_original(inverse)
            return -int(original[1:], 2)
    
    def complement_minus_one(self, complement):
        """补码减1"""
        result = list(complement)
        i = 7
        while i >= 0 and result[i] == '0':
            result[i] = '1'
            i -= 1
        if i >= 0:
            result[i] = '0'
        return ''.join(result)
    
    def inverse_to_original(self, inverse):
        """反码转原码"""
        if inverse[0] == '0':
            return inverse
        else:
            result = '1'
            for bit in inverse[1:]:
                result += '1' if bit == '0' else '0'
            return result
    
    def practice_original_code(self):
        """练习：获取原码"""
        decimals = [5, -5, 127, -127, 0, 10, -10, 63, -63, 1]
        decimal = random.choice(decimals)
        
        print(f"\n【题目】写出十进制 {decimal} 的8位原码")
        user_answer = input("你的答案（8位二进制）：")
        correct_answer = self.get_original_code(decimal)
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            if decimal >= 0:
                print(f"   正数原码：符号位为0，数值位为二进制")
            else:
                print(f"   负数原码：符号位为1，数值位为绝对值二进制")
    
    def practice_inverse_code(self):
        """练习：获取反码"""
        decimals = [5, -5, 127, -127, 10, -10, 63, -63, 1, -1]
        decimal = random.choice(decimals)
        
        print(f"\n【题目】写出十进制 {decimal} 的8位反码")
        user_answer = input("你的答案（8位二进制）：")
        
        original = self.get_original_code(decimal)
        correct_answer = self.get_inverse_code(original)
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            if decimal >= 0:
                print(f"   正数反码：与原码相同")
            else:
                print(f"   负数反码：符号位不变，数值位取反")
    
    def practice_complement_code(self):
        """练习：获取补码（重点）"""
        decimals = [5, -5, -1, -128, 127, -127, 0, -10, 10, -63]
        decimal = random.choice(decimals)
        
        print(f"\n【题目】写出十进制 {decimal} 的8位补码")
        user_answer = input("你的答案（8位二进制）：")
        
        if decimal == -128:
            correct_answer = '10000000'  # 特殊情况
        else:
            original = self.get_original_code(decimal)
            inverse = self.get_inverse_code(original)
            correct_answer = self.get_complement_code(inverse)
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            if decimal >= 0:
                print(f"   正数补码：与原码相同")
            else:
                print(f"   负数补码：反码+1")
    
    def practice_complement_to_decimal(self):
        """练习：补码转十进制（重点）"""
        codes = ['11111111', '11111110', '10000000', '10000001', 
                 '01111111', '00000001', '10101011', '11110000']
        code = random.choice(codes)
        
        print(f"\n【题目】补码 {code} 表示的十进制真值是多少？")
        user_answer = int(input("你的答案："))
        correct_answer = self.complement_to_decimal(code)
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   方法：补码-1得反码，反码取反得原码，原码转十进制")
    
    def practice_range(self):
        """练习：补码范围"""
        bits = random.choice([8, 16, 32])
        
        print(f"\n【题目】{bits}位补码能表示的数值范围是？")
        print("请输入最小值和最大值（格式：最小 最大）")
        user_answer = input("你的答案：").split()
        
        min_val = -(2 ** (bits - 1))
        max_val = 2 ** (bits - 1) - 1
        
        self.total += 1
        if len(user_answer) == 2 and int(user_answer[0]) == min_val and int(user_answer[1]) == max_val:
            self.score += 1
            print(f"✅ 正确！范围是 [{min_val}, {max_val}]")
        else:
            print(f"❌ 错误！正确答案是 [{min_val}, {max_val}]")
            print(f"   公式：最小=-2^(n-1)，最大=2^(n-1)-1")
            print(f"   注意：负数比正数多一个（因为-0被吞掉）")
    
    def practice_ascii(self):
        """练习：ASCII编码"""
        chars = ['A', 'a', '0', 'Z', 'z', '9', 'B', 'b']
        char = random.choice(chars)
        
        print(f"\n【题目】字符 '{char}' 的ASCII码是多少？")
        user_answer = int(input("你的答案（十进制）："))
        correct_answer = ord(char)
        
        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   记忆：'0'=48, 'A'=65, 'a'=97")
            print(f"   大小写差值：32")
    
    def show_score(self):
        """显示得分"""
        print(f"\n{'='*40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
        if self.score == self.total:
            print("🎉 全对！太棒了！")
        elif self.score >= self.total * 0.8:
            print("👍 很好！继续保持！")
        else:
            print("💪 需要多练习，加油！")
    
    def run(self):
        """运行练习"""
        print("="*40)
        print("数据表示练习")
        print("="*40)
        print("\n练习内容：")
        print("1. 原码转换")
        print("2. 反码转换")
        print("3. 补码转换 ⭐重点")
        print("4. 补码转十进制 ⭐重点")
        print("5. 补码范围")
        print("6. ASCII编码")
        print("7. 综合练习")
        print("0. 退出")
        
        while True:
            choice = input("\n选择练习类型（输入数字）：")
            
            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_original_code()
            elif choice == '2':
                self.practice_inverse_code()
            elif choice == '3':
                self.practice_complement_code()
            elif choice == '4':
                self.practice_complement_to_decimal()
            elif choice == '5':
                self.practice_range()
            elif choice == '6':
                self.practice_ascii()
            elif choice == '7':
                types = [
                    self.practice_complement_code,
                    self.practice_complement_to_decimal,
                    self.practice_range,
                    self.practice_ascii
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


def main():
    practice = 数据表示练习()
    practice.run()


if __name__ == '__main__':
    main()