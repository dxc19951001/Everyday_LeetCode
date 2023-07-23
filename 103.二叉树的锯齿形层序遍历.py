# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 103.二叉树的锯齿形层序遍历.py
    @date：2022/12/20 16:26
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 使用BFS思路求解
        # 使用队列，将节点加入后，先进先出

        if not root:
            return root

        queue = []  # 设定BFS队列
        result = []  # 返回的结果列表
        queue.append(root)  # 队列中加入头节点
        count = 1  # 记录层数，基数词正序，偶数层逆序

        while len(queue) > 0:
            list_tmp = [node.val for node in queue]
            if count % 2:
                result.append(list_tmp)
            else:
                result.append(list_tmp[::-1])

            # 可简化为 result.append(list_tmp) if count%2 else result.append(list_tmp[::-1])

            # 临时存放下一层的所有节点
            tmp = []
            # 循环当前层的所有节点
            for node in queue:
                # 如果左子节点存在，入队列
                if node.left:
                    tmp.append(node.left)
                # 如果右子节点存在，入队列
                if node.right:
                    tmp.append(node.right)
            # 当前节点全部循环完成后，则进入下一层
            queue = tmp
            count += 1
        return result
