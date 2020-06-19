class Solution(object):
    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 核心思想：
        # 使用字符串lower()方法全部变成小写
        # 使用isalnum()方法判断字符是字母或数字，去掉符合
        # 比较正序与倒叙的字符串是否相等

        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]


    def isPalindrome(self, s):
        
        # 核心思想：
        # 双指针
        # 同样将字符串字母全部变成小写，并去掉符号
        # 在字符串首尾两端分别设置指针，并判断两个指针是否相等
        # 直至左边指针大于或等于右边指针位置时，都么有不相等的，则为true

        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left, right = 0, n - 1
        
        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True

s = Solution()
b = "A man, a plan, a canal: Panama"
a = s.isPalindrome(b)
print(a)