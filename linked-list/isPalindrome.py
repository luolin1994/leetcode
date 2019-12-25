# -- coding:utf8--
#234 回文链表
#请判断一个链表是否为回文链表。
#进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    # 遍历存入数组中，用双指针法检索
    #时间复杂度O(n)   空间复杂度O(n)
    def isPalindrome(self,head:ListNode) -> bool:
        curr = head
        t = []
        while curr:
            t.append(curr.val)
            curr = curr.next

        start = 0
        end = len(t) -1
        while start != end and start < end:
            if t[start] != t[end]:
                return False
            start += 1
            end -= 1

        return True


    # 使用快慢指针找到中点，reverse 逆序后半部分，从头、中点，开始比较是否相同
    # 快指针每次走俩步，则快指针到头时，慢指针恰好在中点
    def isPalindrome2(self,head:ListNode) -> bool:
        fast = head
        low = head
        while fast and fast.next:
            fast = fast.next.next
            low = low.next
        # 若长度为奇数，则翻转的起点位置加1
        if fast:
            low = low.next

        # 逆序后半部分
        curr = low
        new_mid = None
        while curr:
            curr , new_mid , new_mid.next = curr.next, curr , new_mid

        start = head
        while new_mid:
            if new_mid.val != start.val:
                return False
            else:
                new_mid = new_mid.next
                start = start.next

        return True




node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)
node6 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
#node5.next = node6
solution = Solution()


print(solution.isPalindrome2(node1))