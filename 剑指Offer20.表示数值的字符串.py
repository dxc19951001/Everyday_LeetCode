class Solution:
    def isNumber(self, s: str) -> bool:

        # 简单用float写了，有限状态自动机太麻烦了吧。。。。

        try:
            float(s)
            return True
        except ValueError:
            return False