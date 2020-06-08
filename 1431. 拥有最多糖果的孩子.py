from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # 核心：第i个孩子拿来全部的额外糖果后所拥有的糖果数目，大余最大所有孩子中拥有最大糖果数
        
        maxCandies = max(candies)
        ret = [candy + extraCandies >= maxCandies for candy in candies]
        return ret
