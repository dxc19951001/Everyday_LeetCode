class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 核心思想
        # dfs前序遍历
        # 运用递归分别遍历出左边节点和右边节点
        # 然后合并返回序列化字符串

        # 为什么选择 前序遍历，因为在反序列化时，根|左|右根∣左∣右，更容易定位根节点的值
        # 遇到 null 节点，也要翻译成一个特殊符号，反序列化时才知道这里对应 null 节点

        if root == None: return 'X,'
        leftserilized = self.serialize(root.left)
        rightserilized = self.serialize(root.right)
        return str(root.val) + ',' + leftserilized + rightserilized

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        # 反序列化
        # 序列化时是前序遍历 —— 根|左|右
        # 序列化字符串呈现这样的排列：
        # 根∣(根∣(根∣左∣右)∣(根∣左∣右))∣(根∣(根∣左∣右)∣(根∣左∣右))
        
        data = data.split(',')
        root = self.buildTree(data)
        return root 

    
    def buildTree(self,data):

        # 构建树的函数 buildTree
        # buildTree 接收的 “状态” 是 list 数组，由序列化字符串转成
        # 按照前序遍历的顺序还原出这棵树：先构建根节点，再构建左子树，再构建右子树
        # list 数组首项是 当前子树的根节点，弹出，先遍历它
        
        # buildTree 关注当前节点，然后职责转交
        # 将 list 数组的首项弹出，考察它
        # 如果它为 'X' ，直接返回 null ，没有子树可构建
        # 如果它不为 'X'，则为它创建 node 节点，并构建子树
        # 递归调用 buildTree 构建左子树
        # 递归调用 buildTree 构建右子树
        # 以 node 为根节点的子树，构建完毕，向上返回

        val = data.pop(0)
        if val == 'X': return None
        node = TreeNode(val)
        node.left = self.buildTree(data)
        node.right = self.buildTree(data)
        return node



# 测试用例
var1 = TreeNode(1)
var2 = TreeNode(2)
var3 = TreeNode(3)
var4 = TreeNode(4)
var5 = TreeNode(5)

var1.left = var2

var1.right = var3
var3.left = var4
var3.right = var5

c = Codec()

data = c.serialize(var1)
print(data)

b = c.deserialize(data)
print(b)

