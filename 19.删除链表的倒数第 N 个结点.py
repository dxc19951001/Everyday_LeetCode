# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 19.删除链表的倒数第 N 个结点.py
    @date：2023/1/12 16:56
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    # 核心思想：双指针
    # slow指针指向当前节点，fast指针指向当前节点的后n个节点
    # 当fast.next指针指向空时，表明此时找到了要删除节点的上一个一个节点
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head

        for i in range(n):
            if fast.next:
                fast = fast.next
            else:
                # 如果没有fast.next节点，表明要删除的时头节点
                return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return head