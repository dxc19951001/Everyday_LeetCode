# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 513.找树左下角的值.py
    @date：2022/12/23 19:36
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # 使用BFS层序遍历的方式，找到最后一排的第一个元素

    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return root

        queue = [root]
        result = None

        while len(queue):
            result = queue[0].val
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp

        return result