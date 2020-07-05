class Solution:
    def longestValidParentheses1(self, s: str) -> int:

        # 核心思想
        # 运用栈来解决
        # 入栈的元素是字符串对应的下标
        # 当遇到"("时，将"("的下标入栈
        # 当遇到")"时，将栈顶元素"("下标出栈，并计算")"下标与此时栈顶元素的差值，
        # 此值为有效括号的子串的长度，每次计算更新最大值

        # 此题中将栈stack的栈底元素-1,stack=[-1]，因为字符串下标从0开始，长度计算应该+1
        # 例如字符串为"()"，
        #   1."("入栈,stack=[-1,0]；
        #   2.")"，将离其最近的"("下标出栈，stack=[-1]
        #       并计算")"下标与此时栈顶元素的差值，1-(-1) = 2
        # 结果为2，因此为保证这种情况，所以stack初始元素为-1

        # 当遇到")"时，对stack栈顶元素出栈，若此时stack为空，则将")"下标入栈
        # 相当于将-1出栈，")"的下标为栈底元素
        # 例如")()"
        # 1.")",stack栈顶元素出栈，即-1出栈，将")"入栈，stack=[0]
        # 2."("入栈,stack=[0,1]；
        # 3.")"，将离其最近的"("下标出栈，stack=[0]
        #       并计算")"下标与此时栈顶元素的差值，2-0 = 2
        # 结果为2

        maxnum = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                if stack:
                    maxnum = max(maxnum, i - stack[-1])
        return maxnum

    def longestValidParentheses2(self, s: str) -> int:

        # 核心思想
        # 动态规划
        # 构建一个全为0，长度为n=len(s)的dp列表
        # 括号的结尾必然是')'，所以'('的dp值保持为0不变，我们对'('的dp值进行讨论
        # 当s[i]为')'时，要找到其前一个与之匹配的'('的位置,找到后dp[i]基础长度为2
        # 若dp[i-1]有值，说明dp[i]的')'到与之匹配的'('之间，存在有效的子串
        # 所以将这段有效的子串减去，并再去1，即可找到应该与s[i]匹配的'('位置
        # 即判断s[i-dp[i-1]-1]是否为'('，若为'('，则dp[i]的基础长度为2,dp[i] = 2
        # 判断完基础长度，再s[i-dp[i-1]-1, i]内部的子串长度，即为dp[i-1]的值
        # 此时dp[i] = 2 + dp[i-1]
        # 内部判断完后，再判断外部，s[i-dp[i-1]-1, i]的外部的位置为i-dp[i-1]-2
        # 则dp=dp[i-1]+2+dp[i-dp[i-1]-2]，即基础长度+内部子串长度+外部子串长度

        # 由于地推公式中会出先dp[-1]的情况，即找到s的最后一个元素
        # 例如'())('，显然不是对的，根据上述推导
        # i=0
        # dp[0] = 0;
        # i=1，s[1]=')' and s[i-dp[i-1]-1] = s[1-dp[0]-1]=s[0]='('
        # 执行：dp[1] = dp[0]+2+dp[1-dp[0]-2]=0+2+dp[-1]=2
        # i=2，s[2]=')' and s[i-dp[i-1]-1] = s[2-dp[1]-1]=s[-1]='('
        # 执行：dp[2] = dp[1]+2+dp[2-dp[1]-2]=4;
        # 显然这里出错了，2号位的')'于末尾的'('进行了匹配，构成了括号
        # 所以用i-dp[i-1]-1去找')'对应的'('时，不能为负数，所以i-dp[i-1]-1>=0

        # 因此进入递推公式的条件为s[i] == ')' and i-dp[i-1]-1 >=0 and s[i-dp[i-1]-1] == '(':

        n = len(s)
        if n == 0:
            return 0
        dp = [0]*n
        for i in range(len(s)):
            if s[i] == ')' and i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2
        return max(dp)
   
    def longestValidParentheses(self, s: str) -> int: 
        
        # 核心思想
        # 正序遍历与反序遍历，巧妙解法，不具有通用性
        # 正序遍历s，
        # 遇到'('，left +=1
        # 遇到')'，right +=1
        # 当left == right 时，maxlength=2*right
        # 每次left == right，取maxlength这次于上次的最大值
        # 当出现right>left时，说明此时的')'位置之前，没有与之匹配的'('
        # 说明连续的有效括号的子串断开了，left和right重新归0
        # 保留正序遍历结果maxlength，进行反序遍历
        
        # 反序遍历s也是类似的逻辑，但有一点不同
        # 当出现right<left时，说明此时的'('位置之后，没有与之匹配的')'
        # 说明连续的有效括号的子串断开了，left和right重新归0

        # 为什么要反序遍历一遍呢？
        # 正序遍历判断断开，以')'为准，若没有与')'匹配的'('，则断开
        # 反序遍历判断断开，以'('为准，若没有与'('匹配的')'，则断开
        # 分别判断取最大值
        # 例如：s='()((())'
        # 正序maxlength=2；反序maxlength=4，所以最大值为4                           

        n, left, right, maxlength = len(s), 0, 0, 0
        # 正序遍历
        for i in range(n):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength = max(maxlength, 2 * right)
            elif right > left:
                left = right = 0
        
        # 反序遍历
        left = right = 0
        for i in range(n-1, -1, -1):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                maxlength=max(maxlength, 2 * left)
            elif right < left:
                left=right=0
        return maxlength
