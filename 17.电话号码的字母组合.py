from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # 核心思想--利用列表推导式

        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        if digits == '':
            return []
        
        ans = ['']  # 注意：ans要现设为空列表
        for num in digits:
            ans = [pre+suf for pre in ans for suf in KEY[num]]  # 关键
            # 先执行第一层循环 for pre in ans,得到前一个ans中的每一个前缀
            # 再执行第二层循环 for suf in KEY[nums],得到新加入数组中的每个字母
            # 然后更新ans，得到新加入字母的列表
            # 相当于：
        # for num in digits:
        #     tmp = list()
        #     for pre in ans:
        #         for suf in KEY[num]:
        #             tmp.append(pre+suf)
        #             ans = tmp
        return ans
    
    def letterCombinations2(self, digits: str) -> List[str]:

        # 核心思想--回溯
        # 每次取电话号码的一位数字，从哈希表中获得该数字对应的所有可能的字母，并将其中的一个字母插入到已有的字母排列后面，
        # 然后继续处理电话号码的后一位数字，直到处理完电话号码中的所有数字，即得到一个完整的字母排列。
        # 然后进行回退操作，遍历其余的字母排列。

        if not digits:
            return list()
        
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index: int):
            if index == len(digits):
                # 递归退出，当字母长度与数字长度相等时
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phoneMap[digit]:
                    combination.append(letter)  # 每次将字母放入临时存储列表中
                    backtrack(index + 1)  # 进入递归，选择限一个字母
                    combination.pop()  # 返回此层递归时，将临时列表中的该层字母删除，表示此字母的所有解已经寻找完了

        combination = list()  # 临时存储每一个字母的所有可能解
        combinations = list()  # 最终返回结果
        backtrack(0)
        return combinations

    def letterCombinations3(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 核心思想：回溯
        # 回溯参数：digits，index号码的下标，record记录的结果
        # 终止条件：index == len(digits)，表明已经找到了对应长度的字符串
        # 单层回溯：通过index找到字母，和进行回溯

        if not digits:
            return []

        etter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        def backtrack(digits, index, record):
            if index == len(digits):
                res.append(record)
                return

            letter = etter_map[digits[index]]

            for i in letter:
                record += i
                backtrack(digits, index + 1, record)
                record = record[:-1]

        backtrack(digits, 0, "")

        return res