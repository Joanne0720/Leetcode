"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            if cur.child:
                _nxt = cur.next
                cur.next = self.flatten(cur.child)
                cur.next.prev = cur
                cur.child = None
                while cur.next:
                    cur = cur.next
                cur.next = _nxt
                if _nxt:
                    _nxt.prev = cur
            cur = cur.next
        return head
