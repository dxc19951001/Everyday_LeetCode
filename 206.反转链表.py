# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 206.反转链表.py
    @date：2022/12/19 23:04
"""


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 两个节点，re和 cur，pre为当前节点的前一个节点，cur指向当前节点
        pre = None  # 初始为None
        cur = head  # 初始为head
        while cur:
            # 保存当前节点的下一个节点
            tmp = cur.next
            # 将当前节点的下一个节点只向pre
            cur.next = pre
            # pre向后移动，指向当前节点
            pre = cur
            # cur向后移动，指向下一个节点
            cur = tmp
        return pre
