# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        count = 1
        cur = head
        while cur.next:
            cur = cur.next
            count += 1
        cur.next = head

        cur = head
        for _ in range(count - k % count - 1):
            cur = cur.next
        newhead = cur.next
        cur.next = None
        return newhead