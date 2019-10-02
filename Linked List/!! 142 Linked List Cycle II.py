"""
Floyd 算法.
在第一阶段，找出列表中是否有环，如果没有环，可以直接返回 null 并退出。否则，用 相遇节点 来找到环的入口。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 找到相遇点: 快指针和慢指针。如果快慢指针指向了同一个节点，返回它。直到 while 循环终止且没有返回任何节点，这种情况说明没有成环，返回 null 。
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast is None or fast.next is None:
            return None
        # 找到环的入口: 两个指针： ptr1 ，指向链表的头， ptr2 指向相遇点。然后，我们每次将它们往前移动一步，直到它们相遇，它们相遇的点就是环的入口，返回这个节点。
        ptr1, ptr2 = head, slow
        while ptr1 != ptr2:
            ptr1, ptr2 = ptr1.next, ptr2.next
        return ptr1