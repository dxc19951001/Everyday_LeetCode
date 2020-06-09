class Solution(object):
    # 核心思想
    # 设定parent列表对应26个字母为[0, 25]，
    # parent列表，表示每个字母的父节点

    # 查：若此列表中数字index值与value值相等，则判定该数字为根节点，
    # 例如parent[0]==0，否则则需要像上找出其根节点。

    # 并：对于“=”相等关系两个字母，可以认为属于同一颗树进行合并，
    # 例如`a==b`，可设定a的父节点即为b，`a-->b`。反之，对于“!=”不等关系，则属于两颗不同的树，不能进行合并。

    # 判断矛盾：出现“!=”不等关系的两个字母，不属于同一棵树，必然期根节点不一样，
    # 若一样则出现矛盾，则判定为false。


    class UnionFind:
        # 定义一共并查集的类       
        def __init__(self):
            self.parent = list(range(26))
        
        def find(self, index):
            # 查找出每个数字的父节点，直到得出根节点
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]
        
        def union(self, index1, index2):
            # 将相同的根节点的数字链接起来
            self.parent[self.find(index1)] = self.find(index2)


    def equationsPossible(self, equations):
        uf = Solution.UnionFind()
        # 找出所有等于关系的字母
        # 将有相同根节点的数字构成一颗树
        # 得到若干棵不同根的树
        for st in equations:
            if st[1] == "=":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                uf.union(index1, index2)
        
        # 找到所有不等关系的字母
        # 若判断两个不等关系的字母，是否在根相同的一棵树中
        # 若在同一根的数中则返回false 
        for st in equations:
            if st[1] == "!":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):
                    return False
        return True


class SolutionRank(object):
    # 核心思想
    # 按秩优化，在合并两棵树的时候，将树高度低的树合并到高度高的树上

    class UnionFind:
        # 定义一共并查集的类       
        def __init__(self):
            self.parent = list(range(26))
            self.rank = len(self.parent)*[0]

        
        def find(self, index):
            # 查找出每个数字的父节点，直到得出根节点
            if index == self.parent[index]:
                return index
            self.parent[index] = self.find(self.parent[index])
            return self.parent[index]
        
        def union(self, index1, index2):
            # 将相同的根节点的数字链接起来
            # 并判断哪颗树高，将低的树合并到高的树上
            if self.rank[index1] > self.rank[index2]:
                self.parent[self.find(index2)] = self.find(index1)
            elif self.rank[index1] < self.rank[index2]:
                self.parent[self.find(index1)] = self.find(index2)
            else:
                self.parent[self.find(index1)] = self.find(index2)
                self.rank[index2] +=1
                

    def equationsPossible(self, equations):
        uf = Solution.UnionFind()
        # 找出所有等于关系的字母
        # 将有相同根节点的数字构成一颗树
        # 得到若干棵不同根的树
        for st in equations:
            if st[1] == "=":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                uf.union(index1, index2)
        
        # 找到所有不等关系的字母
        # 若判断两个不等关系的字母，是否在根相同的一棵树中
        # 若在同一根的数中则返回false 
        for st in equations:
            if st[1] == "!":
                index1 = ord(st[0]) - ord("a")
                index2 = ord(st[3]) - ord("a")
                if uf.find(index1) == uf.find(index2):
                    return False
        return True






