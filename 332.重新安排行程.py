import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # 核心思想--深度搜索+回溯
        # 首先先把图的邻接表存进字典，然后对字典的value进行排序
        # 然后从'JFK'开始深搜，每前进一层就减去一条路径，
        # 直到某个节点不存通往其他节点的路径时，说明该节点就为此次行程的终点
        # 需要跳出while循环进行回溯，返回到上一层节点进行搜索，再次找到倒数第二个终点，依次类推
        # 设定ans为返回答案，每次找到的节点都要往头部插入

        # 举例说明：[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        # 构建领接表的字典：{'JFK': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        # 按照题目要求对字典的val排序：{'JFK': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        # 开始从 JFL 开始进行dfs搜索
        # 1.JFK --> ALT  
        #   JFK pop出ALT,JFK的字典变为：'JFK': ['SFO']
        # 2.JFK --> ALT --> JFK 
        #   ALT pop出JFK,ALT的字典变为：'ALT': ['SFO']
        # 3.JFK --> ALT --> JFK --> SFO 
        #   JFK pop出SFO,JFK的字典变为：'JFK': ['']
        # 4.JFK --> ALT --> JFK --> SFO --> ATL 
        #   SFO pop出ALT,SFO的字典变为：'SFO': ['']
        # 5.JFK --> ALT --> JFK --> SFO --> ATL --> SFO
        #   ATL pop出SFO,ATL的字典变为：'ATL': ['']
        # 此时我们可以发现SFO的val为空，没有地方可以去了，说明我们已经找出了终点SFO
        # 然后向上回溯，依次将其添加到ans中
        # 最终答案为：["JFK","ATL","JFK","SFO","ATL","SFO"]


        d = collections.defaultdict(list)   #邻接表
        for f, t in tickets:
            d[f] += [t]  # 路径存进邻接表

        for f in d:
            d[f].sort()  # 邻接表排序

        ans = []
        def dfs(f):  # 深搜函数
            while d[f]:
                dfs(d[f].pop(0))  # 路径检索            
            ans.insert(0, f)  # 放在最前

        dfs('JFK')
        return ans
