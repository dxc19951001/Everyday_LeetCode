class Solution:
    def spiralOrder(self, matrix:[[int]]) -> [int]:
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            # 左-->右
            for i in range(l, r + 1): 
                res.append(matrix[t][i]) # left to right
            t += 1
            if t > b: break
            
            # 上-->下
            for i in range(t, b + 1): 
                res.append(matrix[i][r]) # top to bottom
            r -= 1
            if l > r: break
            
            # 右-->左
            for i in range(r, l - 1, -1): 
                res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: break
            
            # 下-->上
            for i in range(b, t - 1, -1): 
                res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res

        def spiralOrder_1(self, matrix: List[List[int]]) -> List[int]:
            ans = []
            while matrix:
                ans.extend(matrix[0])
                matrix = list(zip(* matrix[1:]))[::-1]
            return ans