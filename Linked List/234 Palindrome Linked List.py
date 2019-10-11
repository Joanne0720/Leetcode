# 链表找中点的方法：快慢指针，快指针到达尾部，慢指针到达中间
# 一边反转前半部分(此解用头插法)，一边移动两个指针

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        fast, slow, prev = head.next, head, head
        while fast and fast.next:
            slow, fast = prev.next, fast.next.next
            prev.next = slow.next
            slow.next = head
            head = slow
        # 长度是单数的情况：
        if fast is None:
            head = head.next
        # 对比
        slow = prev.next
        while slow:
            if head.val != slow.val:
                return False
            head, slow = head.next, slow.next
        return True
