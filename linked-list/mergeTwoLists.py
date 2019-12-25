# 21 合并两个有序链表
#将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self,l1:ListNode,l2:ListNode) -> ListNode:

        node = ListNode(1)
        return node


node11 = ListNode(1)
node12 = ListNode(2)
node13 = ListNode(4)
node11.next = node12
node12.next = node13

node21 = ListNode(1)
node22 = ListNode(3)
node23 = ListNode(4)
node21.next = node22
node22.next = node23