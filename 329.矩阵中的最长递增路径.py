from typing import List
from functools import lru_cache

class Solution:

    # 核心思想--深度优先搜索
    # 从一个单元格开始进行深度优先搜索，即可找到从该单元格开始的最长递增路径。
    # 例如当前元素[i][j]的上下左右中有元素比当前元素大，则计算往各方向进行深度搜索时，所能得到的路径长度
    # 最终取往各个方向中路径长度最长的值，为[i][j]元素的值
    # 依次类推，对每个单元格分别进行深度优先搜索之后，即可得到矩阵中的最长递增路径的长度。
    
    # 但是如果使用朴素深度优先搜索，时间复杂度是指数级，会超出时间限制，因此必须加以优化。
    # 朴素深度优先搜索的时间复杂度过高的原因是进行了大量的重复计算，同一个单元格会被访问多次，每次访问都要重新计算。
    # 由于同一个单元格对应的最长递增路径的长度是固定不变的，因此可以使用记忆化的方法进行优化。
    # 用矩阵memo 作为缓存矩阵，已经计算过的单元格的结果存储到缓存矩阵中。

    # 使用记忆化深度优先搜索，当访问到一个单元格 (i,j)时，
    # 如果memo[i][j] = 0 ，说明该单元格的结果已经计算过，则直接从缓存中读取结果，
    # 如果memo[i][j]=0，说明该单元格的结果尚未被计算过，则进行搜索，并将计算得到的结果存入缓存中。
    # 在python中可以使用@lru_cache(None)这个装饰器来实现

    # 遍历完矩阵中的所有单元格之后，即可得到矩阵中的最长递增路径的长度。


    def __init__(self):
        self.DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 设定一个使得当前点往上下左右方向移动的列表

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            # 当matrix为空，直接返回0
            return 0
        
        @lru_cache(None)  # 设定缓存，实现记忆搜索
        def dfs(row: int, column: int) -> int:
            # 设定dfs搜索函数
            best = 1  # 由于每个点自身可以为一个长度，所以初始路径长度设为1
            for dx, dy in self.DIRS:
                # 循环DIRS，一次循环，计算向一个方向所能得到的最长路径
                newRow, newColumn = row + dx, column + dy  # 使得当前点可以上下左右移动
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    # 如果当前点移动超过了matrix范围则不能取，比当前点的值小不能取
                    best = max(best, dfs(newRow, newColumn) + 1)  # 进行递归，并且对每次递归进行比较，得到该点最长的路径
                    # dfs(newRow, newColumn)需要加 1，是因为要加上当前点的长度1
            return best  # 返回该点的路径

        ans = 0  # 设定总体最初路径为0
        rows, columns = len(matrix), len(matrix[0])
        # 循环每一matrix中的每一个点
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))  # 对该点进行dfs搜索，并比较每个点的最长路径，挑战当前ans，如果大于当前ans则更新
        return ans
