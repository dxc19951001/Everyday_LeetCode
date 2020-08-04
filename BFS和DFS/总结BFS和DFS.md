# BFS和DFS原理

## BFS

![image-20200729091213105](总结BFS 和 DFS.assets/image-20200729091213105.png)

BFS是先对每一层进行搜索

对于上图以A为根节点进行BFS搜索：A-B-C-D-E-F

以E为根节点进行BFS搜索：E-C-D-A-B-F

注意BFS搜索的顺序，每一层搜索的顺序，为上一层节点顺序所连接的节点，例如以A为根节点：A-B-C-E-D-F就是错的，因为第二层先是B，第三层应该先搜索B的连接的节点

因此实现BFS可以采用维护 队列 的方式实现

![image-20200729092724017](总结BFS 和 DFS.assets/image-20200729092724017.png)

| 出栈 | 入队 | queue | BFS         |
| ---- | ---- | ----- | ----------- |
| null | A    | A     | null        |
| A    | B C  | B C   | A           |
| B    | D    | C D   | A-B         |
| C    | E    | D E   | A-B-C       |
| D    | F    | E F   | A-B-C-D     |
| E    | null | F     | A-B-C-D-E   |
| F    | null | null  | A-B-C-D-E-F |



## DFS

<img src="总结BFS 和 DFS.assets/image-20200729092114830.png" alt="image-20200729092114830" style="zoom: 50%;" />

DFS是先走到底部节点，在返回到根节点

对于上图以A为根节点进行DSF搜索：A-B-D-F-E-C

实现DFS可以采用维护 队列 的方式实现

 维护一个stack，放入根节点，每次循环先出栈，在放入与出栈节点相连的节点

| 出栈 | 入栈 | stack | DFS         |
| ---- | ---- | ----- | ----------- |
| null | A    | A     | null        |
| A    | B C  | B C   | A           |
| B    | D    | D C   | A-B         |
| D    | F E  | F E C | A-B-D       |
| F    | null | E C   | A-B-D-F     |
| E    | null | C     | A-B-D-F-E   |
| C    | null | null  | A-B-D-F-E-C |

## 代码实现

```python
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
        vertex = stack.pop()  # 弹出队尾节点
        nodes = graph[vertex]  # 找出该节点的所有连节点
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print(vertex) 


BFS(graph, 'A')
print('-----')   
DFS(graph, 'A')   
```

# BFS最短路径搜索

![image-20200729103814053](总结BFS 和 DFS.assets/image-20200729103814053.png)

每条边上的数字是两点之间的距离

从A走到D有两种方案：ABD，路径长度为6；ACD，路径长度为5；最短路径为ACD

## Priority Queue  

优先队列：每一个元素都带有一个权限值，若权限值高，可进行插队。

若：A,1；C,5；D,3;  （前面为元素，后面数字为权值）

| 入队 | Priority Queue | 备注             |
| ---- | -------------- | ---------------- |
| A,1  | A,1            |                  |
| C,5  | A,1  C,5       |                  |
| D,3  | A,1 D,3 C,5    | D,3插队值C,5前面 |

python中采用heapq模块实现优先队列

参考链接：https://blog.csdn.net/qq_35883464/article/details/99410423

## 采用优先队列进行最短路径搜索

求点A出发到其他所有点的距离，所以每个节点的距离要加上之前的距，所以元素的权重都是到A的距离

入队的元素为出队元素连接的且未走到的点

| 出队 | 入队        | Priority Queue        | 备注                  | 走完的点                 |
| ---- | ----------- | --------------------- | --------------------- | ------------------------ |
| null | A,0         | A,0                   |                       | NULL                     |
| A,0  | C,1 B,5     | C,1 B,5               | C权重大               | A,0                      |
| C,1  | D,5 E,8 B,3 | B,3 B,5, D,5 E,9      | B,3是路径ACB的值      | A,0 C,1                  |
| B,3  | D,4         | D,4 B,5, D,5 E,9      | B,3连接的D            | A,0 C,1 B,3              |
| D,4  | E,7 F,10    | B,5, D,5 E,7 E,9 F,10 | 从D,3走到E,F          | A,0 C,1 B,3 D,4          |
| B,5  | null        | D,5 E,7 E,9 F,10      | B以完                 | A,0 C,1 B,3 D,4          |
| D,5  | null        | E,7 E,9 F,10          | D以完                 | A,0 C,1 B,3 D,4          |
| E,7  | null        | E,9 F,10              | 没有与E相连未走完的点 | A,0 C,1 B,3 D,4 E,7      |
| E,9  | null        | F,10                  | E以走完               | A,0 C,1 B,3 D,4 E,7      |
| F,10 | null        | null                  | 没有与F相连未走完的点 | A,0 C,1 B,3 D,4 E,7 F,10 |

维护一个各个节点parent的字典

| 节点      | A    | B    | C    | D    | E    | F    |
| --------- | ---- | ---- | ---- | ---- | ---- | ---- |
| 父节点    | null | C    | A    | B    | D    | D    |
| 到A点距离 | 0    | 3    | 1    | 4    | 7    | 10   |

因此从A走到F的最短路径为：

A-C-B-D-F

代码实现

```python
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
```

运行结果，与预期结果一致

```python
{'A': None, 'B': 'C', 'C': 'A', 'D': 'B', 'E': 'D', 'F': 'D'}
{'A': 0, 'B': 3, 'C': 1, 'D': 4, 'E': 7, 'F': 10}
```

