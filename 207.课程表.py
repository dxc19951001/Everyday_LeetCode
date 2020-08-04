class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # 核心思想：BFS实现拓扑排序
        # 明白此题需要明白邻接表和拓扑排序的基本概念
        # 推荐参考教程
        #   邻接表：https://www.bilibili.com/video/BV1qt41117iu?from=search&seid=7225342794442360701
        #   拓扑搜索：https://www.bilibili.com/video/BV1PW41187Mz?from=search&seid=12806727847970592120
        # 看完上述教程，即可清楚此题

        indegrees = [0 for _ in range(numCourses)]  # 初始化入杜表
        adjacency = [[] for _ in range(numCourses)]  # 初始化邻接表
        queue = []  # 初始化BFS的队列

        # 构建入杜表和邻接表
        for cur,pre in prerequisites:
            # 由题可知[1,0]画图为0-->1,即pre-->cur
            indegrees[cur] += 1  # 每循环到一个节点，对cur节点的入杜加1
            adjacency[pre].append(cur)  # 邻接表中的pre列表需要加上cur节点
        
        # 将所有入杜为0的节点，放入队列中
        for cur in range(len(indegrees)):
            if not indegrees[cur]: queue.append(cur)
        
        while queue:
            pre = queue.pop(0)  # 将入杜为0的第一个节点出队列
            numCourses -= 1  # 需要学习的课程数减1
            for cur in adjacency[pre]:
                # 循环弹出节点的邻接表中的列表
                indegrees[cur] -= 1  # 该节点连接节点的所有节点，入杜减1
                if not indegrees[cur]: queue.append(cur)  # 若减1后，将入杜为0的节点放入队列中
        return not numCourses  # 若最终所有课程都入队列并出队列，则numCourses为0，符合要求

