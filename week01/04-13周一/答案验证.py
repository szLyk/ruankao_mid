#!/usr/bin/env python3
"""
数制转换快速验证脚本
用于验证进制转换答案
"""

def convert(binary_str, to_type):
    """
    将二进制转换为其他进制
    
    参数：
        binary_str: 二进制字符串
        to_type: 转换类型（decimal/octal/hex）
    
    返回：
        转换后的值
    """
    decimal = int(binary_str, 2)
    
    if to_type == 'decimal':
        return decimal
    elif to_type == 'octal':
        return oct(decimal)[2:]
    elif to_type == 'hex':
        return hex(decimal)[2:].upper()
    else:
        return decimal


def decimal_to_binary(decimal):
    """十进制转二进制"""
    return bin(decimal)[2:]


def verify_all():
    """验证所有题目答案"""
    print("=" * 50)
    print("数制转换答案验证")
    print("=" * 50)
    
    # 二进制转十进制验证
    print("\n【一、二进制转十进制】")
    test_cases = [
        ('1011', 11),
        ('11010', 26),
        ('11111111', 255),
        ('10000000', 128),
        ('10101010', 170),
        ('11110000', 240),
        ('101', 5),
        ('1001', 9),
        ('11001100', 204),
        ('0', 0),
    ]
    
    for binary, expected in test_cases:
        result = convert(binary, 'decimal')
        status = "✅" if result == expected else "❌"
        print(f"{status} {binary} → {result} (预期: {expected})")
    
    # 十进制转二进制验证
    print("\n【二、十进制转二进制】")
    test_cases = [
        (25, '11001'),
        (100, '1100100'),
        (127, '1111111'),
        (128, '10000000'),
        (63, '111111'),
        (16, '10000'),
        (31, '11111'),
        (255, '11111111'),
        (10, '1010'),
        (1, '1'),
    ]
    
    for decimal, expected in test_cases:
        result = decimal_to_binary(decimal)
        status = "✅" if result == expected else "❌"
        print(f"{status} {decimal} → {result} (预期: {expected})")
    
    # 二进制转八进制验证
    print("\n【三、二进制转八进制】")
    test_cases = [
        ('101110', '56'),
        ('1101011', '153'),
        ('11111111', '377'),
        ('1000', '10'),
        ('10101100', '254'),
    ]
    
    for binary, expected in test_cases:
        result = convert(binary, 'octal')
        status = "✅" if result == expected else "❌"
        print(f"{status} {binary} → {result} (预期: {expected})")
    
    # 二进制转十六进制验证
    print("\n【四、二进制转十六进制】")
    test_cases = [
        ('10111010', 'BA'),
        ('11111111', 'FF'),
        ('10000000', '80'),
        ('11110000', 'F0'),
        ('10101010', 'AA'),
    ]
    
    for binary, expected in test_cases:
        result = convert(binary, 'hex')
        status = "✅" if result == expected else "❌"
        print(f"{status} {binary} → {result} (预期: {expected})")
    
    print("\n验证完成！")


if __name__ == '__main__':
    verify_all()