from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        # 核心思想--dfs
        # 构建dfs函数进行搜索，如果搜索到叶子节点就将答案放到res中
        # 最终返回res

        if not root:
            # 如果没有root，直接返回空
            return []
            
        def dfs(root, path):
            # 构建dfs函数，有两个参数，一个是root，一个是已搜索的路径
            if root:
                path += str(root.val)  # 已搜索路径加上当前搜索节点的值
                if not root.left and not root.right:
                    # 如果当前节点为叶子节点，将已搜索完成的path加入到res中
                    res.append(path)
                else:
                    # 否则对左子节点和右子节点展开递归搜索，进行深度搜索
                    path += '->' 
                    dfs(root.left, path)
                    dfs(root.right, path)

        res = []
        dfs(root, '')
        return res