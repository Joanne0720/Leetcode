# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        odd, even, evenHead = head, head.next, head.next
        while even and even.next:
            odd.next = even.next
            even.next = even.next.next
            odd, even = odd.next, even.next
        odd.next = evenHead
        return head