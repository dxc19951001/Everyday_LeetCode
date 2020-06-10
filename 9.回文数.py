class Solution(object):
    def isPalindromeStr(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 核心思想:
        # 将数字转换为字符串，并检查字符串是否为回文。
        # 但是，这需要额外的非常量空间来创建问题描述中所不允许的字符串。

        x = str(x)
        a = x[::-1]
        if x == a:
            return True
        else:
            return False
        
        # 简单写法
        # return str(x) == str(x)[::-1]

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # 核心思想：
        # 既然是回文数，那么前一半的数就等于后一半的数
        
        # 实现步骤
        # 对x除10取余数，每次得到其最后一位数，
        # 同时对x除10取整，则x减少一位
        # 进入下次循环，倒数第一位数字*10+倒数第二位数字
        # 同时再对x除10取整，则x又减少一位
        # 循环上述两步直到得出前一半和后一半的数
        # 跳出循环条件为后一半的数不小于前一半的数
        
        # 判断是为回文数
        # 偶数情况：前一半的数 == 后一半的数
        # 奇数情况：前一半的数 == 后一半的数/10

        # 边界条件
        # 当数字为2位及以上时，末位数为0，必然不是回文数
        # 当数字为负数时，必然不是回文数

        if x < 0:
            return False
        elif x % 10 == 0 and  x != 0:
            return False
        else:
            revertedNumber = 0
            while(x > revertedNumber ):
                revertedNumber = revertedNumber*10 + x % 10
                x /=10
            return x ==  revertedNumber or x == revertedNumber/10



s = Solution()
a = s.isPalindromeStr(1212)
print(a)
