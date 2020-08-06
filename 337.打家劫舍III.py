# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:

        # 核心思想--递归求解
        # 对于树中的每个节点分成偷与不偷
        #   1.偷该节点，则不能偷与之相连的左子树和右子树
        #   2.不偷该节点，则可以偷左子树和右子树中的最大值
        

        def _rob(root):
            # 设定低估函数
            
            if not root: 
                # 递归出口
                return 0, 0  # 返回一个元组，第一个表示偷该节点，第二个表示不偷该节点

            left = _rob(root.left)  # 该节点左子树返回，偷与不偷情况下的最大值
            right = _rob(root.right)  # 该节点右子树返回，偷与不偷情况下的最大值

            # 偷当前节点, 则左右子树都不能偷
            v1 = root.val + left[1] + right[1]  # 当前节点的值加上，左右子树都不偷情况下的值

            # 不偷当前节点, 则取左右子树中最大的值
            v2 = max(left) + max(right)  # 左子树的最大值加上右子树的最大值
            return v1, v2

        return max(_rob(root))  # 最终返回两种情况下的最大值

