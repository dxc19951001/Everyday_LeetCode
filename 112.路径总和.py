class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        # 核心思想
        # 递归
        # 每次递归传入左节点或右节点，并传入sum = sum - root.val
        # 只要左节点或右节点其中一个返回true，则返回true
        # 若计算到当前节点为叶子节点时（叶子节点是指没有子节点的节点，即当前节点没有左节点和右节点）
        # 剩下的sum == 当前节点节点的值，则返回True，否则返回false
        # 若递归至非叶子节点，但其左节点或右节点为空时，空节部分点直接返回false，
        # 因为题目要求的路径是：根节点到叶子节点的路径

        if not root:
            return False
        if sum < 0:
            return False
        if not root.left and not root.right:
            return sum == root.val
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

