class Solution:
    def isSubsequence1(self, s: str, t: str) -> bool:

        # 核心思想
        # 循环s字符串，判断s字符串中的每一个字符是否在t中
        # 若在t中，返回该字符在t中的下标，并t缩小范围值[ind+1:]
        # 使用tmp记录循环完成后，从t中得到的匹配字符串
        # 若tmp=s则说明可以匹配，否则不能匹配

        tmp = ''
        for i in s:
            ind = t.find(i)
            if ind != -1:
                t = t[ind+1:]
                tmp +=i   
        return tmp == s
        
    def isSubsequence(self, s: str, t: str) -> bool:

        # 核心思想--双指针
        # i指向s的头部，j指向t的头部
        # 当i < n and j < m进行循环
        # 如果s[i] == t[j]，则i向后移动
        # 如果不想等，则j往后移动
        # 最终i==n，则说明完全匹配，返回true

        n, m = len(s), len(t)
        i = j = 0
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == n

