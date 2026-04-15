#!/usr/bin/env python3
"""
数制转换练习脚本
用于练习二进制、八进制、十进制、十六进制之间的转换
"""

import random


class 进制转换练习:
    """数制转换练习类"""

    def __init__(self):
        self.score = 0
        self.total = 0

    def binary_to_decimal(self, binary_str):
        """二进制转十进制"""
        return int(binary_str, 2)

    def decimal_to_binary(self, decimal):
        """十进制转二进制"""
        return bin(decimal)[2:]

    def binary_to_octal(self, binary_str):
        """二进制转八进制（三位一组）"""
        # 补齐到3的倍数
        while len(binary_str) % 3 != 0:
            binary_str = '0' + binary_str
        # 三位分组转换
        octal = ''
        for i in range(0, len(binary_str), 3):
            group = binary_str[i:i + 3]
            octal += str(int(group, 2))
        return octal

    def binary_to_hex(self, binary_str):
        """二进制转十六进制（四位一组）"""
        # 补齐到4的倍数
        while len(binary_str) % 4 != 0:
            binary_str = '0' + binary_str
        # 四位分组转换
        hex_map = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        hex_str = ''
        for i in range(0, len(binary_str), 4):
            group = binary_str[i:i + 4]
            value = int(group, 2)
            if value >= 10:
                hex_str += hex_map[value]
            else:
                hex_str += str(value)
        return hex_str

    def octal_to_binary(self, octal_str):
        """八进制转二进制"""
        binary = ''
        for digit in octal_str:
            # 每位八进制转三位二进制
            b = bin(int(digit))[2:]
            binary += b.zfill(3)
        return binary.lstrip('0') or '0'

    def hex_to_binary(self, hex_str):
        """十六进制转二进制"""
        hex_map = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                   'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
        binary = ''
        for digit in hex_str:
            if digit.upper() in hex_map:
                value = hex_map[digit.upper()]
            else:
                value = int(digit)
            # 每位十六进制转四位二进制
            b = bin(value)[2:]
            binary += b.zfill(4)
        return binary.lstrip('0') or '0'

    def generate_random_binary(self, bits=8):
        """生成随机二进制数"""
        return ''.join([random.choice('01') for _ in range(bits)])

    def generate_random_decimal(self, max_value=255):
        """生成随机十进制数"""
        return random.randint(0, max_value)

    def practice_binary_to_decimal(self):
        """练习：二进制转十进制"""
        binary = self.generate_random_binary(8)
        print(f"\n【题目】将二进制 {binary} 转换为十进制")
        user_answer = input("你的答案：")
        correct_answer = self.binary_to_decimal(binary)

        self.total += 1
        if int(user_answer) == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   计算方法：按权展开")
            self._show_binary_expansion(binary)

    def practice_decimal_to_binary(self):
        """练习：十进制转二进制"""
        decimal = self.generate_random_decimal(255)
        print(f"\n【题目】将十进制 {decimal} 转换为二进制")
        user_answer = input("你的答案：")
        correct_answer = self.decimal_to_binary(decimal)

        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   计算方法：除2取余，逆序排列")

    def practice_binary_to_octal(self):
        """练习：二进制转八进制"""
        binary = self.generate_random_binary(9)  # 9位便于三分组
        print(f"\n【题目】将二进制 {binary} 转换为八进制")
        user_answer = input("你的答案：")
        correct_answer = self.binary_to_octal(binary)

        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   计算方法：三位一组转换")

    def practice_binary_to_hex(self):
        """练习：二进制转十六进制"""
        binary = self.generate_random_binary(8)
        print(f"\n【题目】将二进制 {binary} 转换为十六进制")
        user_answer = input("你的答案：").upper()
        correct_answer = self.binary_to_hex(binary)

        self.total += 1
        if user_answer == correct_answer:
            self.score += 1
            print(f"✅ 正确！答案确实是 {correct_answer}")
        else:
            print(f"❌ 错误！正确答案是 {correct_answer}")
            print(f"   计算方法：四位一组转换")

    def _show_binary_expansion(self, binary):
        """展示二进制按权展开"""
        expansion = []
        for i, bit in enumerate(binary):
            if bit == '1':
                power = len(binary) - i - 1
                value = 2 ** power
                expansion.append(f"2^{power}={value}")
        print(f"   {binary} = {' + '.join(expansion)}")

    def show_score(self):
        """显示得分"""
        print(f"\n{'=' * 40}")
        print(f"📊 练习完成！得分：{self.score}/{self.total}")
        if self.score == self.total:
            print("🎉 全对！太棒了！")
        elif self.score >= self.total * 0.8:
            print("👍 很好！继续保持！")
        else:
            print("💪 需要多练习，加油！")

    def run(self):
        """运行练习"""
        print("=" * 40)
        print("数制转换练习")
        print("=" * 40)
        print("\n练习内容：")
        print("1. 二进制 → 十进制")
        print("2. 十进制 → 二进制")
        print("3. 二进制 → 八进制")
        print("4. 二进制 → 十六进制")
        print("5. 综合练习")
        print("0. 退出")

        while True:
            choice = input("\n选择练习类型（输入数字）：")

            if choice == '0':
                self.show_score()
                break
            elif choice == '1':
                self.practice_binary_to_decimal()
            elif choice == '2':
                self.practice_decimal_to_binary()
            elif choice == '3':
                self.practice_binary_to_octal()
            elif choice == '4':
                self.practice_binary_to_hex()
            elif choice == '5':
                # 综合练习，随机题型
                types = [
                    self.practice_binary_to_decimal,
                    self.practice_decimal_to_binary,
                    self.practice_binary_to_octal,
                    self.practice_binary_to_hex
                ]
                random.choice(types)()
            else:
                print("无效选择，请重新输入")


def main():
    """主函数"""
    practice = 进制转换练习()
    practice.run()


if __name__ == '__main__':
    main()
