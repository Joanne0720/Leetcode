# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == []:
            return []
        result = []
        visited, s = set(), [root]
        while s:
            cur = s[-1]
            if cur.left and cur.left not in visited:
                s.append(cur.left)
                visited.add(cur.left)
            else:
                result.append(cur.val)
                s.pop()
                if cur.right:
                    s.append(cur.right)
                    visited.add(cur.right)
        return result