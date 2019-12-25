# --coding:utf8 --
# 141 环形链表
#给定一个链表，判断链表中是否有环。
#为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#进阶：用O(1)的空间复杂度来解决问题

class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def hasCycle(self,head:ListNode) -> bool:

        return  False


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6