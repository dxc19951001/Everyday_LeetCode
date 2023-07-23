class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        # 核心思想：前序遍历
        # 递归参数，根节点，路径参数的和

        # 递归终止条件，节点为空返回False
        # 即循环到最后一个子节点都没有找到
        if not root:
            return False

        # 单层递归
        # 中
        # 当没有左节点和右节点，即叶子节点时，判断路径上数字的和 与 目标值是否相等
        if not root.left and not root.right:
            return sum == root.val

        # 向左右子树进行递归时，传入左节点或右节点，同目标值减去当前节点的值
        bool_left = self.hasPathSum(root.left, sum - root.val)  # 左
        bool_right = self.hasPathSum(root.right, sum - root.val)  # 右

        # 判断在 左子树 或 右子树上是否有满足目标值的和
        return bool_left or bool_right

