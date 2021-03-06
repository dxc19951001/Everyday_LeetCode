# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverFromPreorder1(self, S: str) -> TreeNode:
        
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
                

   def recoverFromPreorder(self, S):
       
        # 核心思想
        # 采用单调栈来解决
        
        # 以输入"1-2--3--4-5--6--7"为例
        # 采用深度搜索前序遍历，如果节点只有一个子节点，那么保证该子节点为左子节点。
        # 那将其表示成 数值(深度)  的形式
        # 1(0) 2(1) 3(2) 4(2) 5(1) 6(2) 7(2)
        # 根节点1(0)先入栈，栈：[1(0)]
        # 2(1) 由于深度比1(0)深 入栈,栈：[1(0), 2(1)]
        # 3(2)深度比栈顶元素2(1)深 入栈，栈：[1(0), 2(1), 3(2)]
        # 4(2)深度与栈顶元素3(2)一样，栈顶元素3(2)出栈，并挂至上一节点2(1)的左边（题意优先左子节点），栈：[1(0), 2(1)]
        # 4(2)深度与栈顶元素2(1)深 入栈，栈：[1(0), 2(1), 4(2)]
        # 5(1)深度比栈顶元素4(2)小，栈顶元素4(2)出栈，并挂至上一节点2(1)的右边（左子节点已经被挂过了),栈：[1(0), 2(1)]
        # 5(1)深度与栈顶元素2(1)一样，栈顶元素2(1)出栈，并挂至上一节点1(0)的左边，栈：[1(0)]
        # 5(1)深度比栈顶元素1(0)深 入栈，栈：[1(0), 5(1)]
        # 6(2)深度比栈顶元素5(1)深 入栈，栈：[1(0), 5(1), 6(2)]
        # 7(2)深度与栈顶元素6(2)一样，栈顶元素6(2)出栈，并挂至上一节点5(1)的右边，栈：[1(0), 5(1)]
        # 7(2)深度比栈顶元素5(1)深 入栈，栈：[1(0), 5(1), 7(2)]
        # 对于栈中剩下的元素依次挂至上一节点的左子节点中，若左子节点有值，则挂至右子节点
        # 直至栈中剩下根节点1(0)没问题得到解决
        

        i = 0  # 初始化循环变量
        stack = []  # 初始化栈
        pre_depth = -1  # 初始化前一节点深度
        while i < len(S):
            depth = 0  # 初始化当前节点深度 
            while S[i] == '-':  # 当前数字前有几个'-'，代表深度为几
                depth += 1
                i += 1
            value = ''  # 初始化节点值
            while i < len(S) and S[i].isdigit():  # 循环出该节点的值
                value += S[i]
                i += 1
            node = TreeNode(int(value))
            
            while stack and depth <= pre_depth:
                # 栈不为空且，当前节点深度比之前节点深度小于或等于时出栈
                out = stack.pop() # 出栈
                if not stack[-1].left:  # 左子节点不为空，优先挂至左子节点
                    stack[-1].left = out
                else:  # 左子节点以有值，则挂至右子节点
                    stack[-1].right = out
                pre_depth -= 1  # 栈顶元素出栈后，之前节点的深度减1
            pre_depth = depth  # 当前节点入栈后，改变之前节点的深度值
            stack.append(node) # 入栈

        # 入栈完毕，剩下的元素
        while stack:
            if len(stack) == 1:  # 当栈中剩下根节点时结束
                break           
            out1 = stack.pop()   # 最后一个节点依次出栈            
            if not stack[-1].left:  # 优先挂至前一节点的左子节点
                stack[-1].left = out1
            else:  # 左子节点有值，挂至有子节点
                stack[-1].right = out1         
            
        return stack[0]  # 返回根节点



s = Solution()
S = "1-2--3--4-5--6--7"
a = s.recoverFromPreorder(S)
print(a)

