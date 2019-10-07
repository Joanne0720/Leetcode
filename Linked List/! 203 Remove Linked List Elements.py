"""
法1：找到第一个不为val的结点作为头结点,定义两个指针进行删除操作;
法2：定义一个新链表指向head结点,进行删除操作;
法3：递归的从后往前进行删除操作;
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head