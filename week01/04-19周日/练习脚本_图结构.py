"""
04-19 图结构练习脚本
涵盖：图的基本概念、完全图边数、邻接矩阵/邻接表、存储选择
"""

import math


def clear_screen():
    """清屏"""
    print("\n" + "=" * 50)


def section_header(title):
    """打印章节标题"""
    clear_screen()
    print(f"  {title}")
    print("=" * 50)


# ==================== 完全图边数计算 ====================

def undirected_complete_edges(n):
    """无向完全图边数"""
    return n * (n - 1) // 2


def directed_complete_edges(n):
    """有向完全图边数"""
    return n * (n - 1)


# ==================== 练习模块 ====================

def practice_basic_concepts():
    """图的基本概念练习"""
    section_header("一、图的基本概念（10题）")

    print("\n【核心概念】")
    print("- 度：顶点关联的边数")
    print("- 入度：箭头指向自己的边数")
    print("- 出度：箭头从自己出发的边数")
    print("- 总入度 = 总出度 = 边数")

    questions = [
        {
            "q": "图G = (V, E)，V表示什么？",
            "answer": "顶点集合",
            "hint": "V = Vertex（顶点），E = Edge（边）"
        },
        {
            "q": "无向图中，顶点的度是什么？",
            "answer": "关联的边数",
            "hint": "比如A连着B和C，A的度就是2"
        },
        {
            "q": "有向图中，入度是什么？",
            "answer": "指向该顶点的边数",
            "hint": "箭头指向自己的边有多少条"
        },
        {
            "q": "有向图中，出度是什么？",
            "answer": "从该顶点出发的边数",
            "hint": "箭头从自己出发的边有多少条"
        },
        {
            "q": "有向图中，所有顶点入度之和等于什么？",
            "answer": "边数",
            "hint": "总入度 = 总出度 = 边数"
        },
        {
            "q": "连通图的定义？",
            "answer": "任意两顶点都有路径相连",
            "hint": "从任意一个顶点都能走到其他所有顶点"
        },
        {
            "q": "强连通图是什么？（有向图）",
            "answer": "任意两顶点双向都有路径",
            "hint": "A能到B，B也能到A，双向可达"
        },
        {
            "q": "无向完全图的定义？",
            "answer": "每两个顶点之间都有边",
            "hint": "所有顶点都互相连接"
        },
        {
            "q": "有向完全图的定义？",
            "answer": "每两个顶点之间都有两条相反方向的边",
            "hint": "A→B和B→A都要有，双向连接"
        },
        {
            "q": "路径的定义？",
            "answer": "从一个顶点到另一个顶点的边序列",
            "hint": "比如A→B→C就是一条路径"
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

    print(f"\n基本概念得分：{score}/10")
    return score


def practice_complete_graph():
    """完全图边数练习"""
    section_header("二、完全图边数计算（10题）⭐重点")

    print("\n【核心公式】")
    print("- 无向完全图：n(n-1)/2 条边")
    print("- 有向完全图：n(n-1) 条边")
    print("- 无向：每对顶点1条边（共享）")
    print("- 有向：每对顶点2条边（双向）")

    questions = [
        {
            "q": "5个顶点的无向完全图有多少条边？",
            "answer": "10",
            "hint": "n(n-1)/2 = 5×4/2 = 10"
        },
        {
            "q": "5个顶点的有向完全图有多少条边？",
            "answer": "20",
            "hint": "n(n-1) = 5×4 = 20"
        },
        {
            "q": "4个顶点的无向完全图有多少条边？",
            "answer": "6",
            "hint": "n(n-1)/2 = 4×3/2 = 6"
        },
        {
            "q": "3个顶点的有向完全图有多少条边？",
            "answer": "6",
            "hint": "n(n-1) = 3×2 = 6"
        },
        {
            "q": "6个顶点的无向完全图有多少条边？",
            "answer": "15",
            "hint": "n(n-1)/2 = 6×5/2 = 15"
        },
        {
            "q": "无向完全图10条边，最少多少个顶点？",
            "answer": "5",
            "hint": "n(n-1)/2 = 10 → n²-n-20=0 → n=5"
        },
        {
            "q": "有向完全图6条边，有多少个顶点？",
            "answer": "3",
            "hint": "n(n-1) = 6 → n²-n-6=0 → n=3"
        },
        {
            "q": "无向完全图边数公式？",
            "answer": "n(n-1)/2",
            "hint": "每对顶点1条边，除以2避免重复计算"
        },
        {
            "q": "有向完全图边数公式？",
            "answer": "n(n-1)",
            "hint": "每对顶点2条边（双向），不除以2"
        },
        {
            "q": "为什么无向图除以2，有向图不除？",
            "answer": "无向边共享，有向边各算各",
            "hint": "无向：A-B和B-A是同一条边。有向：A→B和B→A是两条不同的边"
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\n【第{i}题】⭐" if i <= 6 else f"\n【第{i}题】")
        print(f"题目：{q['q']}")
        user_answer = input("你的答案：").strip()

        if user_answer in q["answer"] or q["answer"] in user_answer:
            print("✅ 正确！")
            score += 1
        else:
            print(f"❌ 错误！正确答案：{q['answer']}")
            print(f"💡 提示：{q['hint']}")

    print(f"\n完全图边数得分：{score}/10")
    return score


def practice_degree():
    """度和入度出度练习"""
    section_header("三、度、入度、出度计算（5题）")

    print("\n【计算规则】")
    print("- 无向图：度 = 连接的边数")
    print("- 有向图：入度（指向自己）+ 出度（从自己出发） = 度")
    print("- 所有顶点的总入度 = 总出度 = 边数")

    questions = [
        {
            "q": "无向图中，某顶点连着3条边，度是多少？",
            "answer": "3",
            "hint": "度 = 关联的边数"
        },
        {
            "q": "有向图中，A有2条入边、1条出边，A的度是多少？",
            "answer": "3",
            "hint": "度 = 入度 + 出度 = 2 + 1 = 3"
        },
        {
            "q": "有向图有10条边，所有顶点入度之和是多少？",
            "answer": "10",
            "hint": "总入度 = 总出度 = 边数"
        },
        {
            "q": "有向图有5个顶点，总度数是20，边数是多少？",
            "answer": "10",
            "hint": "总度数 = 2×边数（因为每条边贡献入度和出度）"
        },
        {
            "q": "无向图有5个顶点，总度数是10，边数是多少？",
            "answer": "5",
            "hint": "总度数 = 2×边数（每条边贡献2个度）"
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\n【第{i}题】")
        print(f"题目：{q['q']}")
        user_answer = input("你的答案：").strip()

        if user_answer == q["answer"]:
            print("✅ 正确！")
            score += 1
        else:
            print(f"❌ 错误！正确答案：{q['answer']}")
            print(f"💡 提示：{q['hint']}")

    print(f"\n度计算得分：{score}/5")
    return score


def practice_storage():
    """存储方式练习"""
    section_header("四、邻接矩阵与邻接表（10题）⭐重点")

    print("\n【核心对比】")
    print("- 邻接矩阵：二维数组，空间O(n²)，判断边O(1)")
    print("- 邻接表：链表数组，空间O(n+e)，遍历邻居O(d)")
    print("- 稠密图用矩阵，稀疏图用表")

    questions = [
        {
            "q": "邻接矩阵的空间复杂度？",
            "answer": "O(n²)",
            "hint": "n×n的二维数组"
        },
        {
            "q": "邻接表的空间复杂度？",
            "answer": "O(n+e)",
            "hint": "n个顶点 + e条边（每条边在两个链表中出现）"
        },
        {
            "q": "邻接矩阵判断边是否存在的时间复杂度？",
            "answer": "O(1)",
            "hint": "直接访问matrix[i][j]"
        },
        {
            "q": "邻接表查找所有邻接点的时间复杂度？",
            "answer": "O(d)",
            "hint": "d是该顶点的度，只遍历存在的邻居"
        },
        {
            "q": "稀疏图用什么存储？",
            "answer": "邻接表",
            "hint": "边少，邻接表节省空间"
        },
        {
            "q": "稠密图用什么存储？",
            "answer": "邻接矩阵",
            "hint": "边多接近n²，矩阵空间利用率高"
        },
        {
            "q": "频繁判断边是否存在，用什么存储？",
            "answer": "邻接矩阵",
            "hint": "O(1)直接访问"
        },
        {
            "q": "频繁遍历邻接点，用什么存储？",
            "answer": "邻接表",
            "hint": "O(d)只访问存在的邻居"
        },
        {
            "q": "邻接矩阵适合什么样的图？",
            "answer": "稠密图",
            "hint": "边多，矩阵空间利用率高"
        },
        {
            "q": "邻接表适合什么样的图？",
            "answer": "稀疏图",
            "hint": "边少，节省空间"
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\n【第{i}题】⭐" if i <= 8 else f"\n【第{i}题】")
        print(f"题目：{q['q']}")
        user_answer = input("你的答案：").strip()

        if user_answer.upper() == q["answer"].upper() or user_answer in q["answer"]:
            print("✅ 正确！")
            score += 1
        else:
            print(f"❌ 错误！正确答案：{q['answer']}")
            print(f"💡 提示：{q['hint']}")

    print(f"\n存储方式得分：{score}/10")
    return score


def practice_adjacency_write():
    """邻接表/矩阵写法练习"""
    section_header("五、邻接表/矩阵写法练习（5题）")

    print("\n【写法要点】")
    print("- 邻接矩阵：1表示有边，0表示无边")
    print("- 邻接表：每个顶点后面挂邻居链表")
    print("- 有向图：只写出边指向的邻居")

    questions = [
        {
            "q": "无向图A-B-C（A连B，B连C），A的邻接表怎么写？",
            "answer": "A→B",
            "hint": "A只有一个邻居B"
        },
        {
            "q": "无向图A-B-C-D（环形），邻接矩阵是几×几？",
            "answer": "4×4",
            "hint": "4个顶点，矩阵大小n×n"
        },
        {
            "q": "有向图A→B→C，B的邻接表怎么写？",
            "answer": "B→C",
            "hint": "B只指向C（只写出边）"
        },
        {
            "q": "无向图的邻接矩阵有什么特点？",
            "answer": "对称",
            "hint": "matrix[i][j] = matrix[j][i]，因为A-B和B-A是同一条边"
        },
        {
            "q": "有向图的邻接矩阵是否对称？",
            "answer": "不对称",
            "hint": "A→B存在但B→A可能不存在"
        }
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\n【第{i}题】")
        print(f"题目：{q['q']}")
        user_answer = input("你的答案：").strip().upper()

        correct = q["answer"].upper()
        if user_answer == correct or correct in user_answer or user_answer in correct:
            print("✅ 正确！")
            score += 1
        else:
            print(f"❌ 错误！正确答案：{q['answer']}")
            print(f"💡 提示：{q['hint']}")

    print(f"\n写法练习得分：{score}/5")
    return score


# ==================== 计算工具 ====================

def graph_edge_calculator():
    """完全图边数计算器"""
    section_header("完全图边数计算工具")

    while True:
        print("\n功能选项：")
        print("1. 计算无向完全图边数")
        print("2. 计算有向完全图边数")
        print("3. 根据边数求顶点数")
        print("0. 返回主菜单")

        choice = input("\n选择功能：").strip()

        if choice == "0":
            break
        elif choice == "1":
            n = int(input("输入顶点数n：").strip())
            edges = undirected_complete_edges(n)
            print(f"\n结果：n(n-1)/2 = {n}×{n-1}/2 = {edges} 条边")
        elif choice == "2":
            n = int(input("输入顶点数n：").strip())
            edges = directed_complete_edges(n)
            print(f"\n结果：n(n-1) = {n}×{n-1} = {edges} 条边")
        elif choice == "3":
            edges = int(input("输入边数：").strip())
            graph_type = input("图类型（无向/有向）：").strip()

            if graph_type in ["无向", "无向图"]:
                # n(n-1)/2 = edges → n² - n - 2edges = 0
                # n = (1 + √(1+8edges)) / 2
                n = int((1 + math.sqrt(1 + 8 * edges)) / 2)
                if undirected_complete_edges(n) == edges:
                    print(f"\n结果：{n} 个顶点")
                else:
                    print(f"\n边数{edges}不是完全图的边数")
            elif graph_type in ["有向", "有向图"]:
                # n(n-1) = edges → n² - n - edges = 0
                # n = (1 + √(1+4edges)) / 2
                n = int((1 + math.sqrt(1 + 4 * edges)) / 2)
                if directed_complete_edges(n) == edges:
                    print(f"\n结果：{n} 个顶点")
                else:
                    print(f"\n边数{edges}不是完全图的边数")


def degree_calculator():
    """度计算工具"""
    section_header("度/入度/出度计算工具")

    while True:
        print("\n功能选项：")
        print("1. 无向图：总度数 → 边数")
        print("2. 无向图：边数 → 总度数")
        print("3. 有向图：边数 → 总入度/总出度")
        print("4. 有向图：入度+出度 → 度")
        print("0. 返回主菜单")

        choice = input("\n选择功能：").strip()

        if choice == "0":
            break
        elif choice == "1":
            total_degree = int(input("输入总度数：").strip())
            edges = total_degree // 2
            print(f"\n边数 = 总度数/2 = {total_degree}/2 = {edges}")
        elif choice == "2":
            edges = int(input("输入边数：").strip())
            total_degree = edges * 2
            print(f"\n总度数 = 边数×2 = {edges}×2 = {total_degree}")
        elif choice == "3":
            edges = int(input("输入边数：").strip())
            print(f"\n总入度 = 总出度 = 边数 = {edges}")
        elif choice == "4":
            in_degree = int(input("输入入度：").strip())
            out_degree = int(input("输入出度：").strip())
            degree = in_degree + out_degree
            print(f"\n度 = 入度 + 出度 = {in_degree} + {out_degree} = {degree}")


def storage_comparison():
    """存储方式对比查看"""
    section_header("邻接矩阵 vs 邻接表 对比")

    print("\n【对比表格】")
    print()
    print("| 特性           | 邻接矩阵       | 邻接表         |")
    print("|---------------|---------------|---------------|")
    print("| 存储方式       | 二维数组       | 链表数组       |")
    print("| 空间复杂度     | O(n²)         | O(n+e)        |")
    print("| 判断边存在     | O(1)          | O(d)          |")
    print("| 查找邻接点     | O(n)          | O(d)          |")
    print("| 适用场景       | 稠密图         | 稀疏图        |")
    print()

    print("【记忆要点】")
    print("- 稀疏图（边少）→ 邻接表（省空间）")
    print("- 稠密图（边多）→ 邻接矩阵（利用率高）")
    print("- 频繁查边 → 矩阵（O(1)直接访问）")
    print("- 频繁遍历 → 邻接表（只访问存在的邻居）")


# ==================== 主菜单 ====================

def main_menu():
    """主菜单"""
    total_score = 0

    while True:
        section_header("04-19 图结构练习系统")

        print("\n【刷题练习】")
        print("1. 基本概念练习（10题）")
        print("2. 完全图边数练习（10题）⭐重点")
        print("3. 度/入度/出度练习（5题）")
        print("4. 邻接矩阵与邻接表（10题）⭐重点")
        print("5. 邻接表/矩阵写法（5题）")
        print("6. 全部练习（40题）")

        print("\n【计算工具】")
        print("7. 完全图边数计算器")
        print("8. 度计算工具")
        print("9. 存储方式对比查看")

        print("\n0. 退出")

        choice = input("\n请选择：").strip()

        if choice == "0":
            print("\n感谢使用！图结构复习加油！💪")
            break
        elif choice == "1":
            total_score += practice_basic_concepts()
        elif choice == "2":
            total_score += practice_complete_graph()
        elif choice == "3":
            total_score += practice_degree()
        elif choice == "4":
            total_score += practice_storage()
        elif choice == "5":
            total_score += practice_adjacency_write()
        elif choice == "6":
            total_score = 0
            total_score += practice_basic_concepts()
            total_score += practice_complete_graph()
            total_score += practice_degree()
            total_score += practice_storage()
            total_score += practice_adjacency_write()
            print(f"\n{'='*50}")
            print(f"  总得分：{total_score}/40")
            print(f"{'='*50}")
        elif choice == "7":
            graph_edge_calculator()
        elif choice == "8":
            degree_calculator()
        elif choice == "9":
            storage_comparison()


if __name__ == "__main__":
    main_menu()