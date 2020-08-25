from typing import List 

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        # 核心思想--递归
        # 将nums拆分成两部分，now--当前部分，last--剩余部分
        # 当len(now) >= 2 时，则放入ans列表中
        # 例如[4,6,7,7]
        # now  last
        # 4    677
        # 46   77 （这里加入now的是第一个7）
        # 467  7  
        # 4677 none
        # 467  none （退栈，到第2个7，这里加入now的是第二个7）
        # 47   7
        # 477  none
        # 依次类推，最后去重

        ans = []

        def find(now, last):
            if len(now) >= 2:
                ans.append(now)
            base = now[-1]  # 当前部分最后一位值的大小
            for i in range(len(last)):
                if last[i] >= base:  # 只有比base大才可以放入列表中
                    find(now+[last[i]],last[i+1:])  # 将当前部分+新的元素，剩余部分，进行递归

        for i in range(len(nums)-1):
            find([nums[i]], nums[i+1:])

        return list(set([tuple(i) for i in ans]))  # 存在重复问题，先讲list转为tuple，利用set去重后，再转换为list            