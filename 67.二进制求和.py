class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 核心思想
        # 利用int(x, base=10)方法
        # x -- 字符串或数字。
        # base -- 进制数，默认十进制
        # 如果是带参数base的话，x要以字符串的形式进行输入
        # 例如：int(11,2),将二进制的11转换为10进制的3
        # bin()方法，返回一个整数 int 或者长整数 long int 的二进制表示。
        # 例如：bin(10) 返回：'0b1010'

        return bin(int(a,2)+int(b,2))[2:]
    
    def addBinary2(self, a: str, b: str) -> str:
        
        # 核心思想
        # 1.比较两个字符的长度，长度短的需要根据长度长的字符来在前面进行补0操作，用while循环搞定；
        # 2.定义一个记录是否进位的标志，一个用来存储结果的list
        # 3.从尾到头一次遍历每一位，注意要先把字符转成二进制，同时还要加上进位的标志一起计算
        # 4.>=2时说明需要进位，就把结果insert在list的第一个位置，同时记录进位
        # 5.最后需要判断一下是否还需要进位，如果还需要就要在最开头的位置insert字符1
        # 6.最后用“”.join(list)来将list转成str，注意list中必须是字符型。
        
        while len(a)<len(b):
            a = "0"+a
        while  len(a)>len(b):
            b = "0"+b
        lens = len(a) #当前字符的长度
        carry = 0  ##记录是否有进位
        res = [] ##记录每次计算的结果
        for i in range(lens-1,-1,-1): ##从最后一位开始进行计算
            sums = int(a[i],2)+int(b[i],2)+carry  ##二进制转成十进制
            if sums >=2:  ##说明有进位
                curr_res = str(sums-2)
                res.insert(0,curr_res)
                carry = 1
            else:
                res.insert(0,str(sums))
                carry = 0
        if carry:
            res.insert(0,"1") 
        # print(res)
        return "".join(res)
