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
    def isPalindrome2(self,head:ListNode) -> bool:


        return False



node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(2)
node5 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
solution = Solution()

print(solution.isPalindrome(node1))