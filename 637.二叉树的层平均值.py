from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:

        # 核心思想--BFS

        res = list()  # 返回的结果
        queue = [root]  # 构建BFS队列

        if not root:
            return res

        while queue:
            # 进行BFS
            level = list()  # 记录该层每个数得值
            n = len(queue)  # 记录该层有几个数
            for _ in range(n):
                # 进行循环，将下一层的节点放入queue中国
                node = queue.pop(0)  # 弹出一个节点
                level.append(node.val)  # level中加入该点值
                if node.left:
                    queue.append(node.left)  # 若该点有左子节点，则放入queue中
                if node.right:
                    queue.append(node.right)  # 若该点有右子节点，则放入queue中
            res.append(sum(level) / n)  # res中加入该层的平均值
        
        return res