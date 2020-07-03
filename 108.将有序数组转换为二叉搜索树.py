# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        # 核心思想
        # 每次对列表长度除以2向下取整
        # 则列表为基数个时取到中间的数，列表为偶数个时取到中间靠左的数
        # 运用递归，依次将分开的左半边和右半边挂载到左子树和右子数上    

        if not nums:
            return None
        else:
            mid=len(nums)//2
            tn=TreeNode(nums[mid])
            nums1=nums[0:mid]
            nums2=nums[mid+1:len(nums)]
            tn.left=self.sortedArrayToBST(nums1)
            tn.right=self.sortedArrayToBST(nums2)
        return tn