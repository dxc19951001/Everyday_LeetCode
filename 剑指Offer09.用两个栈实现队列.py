class CQueue:
    # 核心思想
    # 1.栈无法实现队列功能： 栈底元素（对应队首元素）无法直接删除，需要将上方所有元素出栈。
    # 2.双栈可实现列表倒序： 设有含三个元素的栈 A = [1,2,3]和空栈 B = []。
    # 若循环执行 A 元素出栈并添加入栈 B ，直到栈 A为空，则 A = [], B = [3,2,1]，即 栈 B元素实现栈 A元素倒序。
    # 3.利用栈 B 删除队首元素： 倒序后，B执行出栈删除B栈对顶元素，则相当于删除了A的栈底元素，即对应队首元素。

    # 函数设计
    # 函数设计：
    # 题目只要求实现 加入队尾appendTail() 和 删除队首deleteHead() 两个函数的正常工作，
    # 因此我们可以设计栈 A 用于加入队尾操作，栈 B 用于将元素倒序，从而实现删除队首元素。

    # 加入队尾 appendTail()函数： 将数字 val 加入栈 A 即可。
    # 删除队首deleteHead()函数： 有以下三种情况。
    #   当栈 B 不为空： B中仍有已完成倒序的元素，因此直接返回 B 的栈顶元素。
    #   否则，当 A 为空：没有元素可删除了， 即两个栈都为空，无元素，因此返回 -1。
    #   否则： 将栈 A 元素全部转移至栈 B 中，实现元素倒序，并返回栈 B 的栈顶元素。

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()