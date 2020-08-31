from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # 核心思想--DFS搜索（递归实现）
        # 定义一个visited为set集合，记录已经去过的房间
        # 当visited的长度等于rooms的长度时，说明所有房间都去过了，即为true

        visited=set()  # 定义一个set集合，记录已经去过的房间
        n=len(rooms)
        def dfs(num):
            if num in visited:
                # 如果房间已经去过了，直接返回
                return 
            else:
                # 如果房间没有去过，加入到set中
                visited.add(num)
            
            for i in rooms[num]:
                # 依次对房间中的每把钥匙依次展开dfs搜索
                dfs(i)
            return 
        dfs(0)
        return len(visited)==n
    
    def canVisitAllRooms2(self, rooms: List[List[int]]) -> bool:
        # 核心思想--DFS搜索（栈实现）

        n=len(rooms)
        seen = set()  # 定义一个set集合，记录已经走过的节点
        def DFS(num):
            stack = list()  # 定义DFS栈
            stack.append(num)
            seen.add(num)
        
            while stack:
                # 栈不为空则进行搜索
                vertex = stack.pop()  # 弹出队尾部节点，即弹出一个房间
                nodes = rooms[vertex]  # 拿到该房间中的所有钥匙
                for w in nodes:
                    # 循环每把钥匙
                    if w not in seen:
                        # 若钥匙对应的房间还没有去过
                        stack.append(w)  # 加入栈中
                        seen.add(w)  # 加入set集合中
        DFS(0)
        return len(seen)==n

