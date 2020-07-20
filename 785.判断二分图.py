from typing import List

class Solution:

    # 核心思想
    # 相连的两个节点颜色要相反
    # 采用BFS的方式
    # 由题目可知，大列表的下标代表第几个节点，里面的小列表代表这个节点链接的其他节点
    # 列入[[1,3], [0,2], [1,3], [0,2]]，表示0号节点链接1、3节点，1号节点链接0、2节点......
    # 设定一个color来设置颜色，首先循环到的节点颜色设置为1
    # 在设置一个queue，用来存放已染色的节点，然后循环该节点链接的节点，并将其颜色设置为该节点相反的颜色
    # 若循环完毕，没有出现相互链接的节点，颜色相同的情况，则表示可以分为二分图
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}  # 设定一个存放颜色的字典
        for node in range(len(graph)):
            queue = []  # 用来存放以染色的节点
            if node not in color:  
                # 如果节点没有颜色，则设置颜色为1
                color[node] = 1
                queue.append(node)  # 并放入queue中
            while queue:
                # 循环queue
                pop_node = queue.pop(0)  # 弹出queue中的第一个节点
                for next_node in graph[pop_node]:
                    # 循环遍历该节点链接的节点
                    if next_node not in color:
                        # 如果链接的节点不在color中，则染上相反的颜色
                        color[next_node] = color[pop_node] ^1
                        queue.append(next_node)  # 将染上颜色的节点放入queue中
                    elif color[next_node] == color[pop_node]:
                        # 如果出现当前节点链接的节点出现与该节点颜色相同的情况，则返回false
                        return False
        return True  # 若没有出现矛盾，则返回true