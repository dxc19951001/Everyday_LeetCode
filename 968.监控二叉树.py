# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # 核心思想--分类讨论
        # 从下往上对每层节点加上相机
        # 根据不同的情况分类讨论，分别判断当前节点的左子树和右子树，是否有相机和相机是否能够向上移动
        # 1.当前节点的左子树和右子树的根节点都没有相机，说明左右子树根节点已经被相机监控了，则给当前节点加上相机，且当前节点的相机可以前移
        # 2.当前节点的左子树和右子树的根节点都有相机，且都能前移，两个相机合并成一个放到该节点上，该节点上的相机不能前移了
        # 3.当前节点的左子树和右子树的根节点都有相机，且其中一个能前移，则将能移动的相机移动至该节点上，该节点上的相机不能前移了
        # 4.当前节点的左子树和右子树的根节点都有相机，但没有能够向前移动的相机，该节点已经被子节点相机覆盖了，则该节点不用加相机，没有相机则也不能向前移动

        def helper(node):

            # def一个helper,返回3个值,分别是
            # 当前子树全覆盖需要的摄像头数 l r
            # 当前子树根节点是否装摄像头 lhc rhc
            # 子树根节点摄像机是否能往前挪至父节点（若为true，则说明该节点有相机） lcm rcm

            if not node:
                return (0, False, False)  # 空节点不需要摄像机,自然后两个必然False
            l, lhc, lcm = helper(node.left)
            r, rhc, rcm = helper(node.right)
            res = r+l  # 一个节点的摄像机数等于左子树和右子树的摄像机数之和,然后分类讨论
            if not lhc and not rhc:  # 2个子树的根节点都没有摄像机
                # 为了覆盖自己,要在自己上面加一个摄像机,res += 1,这个相机不需要覆盖子节点,所以是可以往前挪的.
                return (res+1, True, True)
            if lcm and rcm:  # 2个子树的根节点都有摄像机,而且都能往前挪
                # 2个都挪到自己上面就变成1个了,res-=1,这个相机要覆盖2个子节点,就不能继续向前挪了
                return (res-1, True, False)
            if lcm or rcm:  # 其中1个子树的根节点有摄像机能往前挪
                # 把能挪到自己身上的相机往自己身上挪,这个相机要覆盖被挪走相机的子节点,就不能继续向前挪了
                return (res, True, False)
            else:  # 2个子树都没有能往前挪的摄像机
                # 都不能挪,但自己能被子节点的摄像机覆盖,所以不用加装.
                return (res, False, False)
        return helper(root)[0]
