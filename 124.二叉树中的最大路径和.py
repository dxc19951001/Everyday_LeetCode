# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        # 核心思想:
        # 递归
        # 每个节点面临三个选择
        # 1.停下不走 2.走到左子节点 3.走到右子节点
        # 注意：不能走进一个分支，又掉头走另一个分支——路径重叠，不符合要求
        #       走到子节点，又会面临三个选择，可以选择停下，或延伸进子树里

        # 子树向父子书提供路径最大值
        # 父节点，关心走入一个子树的最大收益，不关心具体路径细节
        # 定义 dfs 函数，计算当前子树能向父节点提供的最大路径和
        # 当前子树的左节点和右子节点会递归调用 dfs 函数，
        # 对从父节点延伸下来的路径，有三种选择
        #   1.走入左子树，收益：root.val + dfs(root.left)
        #   2.走入右子树，收益：root.val + dfs(root.right)
        #   3.停在当前子树的根节点，收益：root.val
        # 递归出口：遇到 null 节点，向上返回 0（代表此处收益为 0）

        # 负数情况的处理
        # 如果某个子树向上提供的最大路径和为负，路径走入它的话，收益不增反减
        # 我们希望这个分支成为死支，封死，于是我们让它返回 0

        # 树中的路径，可以从右子树 到 父节点 再到 左子树
        # 题目说，路径不一定经过根节点，意味着，最大路径和可能在局部子树中产生
        # 所以 dfs 求每个子树对父节点提供的最大路径和时，都要求当前子树的最大路径和
        # 设置一个全局变量 maxSum ，每次计算当前子树的最大路径和是，若比 maxSum 大，则更新
        # 子树中的最大路径和 = 左子树提供的最大路径和 + 根节点值 + 右子树提供的最大路径和
        # 相当于从根节点开始，对每棵子树都有进行了计算，找出最大的子树
        
        self.maxVal = root.val  # 设置全局变量
        def dfs( root ):
            if not root:  # 递归出口
                return 0
            left = max( 0, dfs( root.left ) )  # 若左子树节点为负数，返回0
            right = max( 0, dfs( root.right ) )  # 若右子树节点为负数，返回0
            self.maxVal = max( self.maxVal,  root.val + left + right )  # 计算每颗子树的路径和，并与maxVal比较
            return root.val + max( left, right )  # 返回当前子树能向父节点提供的最大路径和
        dfs(root)
        return self.maxVal
        