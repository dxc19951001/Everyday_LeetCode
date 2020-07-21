from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
     def generateTrees(self, n: int) -> List[TreeNode]:
        
        # 核心思想
        # 递归求解
        # 与95题不同，95题无需关注数字，只关心序列长度
        # 本体需要关注序列的起始于终止范围
        # 设定一个helper函数，传入初始start和end值，即[1, n]
        # 依次取[start, end]中的值i作为根节点
        # 则左节点的范围是leftTrees = helper(start, i - 1)
        # 则右节点的范围是rightTrees = helper(i + 1, end)
        # 们递归调用这两部分，获得所有可行的左子树和可行的右子树，
        # 那么最后一步我们只要从可行左子树集合中选一棵，再从可行右子树集合中选一棵拼接到根节点上，
        # 并将生成的二叉搜索树放入答案数组即可。

        # 当start > end时，无法满足二插树条件：右子树要比左子树小，则说明无法再进行划分，
        # 注意要返回一个可迭代对象[None]


        
        def helper(start, end):
            allTrees = []
            
            if start > end:
                return [None]            
            
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = helper(start, i - 1)
                
                # 获得所有可行的右子树集合
                rightTrees = helper(i + 1, end)
                
                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)
            
            return allTrees  # 返回allTrees，就是返回该节点下的所有子树集合
        
        return helper(1, n) if n else []