# --coding:utf8--
# 206 反转链表
# 反转一个单链表

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    # 迭代
    def reverseList(self,head:ListNode) -> ListNode:

        temp = None
        while head:
           head, temp , temp.next = head.next , head , temp

        return temp

    #递归解决方法
    def reverseList2(self, head: ListNode) -> ListNode:

        # 递归终止条件是当前为空，或者下一个节点为空
        if (head == None or head.next == None):
            return head
        # 这里的cur就是最后一个节点
        cur = self.reverseList2(head.next)
        # 这里请配合动画演示理解
        # 如果链表是 1->2->3->4->5，那么此时的cur就是5
        # 而head是4，head的下一个是5，下下一个是空
        # 所以head.next.next 就是5->4
        head.next.next = head
        # 防止链表循环，需要将head.next设置为空
        head.next = None
        # 每层递归函数都返回cur，也就是最后一个节点
        return cur


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


solution = Solution()
print(solution.reverseList(node1).val)
