from typing import List

class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        
        # 核心思想
        # 跳水板总长度最短：全部为短板，最长：全部为长版 
        # 每次循环从全部为短板开始，然后短板减一块加入一块长版，直到全部变为长版
        # 每次得到数值放入lists中，最后返回lists

        # 注意
        # k为空时，返回[]
        # 当短板长度==长板长度时，最长长度==最短长度，所以返回shorter*k即可
        
        if not k:
            return []
        if shorter == longer:
            return [shorter * k]       
        lists = list()
        for i in range(k+1):
            j = k-i
            sum = longer * i + shorter*j
            lists.append(sum)
        
        return lists


