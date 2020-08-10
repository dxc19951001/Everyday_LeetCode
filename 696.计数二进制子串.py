class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        # 核心思想
        # 将字符串中，相邻相同的数进行计数，并放入列表中
        # 列入001110，就变成tmp = [2, 3, 1]，解释：2个0,3和1,1个0
        # 在这个列表中相邻的两个位置上分别是相反的两个数
        # 根据题目要求：计算具有相同数量0和1的非空(连续)子字符串的数量
        # tmp中每一位上的数字，代表可以拿出几个1或者0，
        # 我们分别比较相邻两个位置，进行组合，发现能组合出来的子字符串数量由数字小的位置所决定
        # 例如在tmp中
        # 第一位：2；第二位：3，能组合成 2 个子字符串:0011, 01
        # 第二位：3；第三位：1，能组合成 1 个子字符串:10
        # 一共能组合成 3 种
        # 因此，我们对字符串统计中tmp列表后，分别比较tmp中相邻数字，并去最小值进行累加，即可得到答案

        count = 1
        tmp = list()
        res = 0
        
        # 统计出tmp列表
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                count +=1
            else:
                tmp.append(count)
                count = 1       
        tmp.append(count)  # 注意:循环完成后，最后一个count还没有加入tmp，需要加入到tmp中
        
        # 分别比较tmp相邻元素，并取最小值进行累加，得到答案
        for k in range(1, len(tmp)):
            res += min(tmp[k], tmp[k-1])
        
        return res

    def countBinarySubstrings1(self, s: str) -> int:

        # 核心思想
        # 上述方法用到了一个额外的tmp列表，考虑是否可以用常数来代替这个tmp
        # 对于tmp列表吗，其实只关注列表中相邻两个元素的值
        # 那么我们可以用两个常数pre和cur来存储着两个值，达到节约空间的目的

        cur = 1  # 表示当前相同元素的个数
        pre = 0  # 表示上一个相同元素的个数
        res = 0  # 结果
        
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                # 当s中前后元素相同时
                cur += 1  # 当前元素相同时，cur计数加一
            else:
                # 当s前后元素不相同时
                res += min(pre, cur)  # 比较pre和cur，取最小值加到res中，类比tmp中相邻元素相加
                pre = cur  # pre向前移动，变成cur的值
                cur = 1 # cur重新至为1，进入下一个相邻元素的比较
        
        res += min(pre, cur)  # 注意：循环结束后，最后一次cur的值没有比较，再进行一次cur和pre的比较
        
        return res

    

    def countBinarySubstrings2(self, s: str) -> int:

        # 核心思想
        # 能不能在每次前一个相同元素个数与后一个相同元素个数比较的的时候，就直接对res进行操作，
        # 不用在统计完后一个相同元素个数后，在进行比较取较小值
        # 这样能进一步提升速度
        
        # cur：设定的当前元素值，默认为0
        # pre：表示上一个相同元素的个数
        # count：表示当前相同元素的个数
        # res：表示几个

        cur = pre = count = res = 0
        for c in s:
            if c == cur:
                # 若当前元素与设定得当前元素值相同，则count加1
                count += 1
            else:
                # 若不相同
                pre = count  # pre记录上一个相同元素个数
                cur = c  # 对cur进行重新设定
                count = 1  # 设定当前相同元素的个数为1
            
            if pre >= count:  
                # 若pre大于等于count，则res+1
                # 因为：count是一个慢慢变大的过程，只要还不大于pre，之前的相同元素中，总能拿出元素与其匹配
                res += 1

        return res