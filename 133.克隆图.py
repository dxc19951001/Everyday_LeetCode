# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors

import copy


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        # 核心思想--使用copy库进行deepcopy

        return copy.deepcopy(node)
    

    def cloneGraph2(self, node: 'Node') -> 'Node':

        # 核心思想--dfs
        # 由于是无向图，任何给定的无向边都可以表示为两个有向边，即如果节点 A 和节点 B 之间存在无向边，
        # 则表示该图具有从节点 A 到节点 B 的有向边和从节点 B 到节点 A 的有向边。
        
        # 使用一个哈希表存储所有已被访问和克隆的节点。哈希表中的 key 是原始图中的节点，value 是克隆图中的对应节点。
        # 从给定节点开始遍历图。如果某个节点已经被访问过，则返回其克隆图中的对应节点。
        # 如果当前访问的节点不在哈希表中，则创建它的克隆节点并存储在哈希表中。
        
        # 注意：在进入递归之前，必须先创建克隆节点并保存在哈希表中。
        # 如果不保证这种顺序，可能会在递归中再次遇到同一个节点，再次遍历该节点时，陷入死循环。

        # 递归调用每个节点的邻接点。每个节点递归调用的次数等于邻接点的数量，每一次调用返回其对应邻接点的克隆节点，
        # 最终返回这些克隆邻接点的列表，将其放入对应克隆节点的邻接表中。这样就可以克隆给定的节点和其邻接点。

        lookup = {}  # 设定一个hash表

        def dfs(node):
            # dfs搜索
            if not node: return  # 没有节点之间返回
            if node in lookup:
                return lookup[node]  # 节点在hash表中，则返回其克隆图中的对应节点
            
            clone = Node(node.val, [])  # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
            
            lookup[node] = clone  # 哈希表存储克隆的节点
            
            for n in node.neighbors:
                # 每次访问节点的邻居节点
                clone.neighbors.append(dfs(n))  # 最终返回这些克隆邻接点的列表，将其放入对应克隆节点的邻接表中
            
            return clone

        return dfs(node)


    def cloneGraph3(self, node: 'Node') -> 'Node':

        # 核心思想--BFS
        # 使用一个哈希表 lookup 存储所有已被访问和克隆的节点。哈希表中的 key 是原始图中的节点，value 是克隆图中的对应节点。

        # 将题目给定的节点添加到队列。克隆该节点并存储到哈希表中。

        # 每次从队列首部取出一个节点，遍历该节点的所有邻接点。
        # 如果某个邻接点已被访问，则该邻接点一定在 lookup 中，那么从 lookup 获得该邻接点，否则创建一个新的节点存储在 lookup 中，
        # 并将邻接点添加到队列。将克隆的邻接点添加到克隆图对应节点的邻接表中。重复上述操作直到队列为空，则整个图遍历结束。

        from collections import deque
        lookup = {}

        def bfs(node):
            # BFS搜索
            if not node: return  # 如果没有node则返回
            
            clone = Node(node.val, [])  # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
            
            lookup[node] = clone  # 哈希表存储克隆的节点
            
            queue = deque()  # 创建队列
            queue.appendleft(node)  # 在队列左边进行添加
            while queue:
                # 遍历图，直到队列为空
                tmp = queue.pop()  # 弹出最后一个节点
                for n in tmp.neighbors:
                    if n not in lookup:
                        # 如果节点不在哈希表中，则创建一个新的节点存储在 lookup 中
                        lookup[n] = Node(n.val, [])
                        queue.appendleft(n)  # 将该节点添加至队列中
                    lookup[tmp].neighbors.append(lookup[n])  # 给节点添加邻居节点
            return clone

        return bfs(node)

