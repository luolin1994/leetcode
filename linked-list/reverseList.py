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

        pre = None
        cur = head
        while cur:
            # # 记录当前节点的下一个节点
            # tmp = cur.next
            # # 然后将当前节点指向pre
            # cur.next = pre
            # # pre和cur节点都前进一位
            # pre = cur
            # cur = tmp

            print(cur)
            pre , cur , cur.next = cur , cur.next , pre
            #注意：python多元赋值的顺序为，先计算等式右边的值进行存储，再从左到右进行赋值，因此对最后的cur.next进行赋值时的cur已经被赋予了cur.next

        return pre

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
