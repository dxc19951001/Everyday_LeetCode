# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # 核心思想--前序遍历
        # 利用递归进行前序遍历，将遍历到的节点放入preorderList中
        # 全部遍历完后，循环preorderList
        # 将每个节点挂载到上一个节点的左子节点中

        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)
        
        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

    def flatten2(self, root: TreeNode) -> None:

        # 核心思想--前序遍历和展开同步进行
        # 将根节点放入stack列表中，设置根节点的前一个为None
        # 每次弹出stack列表中的最后一个元素，并将弹出元素的右节点、左节点依次加入stack中
        # 并设置弹出元素为链表中的前一个节点
        # 进入下一次循环，弹出末尾元素，并将其挂载到前一个节点的右边，循环上述步骤

        if not root:
            return
        
        stack = [root]
        prev = None
        
        while stack:
            curr = stack.pop()
            if prev:
                prev.left = None
                prev.right = curr
            left, right = curr.left, curr.right
            if right:
                stack.append(right)
            if left:
                stack.append(left)
            prev = curr


