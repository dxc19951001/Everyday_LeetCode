from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 核心思想--dfs
        # 由题：任何边界上的 'O' 都不会被填充为 'X'。 
        # 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。
        # 可以理解为：边界上的O不会被填充为X，与边界上的O相连的O也不会填充为X
        # 找出边界：第一行与最后一行，第一列与最后一列上的O
        # 并使用dfs搜索，找出边界上的O相连的O，将其标记为 A
        # 全部找完后，最后循环列表，将标记为A的的O设置为O，
        # 没有标记的O全部设为X，得到结果 

        if not board:
            # 如果没有board直接返回
            return
        
        n, m = len(board), len(board[0])  # n是行，m是列

        def dfs(x, y):
            # 使用dfs搜索，找出所有与边界O相连的O
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                # 递归出口：dfs搜索范围不超过n*m
                # 且搜索的点如果不是O（以标记的A 或 X就不用再去标记）
                return
            
            board[x][y] = "A"  # 将于边界相连的O进行标记
            # 每个点的上下左右四个方向
            dfs(x + 1, y) 
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        
        for i in range(n):
            # 第一行和最后一行
            dfs(i, 0)
            dfs(i, m - 1)
        
        for i in range(m - 1):
            # 第一列和最后一列
            dfs(0, i)
            dfs(n - 1, i)
        
        # 标记完成后，对所有已标记为A的点设置为0，其他未标记的O设置为X
        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

    
    def solve2(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # 核心思想--类似的解法，dfs不同实现，可以快10ms左右

        if not board:
            return
        row = len(board)
        col = len(board[0])

        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1),(0,0)]:
                tmp_i = i + x
                tmp_j = j + y
                if 1 <= tmp_i < row and 1 <= tmp_j < col and board[tmp_i][tmp_j] == "O":
                    dfs(tmp_i, tmp_j)

        for j in range(col):
            # 第一行
            if board[0][j] == "O":
                dfs(0, j)
            # 最后一行
            if board[row - 1][j] == "O":
                dfs(row - 1, j)

        for i in range(row):
            # 第一列
            if board[i][0] == "O":
                dfs(i, 0)
            # 最后一列
            if board[i][col-1] == "O":
                dfs(i, col - 1)

        for i in range(row):
            for j in range(col):
                # O 变成 X
                if board[i][j] == "O":
                    board[i][j] = "X"
                # B 变成 O
                if board[i][j] == "B":
                    board[i][j] = "O"