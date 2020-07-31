from typing import List

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        ans = list()
        tmp = list()
        for i in nums:
            if i%2 != 0:
                ans.append(i)
            else:
                tmp.append(i)

        ans.extend(tmp)
        return ans