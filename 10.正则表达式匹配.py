class Solution(object):
    def isMatch(self, s, p):

        # 核心思想
        # 递归回溯
        # 本题难点在于'*' 匹配零个或多个前面的那一个元素，例如a*，则a可以为0个或多个
        # 所以根据'*'是否为p中的第二个元素，分两种情况考虑
        # 1.p中第二个元素不为'*'，每次比较第一个元素，相同后，去除第一个元素，进入下一次递归，直至p对s匹配完
        # 2.p中第二个元素为'*'，必然p长度要大于2，因为'*'前面必然有一个元素，分为匹配前零个和匹配前一个元素两种情况考虑
        #   2.1 匹配前零个元素，即'*'的前一个元素没有匹配的，则s不变，将p中的'*'和前一个元素去除，即去除首部2个元素
        #   2.2 匹配前一个元素，即'*'的前一个元素有匹配的，则将s的第一个元素去除，p不变
        #   类似存在s='abb',p='a*abb';
        #   按2.1来说，p剪去两个元素，s='abb',p='abb'，成功；
        #   按2.2来说，s='bb',p='a*abb',失败；
        #   所以，2.1与2.2的关系是或，只要2.1或2.2有一个为真则返回真

        # 运用递归回溯的方法，不难发现重叠子树非常多。leetcode运行时间：1520 ms
        # 可考虑对递归方法加入缓存，提高效率
        # from functools import lru_cache
        # @lru_cache(100)
        # 可考虑使用动态规划的方法

        if not p:
            # 递归退出条件，若p已经用完了，s仍未匹配完，则为false
            return not s

        # 第一个字母是否匹配，s存在且，p的第一个字母与s的一个字母相等，或p的第一个字母为'.'
        first_match = bool(s and p[0] in {s[0], '.'})
        # 如果 p 第二个字母是 *
        if len(p) >= 2 and p[1] == "*":
            # 2.1的情况，第一个字母没有匹配，则p去除'*'和'*'前面的字母， self.isMatch(s, p[2:])
            # 2.2的情况，第一个字母匹配，则去除s的前1个字母 first_match and self.isMatch(s[1:], p)
            # 两者或关系
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            # 对于不存在'*'的情况，依次比较s与p的没一个元素
            return first_match and self.isMatch(s[1:], p[1:])



class Solution2(object):
    # 核心思想
    # 动态规划
    # dp[i][j] 表示的状态是 s 的前 i 项和 p 的前 j 项是否匹配
    
    # 1. s[i] == p[j] or p[j] == '.'：比如 abb 和 abb，或者 abb 和 ab.，
    #   很容易得到 dp[i][j] = dp[i-1][j-1] = True。
    #   因为 ab 和 ab 是匹配的，如果后面分别加一个 b，或者 s 加一个 b 而 p 加一个  ，仍然是匹配的。
    
    # 2. p[j] == '*'：当 p[j] 为'*'时，由于'*'与前面的字符相关，
    #   因此我们比较'*'前面的字符 p[j-1] 和 s[i] 的关系。根据'*'前面的字符与 s[i] 是否相等，又可分为以下两种情况：
    # 2.1 p[j-1] != s[i]：如果'*'前一个字符匹配不上，即'*'号匹配了0次，因忽略'*'和其前面的一个字母，
    #     看p[j-2] 和 s[i] 是否匹配。 这时 dp[i][j] = dp[i][j-2]。
    # 2.2 p[j-1] == s[i] or p[j-1] == '.': '*'前面的字符可以与 s[i] 匹配，这种情况下，'*'可能匹配了前面的字符的 0 个，也可能匹配了前面字符的多个，
    # 2.2.1 当匹配 0 个时，如 ab 和 abb*，或者 ab 和 ab.* ，这时我们需要去掉 p 中的 b* 或 .* 后进行比较，即 dp[i][j] = dp[i][j-2]；
    # 2.2.2 当匹配多个（包括1个）时，如 abbb 和 ab*，ab和ab*，或者 abbb 和 a.*，则s[i-1]=p[j]，即 dp[i][j] = dp[i-1][j]
    # 只要2.2.1或2.2.2其中有一个为真，则返回真
    
    # 3. 特殊情况，当s为空时即dp[0][j]，若p的长度大于2，如a*或a*b*，可以匹配成功，即dp[0][j] = dp[0]dp[j-2]

    # 4. 以上两种情况把能匹配的都考虑全面了，所以其他情况为不匹配，即 dp[i][j] = False
    
    
    def isMatch(self, s: str, p: str) -> bool:
        # 边界条件
        if not p: return not s
        # 当p为空时，s为空则返回true，若s不为空，则返回false
        if not s and len(p) == 1: return False
        # 当s为空，p的长度为1时，无论如何p无法匹配成功

        m, n = len(s) + 1, len(p) + 1
        dp = [[False for _ in range(n)] for _ in range(m)]
        # 考虑为p和s为空的情况构建二维矩阵，p字母的个数为列，s的字母额个数为行
        # 注意：m和n是s和p的长度加一，在构建二维数组的时候，是考虑了s和p为空的情况
        #       不能直接用来循环遍历s和p，所以在循环遍历s和p的时候，要减1


        # 初始状态
        dp[0][0] = True  # 当p和s都为空时，为true
        dp[0][1] = False # 当s为空，p只有一个时，为false

        for c in range(2, n):
            # 情况3
            j = c - 1
            if p[j] == '*':
                dp[0][c] = dp[0][c - 2]
               
        for r in range(1,m):
            i = r - 1
            for c in range(1, n):
                j = c - 1
                if s[i] == p[j] or p[j] == '.':
                    # 情况1
                    dp[r][c] = dp[r - 1][c - 1]
                elif p[j] == '*':
                    # 情况2
                    if p[j - 1] == s[i] or p[j - 1] == '.':
                        # 情况2.2
                        dp[r][c] = dp[r - 1][c] or dp[r][c - 2]
                    else:
                        # 情况2.1
                        dp[r][c] = dp[r][c - 2] 
                else:
                    # 情况4
                    dp[r][c] = False
        return dp[m - 1][n - 1]




s = ''
p = 'b*'

x = Solution().isMatch(s, p)
print(x)
