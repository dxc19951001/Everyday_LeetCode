# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # 核心思想--DFS
        # 分别对两棵树的左子树和右子树进行递归，可能出现四种情况
        # 1.当递归到都为空节点时，则返回true
        # 2.当一个树有值而另一棵树没有值得情况，返回false
        # 3.当两颗数都有值，但值不相等，返回false
        # 4.其他情况，则进入下一次递归，当两颗树的左子树和右子树相等时返回true

        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
