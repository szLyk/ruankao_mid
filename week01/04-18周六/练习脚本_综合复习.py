"""
Week1 综合复习刷题脚本
涵盖：数制转换、补码、二叉树性质、图结构
"""

import random
import math


def clear_screen():
    """清屏"""
    print("\n" + "=" * 50)


def section_header(title):
    """打印章节标题"""
    clear_screen()
    print(f"  {title}")
    print("=" * 50)


# ==================== 数制转换模块 ====================

def binary_to_decimal(binary_str):
    """二进制转十进制"""
    return int(binary_str, 2)


def decimal_to_binary(decimal):
    """十进制转二进制"""
    if decimal == 0:
        return "0"
    result = ""
    while decimal > 0:
        result = str(decimal % 2) + result
        decimal //= 2
    return result


def binary_to_octal(binary_str):
    """二进制转八进制"""
    # 补齐到3的倍数
    while len(binary_str) % 3 != 0:
        binary_str = "0" + binary_str
    result = ""
    for i in range(0, len(binary_str), 3):
        group = binary_str[i:i+3]
        result += str(int(group, 2))
    return result


def binary_to_hex(binary_str):
    """二进制转十六进制"""
    # 补齐到4的倍数
    while len(binary_str) % 4 != 0:
        binary_str = "0" + binary_str
    hex_map = "0123456789ABCDEF"
    result = ""
    for i in range(0, len(binary_str), 4):
        group = binary_str[i:i+4]
        result += hex_map[int(group, 2)]
    return result


def hex_to_decimal(hex_str):
    """十六进制转十进制"""
    return int(hex_str, 16)


def octal_to_decimal(octal_str):
    """八进制转十进制"""
    return int(octal_str, 8)


def practice_number_conversion():
    """数制转换练习"""
    section_header("一、数制转换练习（10题）")

    questions = [
        {
            "q": "(1101)₂ = (    )₁₀",
            "answer": "13",
            "hint": "1×8 + 1×4 + 0×2 + 1×1 = 13"
        },
        {
            "q": "(255)₁₀ = (    )₂",
            "answer": "11111111",
            "hint": "255 = 128+64+32+16+8+4+2+1"
        },
        {
            "q": "(101110)₂ = (    )₈",
            "answer": "56",
            "hint": "101=5, 110=6 → 56"
        },
        {
            "q": "(FF)₁₆ = (    )₂ = (    )₁₀",
            "answer": "11111111,255",
            "hint": "F=15=1111, FF=11111111=255"
        },
        {
            "q": "(AB)₁₆ = (    )₁₀",
            "answer": "171",
            "hint": "A=10, B=11 → 10×16+11=171"
        },
        {
            "q": "(377)₈ = (    )₁₀",
            "answer": "255",
            "hint": "3×64 + 7×8 + 7×1 = 255"
        },
        {
            "q": "十进制63转二进制？",
            "answer": "111111",
            "hint": "63 = 32+16+8+4+2+1 = 6个1"
        },
        {
            "q": "二进制101010转十六进制？",
            "answer": "2A",
            "hint": "1010=A, 0010=2 → 2A"
        },
        {
            "q": "八进制17转二进制？",
            "answer": "1111",
            "hint": "1=001, 7=111 → 001111 → 1111"
        },
        {
            "q": "十六进制10转十进制？",
            "answer": "16",
            "hint": "1×16 + 0×1 = 16"
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\n【第{i}题】")
        print(f"题目：{q['q']}")
        user_answer = input("你的答案：").strip().replace(" ", "").replace("=", ",")

        if user_answer.upper() == q["answer"].upper().replace(" ", ""):
            print("✅ 正确！")
            score += 1
        else:
            print(f"❌ 错误！正确答案：{q['answer']}")
            print(f"💡 提示：{q['hint']}")

    print(f"\n数制转换得分：{score}/10")
    return score


# ==================== 补码模块 ====================

def decimal_to_complement(decimal, bits=8):
    """十进制转补码"""
    if decimal >= 0:
        # 正数：直接转二进制，补齐位数
        binary = decimal_to_binary(decimal)
        return binary.zfill(bits)
    else:
        # 负数：取反加1
        # 先计算绝对值的二进制
        abs_binary = decimal_to_binary(abs(decimal)).zfill(bits)
        # 取反
        inverted = "".join("1" if b == "0" else "0" for b in abs_binary)
        # 加1
        result = ""
        carry = 1
        for b in reversed(inverted):
            if b == "0" and carry == 1:
                result = "1" + result
                carry = 0
            elif b == "1" and carry == 1:
                result = "0" + result
                carry = 1
            else:
                result = b + result
        return result


def complement_to_decimal(complement):
    """补码转十进制"""
    if complement[0] == "0":
        # 正数
        return int(complement, 2)
    else:
        # 负数：取反加1，取负
        inverted = "".join("1" if b == "0" else "0" for b in complement)
        # 加1
        result = ""
        carry = 1
        for b in reversed(inverted):
            if b == "0" and carry == 1:
                result = "1" + result
                carry = 0
            elif b == "1" and carry == 1:
                result = "0" + result
                carry = 1
            else:
                result = b + result
        return -int(result, 2)


def practice_complement():
    """补码练习"""
    section_header("二、数据表示（补码）练习（10题）⭐重点")

    print("\n【补码核心知识】")
    print("- 8位补码范围：-128 到 +127")
    print("- -1 的补码：11111111")
    print("- -128 的补码：10000000")
    print("- 负数比正数多1个（因为0占用正数位置）")

    questions = [
        {
            "q": "-1的8位补码是？",
            "answer": "11111111",
            "hint": "1→00000001→取反11111110→加1→11111111"
        },
        {
            "q": "-128的8位补码是？",
            "answer": "10000000",
            "hint": "特殊值！-128无法用常规方法计算，直接记住"
        },
        {
            "q": "补码11111111表示的真值？",
            "answer": "-1",
            "hint": "首位为1是负数，取反加1得1，所以是-1"
        },
        {
            "q": "补码10000000表示的真值？",
            "answer": "-128",
            "hint": "特殊值！这是最小的负数"
        },
        {
            "q": "8位补码范围是？",
            "answer": "-128到127",
            "hint": "负数-128到-1（128个），正数0到127（128个）"
        },
        {
            "q": "字符'A'的ASCII码？",
            "answer": "65",
            "hint": "记住'A'=65，'a'=97，'0'=48"
        },
        {
            "q": "字符'a'的ASCII码？",
            "answer": "97",
            "hint": "小写字母比大写大32，'A'+32=97"
        },
        {
            "q": "字符'0'的ASCII码？",
            "answer": "48",
            "hint": "数字字符从48开始，'0'=48, '9'=57"
        },
        {
            "q": "大小写字母ASCII差值？",
            "answer": "32",
            "hint": "'a'-'A'=97-65=32"
        },
        {
            "q": "16位补码范围是？",
            "answer": "-32768到32767",
            "hint": "2^15=32768，负数比正数多1"
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\n【第{i}题】⭐" if i <= 5 else f"\n【第{i}题】")
        print(f"题目：{q['q']}")
        user_answer = input("你的答案：").strip().replace(" ", "").replace("到", "到").replace("-", "到")

        # 答案匹配处理
        correct = q["answer"].replace(" ", "").replace("到", "到").replace("-", "到")
        if user_answer in correct or correct in user_answer:
            print("✅ 正确！")
            score += 1
        else:
            print(f"❌ 错误！正确答案：{q['answer']}")
            print(f"💡 提示：{q['hint']}")

    print(f"\n补码得分：{score}/10")
    return score


# ==================== 二叉树模块 ====================

def calculate_tree_depth(n):
    """计算完全二叉树深度"""
    return math.floor(math.log2(n)) + 1


def calculate_full_tree_nodes(depth):
    """计算满二叉树节点数"""
    return 2 ** depth - 1


def calculate_n0_from_n2(n2):
    """根据n2计算n0"""
    return n2 + 1


def calculate_n2_from_n0(n0):
    """根据n0计算n2"""
    return n0 - 1


def find_parent(node_index):
    """找父节点"""
    return math.floor(node_index / 2)


def find_children(node_index):
    """找孩子节点"""
    return 2 * node_index, 2 * node_index + 1


def practice_binary_tree():
    """二叉树练习"""
    section_header("四、二叉树练习（10题）⭐重点")

    print("\n【二叉树核心性质】")
    print("- 性质3：n0 = n2 + 1（必考！）")
    print("- 完全二叉树深度：⌊log₂n⌋ + 1")
    print("- 满二叉树节点数：2^k - 1")
    print("- 父节点：⌊i/2⌋，左孩子：2i，右孩子：2i+1")

    questions = [
        {
            "q": "二叉树n2=30，n0=？",
            "answer": "31",
            "hint": "n0 = n2 + 1 = 30 + 1 = 31"
        },
        {
            "q": "二叉树n0=50，n2=？",
            "answer": "49",
            "hint": "n2 = n0 - 1 = 50 - 1 = 49"
        },
        {
            "q": "100个节点的完全二叉树深度？",
            "answer": "7",
            "hint": "⌊log₂100⌋ + 1 = ⌊6.64⌋ + 1 = 7"
        },
        {
            "q": "深度4的满二叉树节点数？",
            "answer": "15",
            "hint": "2^4 - 1 = 16 - 1 = 15"
        },
        {
            "q": "完全二叉树节点50的父节点？",
            "answer": "25",
            "hint": "⌊50/2⌋ = 25"
        },
        {
            "q": "前序ABDECF，中序DBEACF，后序？",
            "answer": "DEBFCA",
            "hint": "前序定根，中序分左右，递归求解"
        },
        {
            "q": "前序+后序能否唯一确定二叉树？",
            "answer": "不能",
            "hint": "必须要有中序才能区分左右子树"
        },
        {
            "q": "层序遍历用什么实现？",
            "answer": "队列",
            "hint": "FIFO特性，逐层访问"
        },
        {
            "q": "前序遍历顺序？",
            "answer": "根左右",
            "hint": "先访问根，再左子树，最后右子树"
        },
        {
            "q": "后序遍历顺序？",
            "answer": "左右根",
            "hint": "先左子树，再右子树，最后根"
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\n【第{i}题】⭐" if i <= 7 else f"\n【第{i}题】")
        print(f"题目：{q['q']}")
        user_answer = input("你的答案：").strip()

        if user_answer in q["answer"] or q["answer"] in user_answer:
            print("✅ 正确！")
            score += 1
        else:
            print(f"❌ 错误！正确答案：{q['answer']}")
            print(f"💡 提示：{q['hint']}")

    print(f"\n二叉树得分：{score}/10")
    return score


# ==================== 图结构模块 ====================

def undirected_complete_graph_edges(n):
    """无向完全图边数"""
    return n * (n - 1) // 2


def directed_complete_graph_edges(n):
    """有向完全图边数"""
    return n * (n - 1)


def practice_graph():
    """图结构练习"""
    section_header("五、图结构练习（5题）")

    print("\n【图核心公式】")
    print("- 无向完全图边数：n(n-1)/2")
    print("- 有向完全图边数：n(n-1)")
    print("- 稀疏图用邻接表，稠密图用邻接矩阵")
    print("- DFS用栈，BFS用队列")

    questions = [
        {
            "q": "无向完全图5个顶点有多少边？",
            "answer": "10",
            "hint": "n(n-1)/2 = 5×4/2 = 10"
        },
        {
            "q": "有向完全图5个顶点有多少边？",
            "answer": "20",
            "hint": "n(n-1) = 5×4 = 20"
        },
        {
            "q": "稀疏图用什么存储？",
            "answer": "邻接表",
            "hint": "边少时邻接表节省空间"
        },
        {
            "q": "频繁判断边是否存在用什么存储？",
            "answer": "邻接矩阵",
            "hint": "矩阵可O(1)判断边是否存在"
        },
        {
            "q": "DFS用什么实现？",
            "answer": "栈或递归",
            "hint": "深度优先需要记住路径，用栈"
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\n【第{i}题】")
        print(f"题目：{q['q']}")
        user_answer = input("你的答案：").strip()

        if user_answer in q["answer"] or q["answer"] in user_answer:
            print("✅ 正确！")
            score += 1
        else:
            print(f"❌ 错误！正确答案：{q['answer']}")
            print(f"💡 提示：{q['hint']}")

    print(f"\n图结构得分：{score}/5")
    return score


# ==================== 工具函数模块 ====================

def number_conversion_tool():
    """数制转换工具"""
    section_header("数制转换计算工具")

    while True:
        print("\n功能选项：")
        print("1. 二进制 → 十进制")
        print("2. 十进制 → 二进制")
        print("3. 二进制 → 八进制")
        print("4. 二进制 → 十六进制")
        print("5. 十六进制 → 十进制")
        print("6. 八进制 → 十进制")
        print("0. 返回主菜单")

        choice = input("\n选择功能（输入数字）：").strip()

        if choice == "0":
            break
        elif choice == "1":
            binary = input("输入二进制数：").strip()
            print(f"结果：{binary_to_decimal(binary)}")
        elif choice == "2":
            decimal = int(input("输入十进制数：").strip())
            print(f"结果：{decimal_to_binary(decimal)}")
        elif choice == "3":
            binary = input("输入二进制数：").strip()
            print(f"结果：{binary_to_octal(binary)}")
        elif choice == "4":
            binary = input("输入二进制数：").strip()
            print(f"结果：{binary_to_hex(binary)}")
        elif choice == "5":
            hex_num = input("输入十六进制数：").strip()
            print(f"结果：{hex_to_decimal(hex_num)}")
        elif choice == "6":
            octal = input("输入八进制数：").strip()
            print(f"结果：{octal_to_decimal(octal)}")


def complement_tool():
    """补码计算工具"""
    section_header("补码计算工具")

    while True:
        print("\n功能选项：")
        print("1. 十进制 → 补码")
        print("2. 补码 → 十进制（真值）")
        print("3. 查看8位补码范围表")
        print("0. 返回主菜单")

        choice = input("\n选择功能（输入数字）：").strip()

        if choice == "0":
            break
        elif choice == "1":
            decimal = int(input("输入十进制数（-128到127）：").strip())
            bits = int(input("位数（默认8位）：").strip() or "8")
            result = decimal_to_complement(decimal, bits)
            print(f"{decimal} 的 {bits}位补码：{result}")
        elif choice == "2":
            complement = input("输入补码：").strip()
            result = complement_to_decimal(complement)
            print(f"补码 {complement} 的真值：{result}")
        elif choice == "3":
            print("\n【8位补码范围表】")
            print("十进制      补码")
            print("-128      →  10000000  （最小负数）")
            print("-127      →  10000001")
            print("-1        →  11111111")
            print("0         →  00000000")
            print("1         →  00000001")
            print("127       →  01111111  （最大正数）")


def binary_tree_tool():
    """二叉树计算工具"""
    section_header("二叉树计算工具")

    while True:
        print("\n功能选项：")
        print("1. 根据n2计算n0")
        print("2. 根据n0计算n2")
        print("3. 计算完全二叉树深度")
        print("4. 计算满二叉树节点数")
        print("5. 找父节点和孩子节点")
        print("6. 根据总节点n计算n0,n1,n2")
        print("0. 返回主菜单")

        choice = input("\n选择功能（输入数字）：").strip()

        if choice == "0":
            break
        elif choice == "1":
            n2 = int(input("输入n2（度为2的节点数）：").strip())
            n0 = calculate_n0_from_n2(n2)
            print(f"n0 = n2 + 1 = {n2} + 1 = {n0}")
        elif choice == "2":
            n0 = int(input("输入n0（叶子节点数）：").strip())
            n2 = calculate_n2_from_n0(n0)
            print(f"n2 = n0 - 1 = {n0} - 1 = {n2}")
        elif choice == "3":
            n = int(input("输入完全二叉树节点数：").strip())
            depth = calculate_tree_depth(n)
            print(f"深度 = ⌊log₂{n}⌋ + 1 = ⌊{math.log2(n):.2f}⌋ + 1 = {depth}")
        elif choice == "4":
            depth = int(input("输入满二叉树深度：").strip())
            nodes = calculate_full_tree_nodes(depth)
            print(f"节点数 = 2^{depth} - 1 = {nodes}")
        elif choice == "5":
            node = int(input("输入节点编号：").strip())
            parent = find_parent(node)
            left, right = find_children(node)
            print(f"父节点：⌊{node}/2⌋ = {parent}")
            print(f"左孩子：2×{node} = {left}")
            print(f"右孩子：2×{node}+1 = {right}")
        elif choice == "6":
            n = int(input("输入总节点数n：").strip())
            # 对于完全二叉树
            n1 = n % 2  # 奇数时n1=0，偶数时n1=1
            n0 = (n + 1) // 2
            n2 = n0 - 1
            print(f"\n【完全二叉树结果】")
            print(f"n = {n} ({'偶数' if n%2==0 else '奇数'})")
            print(f"n1 = {n1} （奇数时为0，偶数时为1）")
            print(f"n0 = {n0} （叶子节点）")
            print(f"n2 = {n2} （度为2的节点）")
            print(f"验证：n0 + n1 + n2 = {n0} + {n1} + {n2} = {n0+n1+n2}")


def graph_tool():
    """图计算工具"""
    section_header("图计算工具")

    while True:
        print("\n功能选项：")
        print("1. 计算无向完全图边数")
        print("2. 计算有向完全图边数")
        print("3. 计算稀疏图/稠密图判定")
        print("0. 返回主菜单")

        choice = input("\n选择功能（输入数字）：").strip()

        if choice == "0":
            break
        elif choice == "1":
            n = int(input("输入顶点数：").strip())
            edges = undirected_complete_graph_edges(n)
            print(f"无向完全图边数 = n(n-1)/2 = {n}×{n-1}/2 = {edges}")
        elif choice == "2":
            n = int(input("输入顶点数：").strip())
            edges = directed_complete_graph_edges(n)
            print(f"有向完全图边数 = n(n-1) = {n}×{n-1} = {edges}")
        elif choice == "3":
            n = int(input("输入顶点数n：").strip())
            e = int(input("输入边数e：").strip())
            threshold = n * (n - 1) // 2  # 完全图边数的一半
            if e < threshold:
                print(f"边数 {e} < {threshold}，判定为【稀疏图】，建议用邻接表")
            else:
                print(f"边数 {e} >= {threshold}，判定为【稠密图】，建议用邻接矩阵")


# ==================== 主菜单 ====================

def main_menu():
    """主菜单"""
    total_score = 0

    while True:
        section_header("Week1 综合复习刷题系统")
        print("\n【刷题练习】")
        print("1. 数制转换练习（10题）")
        print("2. 补码练习（10题）⭐重点")
        print("3. 二叉树练习（10题）⭐重点")
        print("4. 图结构练习（5题）")
        print("5. 全部练习（45题）")

        print("\n【计算工具】")
        print("6. 数制转换工具")
        print("7. 补码计算工具")
        print("8. 二叉树计算工具")
        print("9. 图计算工具")

        print("\n0. 退出")

        choice = input("\n请选择：").strip()

        if choice == "0":
            print("\n感谢使用！复习加油！💪")
            break
        elif choice == "1":
            total_score += practice_number_conversion()
        elif choice == "2":
            total_score += practice_complement()
        elif choice == "3":
            total_score += practice_binary_tree()
        elif choice == "4":
            total_score += practice_graph()
        elif choice == "5":
            total_score = 0
            total_score += practice_number_conversion()
            total_score += practice_complement()
            total_score += practice_binary_tree()
            total_score += practice_graph()
            print(f"\n{'='*50}")
            print(f"  总得分：{total_score}/45")
            print(f"{'='*50}")
        elif choice == "6":
            number_conversion_tool()
        elif choice == "7":
            complement_tool()
        elif choice == "8":
            binary_tree_tool()
        elif choice == "9":
            graph_tool()


if __name__ == "__main__":
    main_menu()