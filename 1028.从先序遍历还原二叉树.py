# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverFromPreorder(self, S: str) -> TreeNode:
        
        # 核心思想：
        # 题目采用深度搜索先序遍历，并且如果节点只有一个子节点，那么保证该子节点为左子节点。
        # 深度优先遍历转先序遍历的必然结果是：后一个节点值可能是前一个的左子树，
        # 也可能是前n个的右子树。且同一个深度的情况下优先为左子树。
        # 通过字典的方式保存，字典的key是深度，字典的value是节点值为value的树。
        

        ans = {-1: TreeNode(0)}     
        # 字典初始化，   
        # -1表示深度，
        # TreeNode(0) 表示节点值为0的树
        # 相当于二插数根的父节点     
        
        def addTree(v, p):          
            # 添加树函数
            # 向父节点添加子节点  
            ans[p] = TreeNode(int(v))                   
            # 当前节点值为v的树
            if not ans[p - 1].left: 
                # 左子树不存在就加在左边     
                # 这个很好理解，同一个深度下先放在左子树
                ans[p - 1].left = ans[p]
            else:                   
                # 反之加在右边          
                # 第二次出现的同样深度的 节点 就放在这里的右子树上
                ans[p - 1].right = ans[p]
        
        val, dep = '', 0            
        # 初始化值 和 根节点深度0
        
        for c in S:
            # 遍历字符串
            if c != '-':            
                # 如果不是'-'，将的得到的数字赋值给val
                val += c            
                # 对于多位数，通过累加字符来获得数字   
                # val初始值是''，所以c是数字时和字符串相加，可得到对应的多位数的字符串
            elif val:               
                # 如果是‘-’，且val值存在；
                # 即-的前一位是数字，val有值     
                addTree(val, dep)   
                # 把累加好的数字和对应深度添加进树     
                # 这里就去找有没有左子树，没有就加左边，有就加右边
                val, dep = '', 1    
                # 值和对应深度重新初始化           
                # 由于树的根节点为深度为0
                # 其他子节点的深度为>1
            else:
                # 如果连续的'-'，只加深度不加值   
                dep += 1            
        
        addTree(val, dep)           
        # 末尾剩余的数字也要加进树   
        # 最后一个节点值为一位数 
        # 只在if判断里，所以要补充添加到树里          
        
        return ans[0]            
        # 最后，返回构建好的树的根节点即可
        
        
    def recoverFromPreorder(self, S: str) -> TreeNode:
        i = 0
        stack = []
        pre_depth = -1
        pre_node = None
        while i < len(S):
            depth = 0
            while S[i] == '-':
                depth += 1
                i += 1
            value = ''
            while i < len(S) and S[i].isdigit():
                value += S[i]
                i += 1
            node = TreeNode(int(value))
            
            if stack and depth == pre_depth + 1:
                stack[-1].left = node
            else:
                for _ in range(pre_depth - depth + 1):
                    stack.pop()
                if stack:
                    stack[-1].right = node
            pre_depth = depth
            stack.append(node)
        return stack[0]


