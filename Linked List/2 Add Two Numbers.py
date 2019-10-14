"""
求和运算最后可能出现额外的进位，这一点很容易被遗忘!
最后检查 carry=1 是否成立，如果成立，则向返回列表追加一个含有数字 1 的新结点。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyhead = ListNode(0)
        pre = dummyhead
        carry = 0
        while l1 or l2:
            p = l1.val if l1 else 0
            q = l2.val if l2 else 0
            pre.next = ListNode((carry + p + q) % 10)
            carry = (carry + p + q) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            pre = pre.next
        if carry > 0:
            pre.next = ListNode(carry)
        return dummyhead.next