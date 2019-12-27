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

   #扫描两次
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        #第一次扫描，统计链表的长度
        length = 0
        curr1 = head
        while curr1:
            length += 1
            curr1= curr1.next

        if n == length:
            return head.next
        #第二次扫描，删除节点
        curr2 = head
        i = 0
        while curr2:
            i += 1
            if i == length -n:
                curr2.next = curr2.next.next
                break
            curr2 = curr2.next  #第一次忘记了
        return head

    # 一次扫描，用数组存放
    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        curr = head
        temp = []
        while curr:
            temp.append(curr)
            curr = curr.next
        length = len(temp)

        if n == length:
            return head.next
        change = temp[length - n -1]
        change.next = change.next.next
        return head

    # 快慢指针，先让p1走n步，然后p1,p2一起走，快指针比慢指针先行n步，快指针到底部时，慢指针所处位置为i删除位置
    def removeNthFromEnd3(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head

        for i in range(n):
            fast = fast.next

        if fast == None:
            return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head




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

solution = Solution()


print(solution.removeNthFromEnd3(node1 ,6).val)