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