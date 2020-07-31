graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D'],
    'F': ['D']
}


def BFS(graph, s):

    # 将图变为树

    queue = list()  # 定义BFS的队列
    queue.append(s)

    seen = set()  # 定义一个set集合，记录已经走过的节点
    seen.add(s)

    parent = {s: None}  # 记录当前节点的前一个节点，其中根节点的前一个节点为空

    while queue:
        vertex = queue.pop(0)  # 弹出队首节点
        nodes = graph[vertex]  # 找出该节点的所有连节点
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)

    return parent


par = BFS(graph, 'E')

for key, val in par.items():
    print(key, val)


# 找到当前节点到根节点的路径
cur = 'B'
while cur:
    print(cur)
    cur = par[cur]
