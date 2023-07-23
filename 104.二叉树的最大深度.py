# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root):

        # 核心思想--后序遍历（左右中
        # 分别递归左子树和右子树，每次递归一层，
        # 返回左子树或右子树最大的深度，并加上本层的深度1
        # 递归出口：当递归到右子节点时，返回0

        # 递归出口，如果没有节点了则返回0
        if root is None: 
            return 0

        # 左边节点的最大高度
        left_height = self.maxDepth(root.left)
        # 右边边节点的最大高度
        right_height = self.maxDepth(root.right)
        # 中间节点是除处理过程，左边边和右边子节点的最大高度+1，为当前中间节点的高度
        depth = max(left_height, right_height) + 1
        return depth

    def maxDepth2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS方法
        # 每一层遍历完以后计数+1

        if not root:
            return 0

        queue = [root]
        coun = 0

        while len(queue):

            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
            coun += 1

        return coun