from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # 核心思想--回溯（本题回溯经典例题）
        # 回溯的要点
        #   选择，选择决定了我们的搜索空间，决定了我们搜索空间有哪些节点。
        #   约束，约束条件用来剪枝，直接不让它进入某些无效的分支。
        #   目标，目标决定了我们什么时候捕获有效的解，并提前回溯，避免继续递归。
        # 本题图解参考：https://leetcode-cn.com/problems/n-queens/solution/shou-hua-tu-jie-cong-jing-dian-de-nhuang-hou-wen-t/
        # 依次枚举Q可能在的位置，如果发现合适则及时回溯，不需要在提前递归下去

        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"  # 找出该行Q所在位置，并赋值为"Q"
                board.append("".join(row))  # 将其追加到board中
                row[queens[i]] = "."  # 将row还原，方便进入下一行添加Q所在位置
            return board

        def backtrack(row: int):
            if row == n:
                # 如果搜索到最后，已搜索行数 == n，则说明已经找到正确的解
                board = generateBoard()  # 返回正确解的列表
                solutions.append(board)
            else:
                # 否则则进行搜索
                for i in range(n):
                    # 让Q在一行中的每个位置上进行搜索（即一行中的每一列）
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        # 如果在列、左对角线、右对角线上存在Q，则下一个Q不能放在此位置
                        continue  # 直接跳出本次循环，不用进入递归搜索
                    
                    queens[row] = i  # 记录在第row行的第i个位置设置为Q 
                    columns.add(i)  # 将Q所在的列的位置添加到columns中
                    
                    diagonal1.add(row - i)  
                    # 方向一的斜线为从左上到右下方向，同一条斜线上的每个位置满足行下标与列下标之差相等，
                    # 例如 (0,0)(0,0) 和 (3,3)(3,3) 在同一条方向一的斜线上。
                    # 因此使用行下标与列下标之差即可明确表示每一条方向一的斜线。
                    
                    diagonal2.add(row + i)
                    # 方向二的斜线为从右上到左下方向，同一条斜线上的每个位置满足行下标与列下标之和相等，
                    # 例如 (3,0)(3,0) 和 (1,2)(1,2) 在同一条方向二的斜线上。
                    # 因此使用行下标与列下标之和即可明确表示每一条方向二的斜线。

                    backtrack(row + 1)  # 确定好这行的位置，进入递归搜索下一行的位置

                    # 如果进入下一行后，发现没有合适放置Q的位置，则进行回溯
                    columns.remove(i)  # 去除列上的判条件
                    diagonal1.remove(row - i)  # 去除左对角线上的判断条件
                    diagonal2.remove(row + i)  # 去除右对角线上的判断条件
                    
        solutions = list()  # 返回的答案
        queens = [-1] * n   # 记录每一行Q在的位置
        columns = set()     # 记录已经在的列
        diagonal1 = set()   # 记录Q已经在的左斜对角
        diagonal2 = set()   # 记录Q已在的右斜对角
        row = ["."] * n     # 用于设定每一行的情况（包括Q和.）
        backtrack(0)        # 从第0个开始搜索
        return solutions

