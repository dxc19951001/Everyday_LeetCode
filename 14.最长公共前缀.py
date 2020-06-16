class Solution(object):
    def longestCommonPrefix_ASCII(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # 核心思想：
        # main和max函数对字符串排序
        # 是对字符串中的字母的ASCII值进行安位排序的
        # 即对每个位比大小
        # 例如abc(97 98 99)、abb(97 98 98)、acc(97 99 99)
        # 则顺序为 abb < abc < acc
        # 比较排序中最大值和最小值
        # 最大值与最小值的前缀字母有几个一样的，则有整个字符串有几个相同的前缀
        # 因为：若最大值与最小值在同一位的字母一样，则ASCII值相等
        # 这说明中间字符串该位的ASCII值也相等（夹逼定理）
        # 若最大和最小值在同一位的值不等，则结束

        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i,x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1
    

    def longestCommonPrefix_minStr(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 核心思想
        # 找到组成长度最短的字符串，并以此为依据
        # 因为字符串前缀相等的最大长度，即为最短字符串长度
        # 设定一个较大的数j
        # 依次比较每个字符串与最短字符串前缀相同的位数k
        # 每次比较完后更新j值
        # 最终返回最短字符串的前j个字符，即为相同的前缀
        
        if not strs : return ""

        ans = min(strs, key = lambda x: len(x))
        j = 100000000000
        

        for i in range(len(strs)):
            for k in range(len(ans)):
                if ans[k] != strs[i][k]:
                    if j > k:
                        j = k                            
        return ans[:j]

    def longestCommonPrefix_binarySearch(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # 核心思想：
        # 对上述最短字符串方法的改进
        # 找出最短字符串的长度后，最长公共字符串长度已确定
        # 所以进行二分查找，每次查找一半最大公共字符串长度
        # 直到确定最大字符串长度


        def isCommonPrefix(length):
            # 封装二次查找方法
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))
            # all()函数当都为true时，返回true
            # 这里判断所有字符串一半最大字符串长度是否相等

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]



    def longestCommonPrefix_breadthSearch(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # 核心思想
        # 横向搜索
        # 依次比较相邻两个字符串之间最长公共前缀
        # 将每次比较得到的最长公共前缀与下个字符串进行比较，并更新公共前缀

        
        if not strs:
            return ""
        
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        
        return prefix

    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]
    

    def longestCommonPrefix_verticalSearch(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # 核心思想
        # 纵向搜索
        # 从前往后遍历所有字符串的每一列，比较相同列上的字符是否相同，
        # 如果相同则继续对下一列进行比较，
        # 如果不相同则当前列不再属于公共前缀，当前列之前的部分为最长公共前缀。

        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        # 第一个字符串长度、字符串个数
        for i in range(length):
            c = strs[0][i]  # 以第一个字符串为依据，依次比较每一列
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                
                # any()函数中，有一个为true则返回true，全为false返回false
                # i == len(strs[j]) 
                # 判断短字符串，当短字符串该字符串长度等于i时，
                # 即该字符串已经循环到最后一列了，无法再往回循环，退出
                # strs[j][i] != c
                # 判断每一列中的值是否相同，不相同则退出
                                
                return strs[0][:i]
        
        return strs[0]





