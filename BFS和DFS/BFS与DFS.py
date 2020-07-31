graph = {
    'A' : ['B', 'C'],
    'B' : ['A', 'C', 'D'],
    'C' : ['A', 'B', 'D', 'E'],
    'D' : ['B', 'C', 'E', 'F'],
    'E' : ['C', 'D'],
    'F' : ['D']
}

def BFS(graph, s):
    queue = list()  # 定义BFS的队列
    queue.append(s)
    
    seen = set()  # 定义一个set集合，记录已经走过的节点
    seen.add(s)
 
    while queue:
        vertex = queue.pop(0)  # 弹出队首节点
        nodes = graph[vertex]  # 找出该节点的所有连节点
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex) 

def DFS(graph, s):
    stack = list()  # 定义BFS的队列
    stack.append(s)
    
    seen = set()  # 定义一个set集合，记录已经走过的节点
    seen.add(s)
 
    while stack:
        vertex = stack.pop()  # 弹出队尾部节点
        nodes = graph[vertex]  # 找出该节点的所有连节点
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex) 


BFS(graph, 'A')
print('-----')   
DFS(graph, 'A')   