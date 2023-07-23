# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # 核心思想--后序遍历 左右中
        # 通过后序遍历判断两颗树的左节点和右节点的是否相等
        # 如果相等则相似返回到中节点

        # 递归参数：
        # p树的左节点，q树的左节点
        # p树的右节点，q树的右节点
        # 返回值：左节点和右节点进行布尔判断，都相等返回True

        # 递归终止条件
        # p为空，q不为空，返回F
        # p不为空，q为空，返回T
        # p和q都为空，返回T
        # p和q的值不想等返回F
        # 如果p和q值相等则继续想想下执行

        if p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        elif p is None and q is None:
            return True
        elif p.val != q.val:
            return False

        # 单层递归，分别对p和q的左右、节点进行判断
        bool_left = self.isSameTree(p.left, q.left)
        bool_right = self.isSameTree(p.right, q.right)
        # 返回到中间节点是左节点和右节点的布尔值
        return bool_left and bool_right
