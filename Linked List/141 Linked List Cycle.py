# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        # 用哈希表记录法
        # if head == None:
        #     return False
        #
        # target = {head}
        # cur = head
        # while cur.next:
        #     cur = cur.next
        #     if cur in target:
        #         return True
        #     else:
        #         target.add(cur)
        # return False

        # 快慢指针法, 慢指针每次移动一步，而快指针每次移动两步.
        # 如果没有环，快指针将停在链表的末尾。
        # 如果有环，快指针最终将与慢指针相遇。
        if head is None:
            return False
        fast = head.next
        slow = head
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
