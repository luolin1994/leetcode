# --coding:utf8 --
# 21 合并两个有序链表
#将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的
# 知识点：链表  递归

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:


    #判断大小，排序
    def mergeTwoLists(self,l1:ListNode,l2:ListNode) -> ListNode:

        new = ListNode(0) #不用重新获取头节点
        curr = new
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next

        if l1 == None:
            curr.next = l2
        else:
            curr.next = l1



        return new.next

    # 递归
    # if l1[0] < l2[0]    l1[0] + merge(l1[1:],l2)
    # else                l2[0] + merge(l1,l2[1:])
    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1,l2.next)
            return l2





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

node111 = None
node222 = ListNode(0)

solution = Solution()

print(solution.mergeTwoLists2(node11,node21).val)