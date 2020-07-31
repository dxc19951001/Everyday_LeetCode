import heapq  # 引入heapq实现优先队列

graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}

def init_distance(graph, s):
    # 初始化各个节点到根节点的距离
    distance = {s : 0}
    for vertex in graph:
        if vertex !=s:
            distance[vertex] = float('inf')
    return distance

def dijkstra(graph, s):

    pqueue = list()  # 定义BFS的队列
    heapq.heappush(pqueue, (0, s))

    seen = set()  # 定义一个set集合，记录已经走过的节点
    
    parent = {s: None}  # 记录当前节点的前一个节点，其中根节点的前一个节点为空

    distance = init_distance(graph, s)  # 记录节点点到根节的距离

    while pqueue:
        pair = heapq.heappop(pqueue)  # 弹出队首节点
        dist = pair[0]  # 获取当前节点到根节的距离
        vertex = pair[1]  # 获取当前点
        seen.add(vertex)  # 只有当该点出队后，才能判断为已走过

        nodes = graph[vertex].keys()  # 找出该节点的所有连节点
        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    # 判断当前节点至连接节点到根节点的距离
                    # 例如：从A-B-D,从D到A的距离为5+1
                    # 如果比之前的小，则更新连接点到根节点的距离，已经连接点的父节点
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]

    return parent,distance

parent,distance = dijkstra(graph, 'A')

print(parent)
print(distance)