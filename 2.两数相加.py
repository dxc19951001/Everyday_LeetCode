class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # 核心思想：
        # 类似加法的原理, 我们从低位（链条第一位）开始，同位相加，满10高位+1
        # 当两个链表和进位都为0时，则退出

        # 设置头节点 ans = ListNode(0)
        # 设置一个中间变量tmp，tmp = ans
        # tmp和ans此时同时指向 ListNode(0)，共用一片内存空间
        # 在计算一位加法完成后，得出值为x，则tmp = ans = ListNode(x)
        # 设置tmp的下一个节点tmp.next,并令其值为ListNode(0) ,即ListNode(x).next= ListNode(0)
        # 即tmp.next = ListNode(0) ，tmp和ans共有一片内存空间，则ans.next=ListNode(0) 
        # tmp向后移动，令 tmp = tmp.next，此时ans和tmp不相等了，ans.next = tmp
        
        # 再进行依次加法运算，得出值为x1，则tmp = ListNode(x1)
        # 设置tmp的下一个节点tmp.next,并令其值为ListNode(0) 
        # 即tmp.next = ListNode(0)，即ListNode(x1).next= ListNode(0)
        # 再使tmp向后移动，令 tmp = tmp.next，

        # 此时构建出链表：ListNode(x)-->ListNode(x1)-->ListNode(0) 
        
        # 先设置tep的下一个节点的值，再令tmp = tmp.next，tmp向后移动
        # 以此类推构建出一条列表


        ans = ListNode(0)   # 头结点，无存储，指向链表第一个结点
        tmp = ans # 初始化链表结点
        tmpsum = 0  # 初始化 进一 的数

        while True:
            # 依次遍历l1 l2，对应位相加
            if l1 != None:
                tmpsum += l1.val
                l1 = l1.next
            if l2 != None:
                tmpsum += l2.val
                l2 = l2.next
            tmp.val = tmpsum % 10     # 除10取余作为当前位的值
            tmpsum //= 10                #除10取整，即高位，作为指针的下个结点 进行加法运算
            if l1 == None and l2 == None and tmpsum == 0:
                break
            tmp.next = ListNode(0)  
            # 指向链表的下一位，这个值随意，在tmp.val = tmpsum % 10会改变这个值
            tmp = tmp.next  # 更新指针，往后移动
        return ans



var1 = ListNode(2)
var2 = ListNode(4)
var3 = ListNode(3)

var1.next = var2
var2.next = var3
# var3.next = None


var4 = ListNode(5)
var5 = ListNode(6)
var6 = ListNode(4)

var4.next = var5
var5.next = var6
# var6.next = None

result = Solution().addTwoNumbers(var1, var4)

print(result.val)
print(result.next.val)
print(result.next.val)

while result:
    if result is not None:
        print(result.val)
        result = result.next