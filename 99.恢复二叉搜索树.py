# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def recoverTree(self, root):

        # 核心思想
        # 将搜索二叉树的每一个节点按照中序遍历放入列表中
        # 此列表中的数值应该为单调递增，找到不是单调递增的两个节点，即为出错点
        
        # 中序遍历二叉树，并将遍历的结果保存到list中 
        nodes = []   
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)
        dfs(root)
        
        x = None
        y = None
        pre = nodes[0]
        
        # 扫面遍历的结果，找出可能存在错误交换的节点x和y
        for i in range(1, len(nodes)):
            if pre.val > nodes[i].val:
                if not x:
                    x = pre
                y = nodes[i]  
            pre = nodes[i]
        
        # 如果x和y不为空，则交换这两个节点值，恢复二叉搜索树 
        if x and y:
            x.val,y.val = y.val,x.val
        
