# 237 删除链表中的节点
#请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
#说明:链表至少包含两个节点。
# 链表中所有节点的值都是唯一的。
# 给定的节点为非末尾节点并且一定是链表中的一个有效节点。
# 不要从你的函数中返回任何结果。
#输入: head = [4,5,1,9], node = 5
#输出: [4,1,9]
#解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

class Node:

    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteNode(self,node):
        node.val = node.next.val
        node.next = node.next.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

solution = Solution()
solution.deleteNode(node2)
print(node1.next.val)


