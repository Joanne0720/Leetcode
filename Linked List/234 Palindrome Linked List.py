# 链表找中点的方法：快慢指针，快指针到达尾部，慢指针到达中间
# 一边头插法，一边移动两个指针

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
