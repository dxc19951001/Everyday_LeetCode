from typing import List
# 核心思想
# 分类讨论
# 先对列表进行排序

# 1.sum(arr) <= target
#   即数组之和小于等于目标值，此时返回的数值应尽可能地大来向目标值靠近，因此返回最大的max(arr)；

# 2.平均值小于等于数组arr的最小值，min(arr) >= average
#   此时可以直接返回平均值average即可

# 3.平均值大于数组arr的最大值，max(arr) < average
#   此时直接返回max(arr)即可

# 4.平均值大于arr的最小值，小于等于arr的最大值时，max(arr)>= average > min(arr)
#   此时的目标值target计算公式为：target = sum[:i+1] + average * (len(arr) - i -1)，
#   显然我们需要计算的就是average的数值，移项后得到average的计算公式为：average=(target - summ)/(len(arr)- i - 1)，
#   我们对原数组arr进行排序后进行前序遍历，停止条件为：arr[i+1]> average >= arr[i]，
#   即所得average数值应只能大于当前遍历元素但必须小于下一个遍历元素，由于取最接近average四舍五入


class Solution(object):
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        if sum(arr) <= target:
            return max(arr)
        average = round(target / len(arr))
        if average <= min(arr):
            return average
        elif average > max(arr):
            return max(arr)
        else:
            for i in range(len(arr)):
                average = (target - sum(arr[:i+1]))/(len(arr)- i - 1)
                if arr[i+1]> average >= arr[i]:
                    return round(average)
