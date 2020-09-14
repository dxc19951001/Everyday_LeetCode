from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        # 核心思想--中序遍历不忘“左链入栈”
        # 中序遍历 左 --> 中 --> 右
        # 先通过循环一直循环到左子树的左叶子节点，并依次将左节点加入到stack中
        # 将stack中的最后一个节点弹出，并将该节点加入到res中，再看有没有该节点有没有右节点
        # 有则加入到stack中
        # 循环往复，直至遍历完成

        stack = list()
        res = list()
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root= stack.pop()
            res.append(root.val)
            root = root.right
        return res
    
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        # 核心思想--递归
        # res依次加入左节点，父节点和右节点
        res = []
        if not root: return []
        def dfs(root):
            if root.left:
                dfs(root.left)
            res.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        return res