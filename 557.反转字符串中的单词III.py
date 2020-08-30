class Solution:
    def reverseWords(self, s: str) -> str:

        # 核心思想
        # 分割字符串，对每个字符串倒序后拼接

        tmp = s.split()
        ans = str()
        for i in tmp:
            ans += i[::-1] + ' '
        
        return ans[:-1]