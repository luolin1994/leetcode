# --coding:utf-8 --
# 19 删除链表的倒数第N个节点
# 给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
# 说明：给定的n保证是有效的
# 进阶：尝试使用一次扫描实现

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        return ListNode(0)