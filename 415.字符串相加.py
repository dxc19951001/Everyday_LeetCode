class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        # 核心思想 -- 双指针
        # 先取每个字符串的最后一位，依次向前相加
        # 设置一个carrt进位，模拟加法运算

        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = ''
        while i >= 0  or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1

        return "1" + res if carry else res

    def addStrings2(self, num1: str, num2: str) -> str:

        # 核心思想 -- 双指针
        # 设置一个位数倍数k，个位是1，十位是10，每次相应位置相加并乘以倍数
        # 依次累加每一位数字

        i = len(num1) - 1
        j = len(num2) - 1
        k = 1
        res = 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = (n1 + n2) *k
            res += tmp
            k *=10
            i, j = i-1, j-1

        return str(res)

    
