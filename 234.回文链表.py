# coding=utf-8
"""
    @project: Everyday_LeetCode
    @Author：Charles
    @file： 234.回文链表.py
    @date：2023/1/13 23:27
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 遍历链表节点放到list中，再判断record == record[::-1]

        cur = head
        record = []

        while cur:
            record.append(cur.val)
            cur = cur.next

        return record == record[::-1]