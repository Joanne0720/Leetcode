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
        childhead, cur = head, head
        while cur:
            if cur.child:
                nxt = cur.next
                cur.next, childtail = self.flatten(cur.child)
                cur.next.prev = cur
                cur.child = None
                childtail.next, nxt.prev = nxt, childtail
                cur = nxt
            else:
                cur = cur.next
        return childhead, cur.prev
