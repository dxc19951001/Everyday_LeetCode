from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        # 核心思想--暴力4层for循环
        # 本题实质是将字符串划分为4个部分，加上三个 . 变成一个ip地址，
        # 每个部分划分出的字符串装换为整数，需要在[0，255]区间内
        
        # 注意：若划分出的字符串为001，转换为整数位1，
        #       则最终拼接成ip地址的字符串的时候会少2位数字，所以这种时不符合要求的

        res = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a + b + c + d == len(s):
                            # 划分出的4个部分长度相加位原本字符串长度
                            # n1、n2、n3、n4 分别为4个部分
                            n1 = int(s[:a])
                            n2 = int(s[a:a+b])
                            n3 = int(s[a+b:a+b+c])
                            n4 = int(s[a+b+c:])
                            if n1 < 256 and n2 < 256 and n3 < 256 and n4 < 256:
                                # 每个部分都需要在[0,255]区间内
                                ip = str(n1) + '.' + str(n2) + '.' + str(n3) + '.' + str(n4)  # 组成ip地址的长度
                                if len(ip) == len(s) + 3:
                                    # ip地址的长度应该为原本s的长度加上3个 . 的长度
                                    # 若不是则说明有的数字被在转换为整形时去除了，是不符合要求的
                                    res.append(ip)
        return res