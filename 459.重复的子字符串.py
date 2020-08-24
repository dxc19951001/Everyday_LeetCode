class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:

        # 核心思想--掐头去尾
        # 若s由子串 x 重复n次构成，则 s = nx
        # s+s = 2nx
        # 移除s+s的第一个字符和最后一个字符，即(s+s)[1:-1]
        # 则第一个s中的第一个子串x，第二个s中的最后一个子串x，的结构就被破坏了
        # 此时剩2n-2个子串，
        # 若s在(s+s)[1:-1]中，说明剩下的子串又重新组成了完整的s，则2n-2>=n, 即n>=2
        #   所以s中至少由2个子串x
        # 若s不在(s+s)[1:-1]中，说明剩下的子串不能重新组成完整的s，则2n-2<n, 即n<2，n只能取1
        #   s只有1个子串x组成，说明s不能由子串x重复多次构成

        return s in (s+s)[1:-1]