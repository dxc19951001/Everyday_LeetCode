from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 核心思想：前序遍历+回溯
    # 通过前序遍历遍历到每个叶子节点上，再从叶子节点返回执行未遍历的部分

    def binaryTreePaths(self, root) -> List[str]:
        path = ''  # 记录每此遍历的路径
        result = []  # 最终返回结果
        if not root:
            return result
        self.traversal(root, path, result)  # 路径遍历函数
        return result

    def traversal(self, cur: TreeNode, path: str, result: List[str]) -> None:
        # 递归参数：节点，路径，返回列表
        # 递归终止条件：当为叶子节点时，将路径path加入到结果result中

        # path时赋值，每一层递归都会赋新的值
        # 当下一层递归返回到上一层时，path不会记录下一层增加的部分，形成了回溯
        # 为了记录叶子节点的值，path要放在终止条件前
        path += str(cur.val)

        # 递归终止条件
        if not cur.left and not cur.right:
            result.append(path)

        # 为了防止空指针，只在左右子节点时进行递归
        if cur.left:
            # + '->' 是隐藏回溯
            self.traversal(cur.left, path + '->', result)

        if cur.right:
            self.traversal(cur.right, path + '->', result)
