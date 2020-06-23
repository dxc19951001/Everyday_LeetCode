class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:

        # 核心思想
        # 本题的难点在于如何确定pattern中a和b所表示的字符串长度
        # "a"和"b"不能同时表示相同的字符串
        # cnta、cntb 分别表示pattern中a和b的个数

        # 字符value的长度(式子1）可表示为： len(val) = cnta*len(a) + cntb*len(b)
        # 其中a代表的字符串长度len(a):[0, len(val)/cnta]
        #   因为len(a)可以为空，例如ab，dogcat，a为空，b为dogcat
        #   len(a)也可以是value中的每一个单词的长度，例如aaa，dogdogdog
        # 根据式子1，则b表示的字符串长度： len(b)= [len(val) - cnta*len(a)]/cntb
        #   若len(b)计算得不为整数，则a长度下求出的b长度不符合要求，直接进入下一个a长度

        # 一般情况
        # 根据上述分析，我们for循环len(a)的长度范围，不断尝试len(a)可能的长度，枚举出每一种可能的情况
        #   利用set中元素不重复的特性，分别设置两个set存储a和b所代表的字符串
        #   循环遍历pattern，当循环到a时，从value中截取len(a)放入set1中，当循环到b时，再从value中截取len(b)放入setb中
        # 当在a和b的某个长度时，两个set的长度都为1，说明找到了合适的a和b字符串长度，可与表示value
        #   此时返回true
        # 若循环完成，也没有返回两个set的长度都为1
        #   则返回false

        # 考虑一些特殊情况
        # 1.若pattern为空，则value也为空
        # 2.若value为空，则pattern中为空或只有一字母a或b，len(pattern)<=1
        #   因为a和b不能表示相同的字符串，只有一个a或者只有一个b，可以表示为空
        # 3.若pattern只有一个字母，则每个字母的长度为len(value)//len(pattern)
        #   在value中取出该长度的字符串，乘上pattern的长度，应与value相等

        # 特殊情况1
        if not pattern:
            return not value

        # 特殊情况2
        if not value:
            return len(pattern) <= 1

        # 得到a，b个数，和value的长度
        cnta = pattern.count('a')
        cntb = len(pattern) - cnta
        n = len(value)

        # 特殊情况3
        if 0 == cnta*cntb:
            return value == value[:len(value)//len(pattern)]*len(pattern)

        # 一般情况
        for i in range(0, n//cnta+1):
            # 循环遍历a可能的的字符串长度 
            if (n-i*cnta) % cntb == 0:           
                # 因为字符串长度为整数，若a字符串长度下的b字符串长度不为整数，则不符合要求
                j = (n-i*cnta)//cntb  # 根据公式，得到a字符串长度下，b的字符串长度
                cur, judge1, judge2 = 0, set(), set()  # cur用来记录每次切片的节点，设置两种个set集合，记录a和b所代表的的字符串
                for ch in pattern:               
                    if ch == 'a':
                        judge1.add(value[cur:cur + i])  # 向judge1中添加字符串a
                        cur += i
                    else:
                        judge2.add(value[cur:cur + j])  # 向judge2中添加字符串b
                        cur += j
                    if len(judge1) > 1 or len(judge2) > 1:
                        # 若两个集合中有一个中的元素超过1，则不符合要求，跳出此次循环
                        break
                if len(judge1) == 1 and len(judge2) == 1:
                    # 若自身的a字符串长度和b字符串长度，使得两个set集合中的元素不重复，则满足要求，结束
                    return True
        return False


s = Solution()
pattern = ""
value = "x"
print(s.patternMatching(pattern, value))
