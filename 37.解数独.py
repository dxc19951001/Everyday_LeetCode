from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 核心思想--回溯
        # 找出每一行、每一列、每一块中，在1-9中剩下的元素，
        # 并记所需要填写位置的坐标
        # 依次从行、列、块剩余的值中，选择数字填入需要填写的位置中
        # 如果填写过程中发现不合适，无法满足要求，则进行回溯，填写下一个值
        # 直到求出结果

        row = [set(range(1, 10)) for _ in range(9)]  # 行剩余可用数字
        col = [set(range(1, 10)) for _ in range(9)]  # 列剩余可用数字
        block = [set(range(1, 10)) for _ in range(9)]  # 块剩余可用数字

        empty = []  # 收集需填数位置
        for i in range(9):  # 循环列
            for j in range(9):  # 循环行
                if board[i][j] != '.':  # 更新可用数字，取除列、行、块中以用过的值
                    val = int(board[i][j])  
                    row[i].remove(val)  # 将该列中的此值去除
                    col[j].remove(val)  # 将该行中的此值去除
                    block[(i // 3)*3 + j // 3].remove(val)  # 将该块中的此值去除
                else:
                    empty.append((i, j))  # 将剩余可用位置加入到empty中

        def backtrack(iter=0):
            if iter == len(empty):  # 处理完empty代表找到了答案
                return True
            i, j = empty[iter]  # 将empty中第一个空缺需要填写的列、行赋值给i，j
            b = (i // 3)*3 + j // 3  # 由行列坐标推出所在块的位置
            for val in row[i] & col[j] & block[b]:
                # val是要在列剩余可用数字、行剩余可用数字、块剩余可用数字中都存在的
                # 对每个数字进行循环，先假设该数字就是解，将其在列、行、块中删除，并加入board中
                row[i].remove(val)
                col[j].remove(val)
                block[b].remove(val)
                board[i][j] = str(val)                
                if backtrack(iter+1):
                    # 进行递归，进入empty中记录的下一个位置，重复上述步骤
                    return True  # 如果最终返回true则表示找到了答案
                
                # 如果此值不合适，重新将该值加回到行、列、块中
                # 进行回溯，for循环进入下一个值
                row[i].add(val)
                col[j].add(val)
                block[b].add(val)
            return False  # 如果选择该val的情况下，无法得出答案，则返回false
        backtrack()
