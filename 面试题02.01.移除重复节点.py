# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # 核心思想：
        # 设置两个指针
        # pre指向当前节点，cur指向当前节点的下一个节点
        # 设置一个set用来存储每个节点的val值，set初始值为head.val
        # 利用set不重复的特性，
        # 当cur.val的值存在于set中时
        #   当前节点的下个节点为下一个节点的下一个节点，即pre.next = cur.next
        #   cur向后移动至下一个节点，即cur = cur.next
        # 当cur.val的值没有在set中时
        #   将cur.val值添加至set中，并将当前节点向后移动，即pre.next = cur
        #   cur向后移动至下一个节点，即cur = cur.next
        # 当cur为None时，结束循环

        if not head:
            return head
        pre, cur = head, head.next
        rec = {pre.val}
        print(rec)
        while cur:
            if cur.val in rec:
                pre.next = cur.next
            else:    
                rec.add(cur.val)    
                pre = cur 
            cur = cur.next 
        return head 