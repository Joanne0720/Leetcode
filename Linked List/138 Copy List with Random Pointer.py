# 拷贝的意思是每当遇到一个新的未访问过的节点，你都需要创造一个新的节点。

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}

        def DFS(node):
            if node is None:
                return None
            if node in visited:
                return visited[node]
            # create a new node
            # with the value same as old node.
            clone = Node(node.val, None, None)
            visited[node] = clone
            clone.next = DFS(node.next)
            clone.random = DFS(node.random)
            return clone

        return DFS(head)



# 方法二：旧节点和新节点交错的方法，不需要额外空间
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        cur = head
        # Cloned node,weaving, A->B->C: A->A'->B->B'->C->C'
        while cur:
            clone = Node(cur.val)
            clone.next, cur.next = cur.next, clone
            cur = clone.next
        cur = head
        # link the random pointers
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        # Unweave the linked list, A->A'->B->B'->C->C': A->B->C and A'->B'->C'
        newHead = head.next
        old, new = head, head.next
        while old:
            old.next = old.next.next
            new.next = new.next.next if new.next else None
            old, new = old.next, new.next
        return newHead