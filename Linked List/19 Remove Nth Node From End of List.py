# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast, slow = head, head
        # 找到要删除的节点的前面一个节点
        for _ in range(n):
            fast = fast.next
        # 可能一共只有n个节点，即删除头结点
        if fast is None:
            head = head.next
            return head
        while fast.next:
            fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head