from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        # 核心思想--BFS
        # 通过BFS搜索后，对所有元素的值进行计数
        # 选择出现次数最多的元素，若有元素出现次数相同的多，则都输出

        if not root:return []
        queue=[root]
        res=[root.val]
        while queue:
            q=queue.pop()
            if q.left:
                queue.append(q.left)
                res.append(q.left.val)
            if q.right:
                queue.append(q.right)
                res.append(q.right.val)
        dic={}
        for i in res:
            dic[i]=dic.get(i,0)+1
        maxvalue=max(dic.values())
        r=[]
        for j in dic:
            if dic[j]==maxvalue:r.append(j) 
        return r 