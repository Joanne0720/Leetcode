# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = head
            head = nxt
        return head