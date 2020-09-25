from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        # 核心思想
        # 后序遍历的数组最后一个元素代表的即为根节点
        # 可以利用已知的根节点信息在中序遍历的数组中找到根节点所在的下标
        # 然后根据其将中序遍历的数组分成左右两部分，左边部分即左子树，右边部分为右子树，
        # 后序遍历中到下标所在元素为左子树，下标到后序遍历长度减1的元素属于右子树
        # 针对每个部分可以用同样的方法继续递归下去构造

        if not postorder:
            return None
        root = TreeNode(postorder[-1])  #  后序遍历的最后一个元素为根节点
        n = inorder.index(root.val)  # 找出在中序遍历中的下标
        root.left = self.buildTree(inorder[:n],postorder[:n])  # 根据中序遍历划分左子树，后序遍历中的前n-1个元素属于左子树
        root.right = self.buildTree(inorder[n+1:],postorder[n:-1])  # 根据中序遍历划分右子树，后序遍历中的n到倒数低2个元素属于右子树
        return root


l1 = [9,3,15,20,7]
l2 = [9,15,7,20,3]

s = Solution()

s.buildTree(l1, l2)