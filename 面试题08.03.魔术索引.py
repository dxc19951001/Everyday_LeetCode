from typing import List

class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in nums:
            if nums[i] == i:
                return i
        return -1