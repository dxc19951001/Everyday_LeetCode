
 # 暴力扫描
class Solution(object):
    def dailyTemperatures_1(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 核心思想:
        # 对列表中的每个元素找到比其大的第一个数
        # 注意边界，若找到结束也没有找到，则返回0
        # 采用俩个for循环，
        # 里面的for循环，从i+1到最后，去寻找第一个比当前数字大的数字
        # 缺点:时间复杂度O(n**n)和空间复杂度O(n)极高
        # 跑测试用例超出时间限制
        
        n = len(T)
        ans = [0] * n
        for i in range(n):
            a = 0    
            for k in range(i+1, n):
                if T[i] < T[k]:
                    a +=1   
                    break
                elif T[i] >= T[k]:
                    a +=1
                    if k == n-1:
                        # 找到列表结束也没找到
                        # 返回0
                        a =0                
            ans[i] = a
        return ans
    
    # 从后向前循环解法
    def dailyTemperatures_2(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 核心思想：
        # 根据题意，我们需要得到当前温度T[i]，在过几天可得到比T[i]大的数
        # 可以理解为：仅从第二天温度T[i+1]到最后一个温度之间，找到比T[i]大的数
        # 那么可以对T从后向前循环，每次循环将温度作为key，索引作为val，添加到一个字典dic中
        # 这样每次循环，dic只包含当前温度到最后一个温度
        
        # 由题可知温度在[30, 100]，若当前温度为T[i]，
        # 则我们需要找到温度为[T[i]+1, 100]，即温度比T[i]大的，且在dic中存在的
        # 找出所有满足要求的温度，将其索引依次与当前温度T[i]索引向减，取出最小值
        # 若没有满足要求的，直接返回0

        dic = dict()
        ans = [0] * len(T)
        for i in range(len(T) - 1, -1, -1): 
            # 从后向前遍历
            dic[T[i]] = i  
            # 记录当前温度
            tmp = [dic[t] - i for t in range(T[i] + 1, 101) if t in dic]
            # 找出比T[i]大且在dic存的全部温度的索引，求出与T[i]索引的差，即相差天数
            ans[i] = (min(tmp) if tmp else 0)
            # 得到最小的相差天生，若tmp不存在说明没有找到，直接返回0
        return ans

    # 单调栈
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 核心思想：
        # 设置一个单调栈stack
        # 当栈为空，或者当日温度小于等于栈顶温度，则直接入栈
        # 若当日温度大于栈顶温度，说明栈顶元素的升温日已经找到了，
        # 则将栈顶元素出栈，计算其与当日相差的天数即可。
        # 注意放入栈中的元素为温度的索引

        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans




s = Solution()
temperatures = [89,62,70,58,47,47,46,76,100,70]
a = s.dailyTemperatures(temperatures)

print(a)
