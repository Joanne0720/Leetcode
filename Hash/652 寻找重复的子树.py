"""
序列化二叉树：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串。
需要注意的是，序列化二叉树的过程中，如果遇到空节点，需要以某种符号（#）表示。
"""
from collections import defaultdict


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        d = defaultdict(list)
        def dfs(root):
            if not root:
                return ''
            s = ' '.join((str(root.val), dfs(root.left), dfs(root.right)))
            d[s].append(root)
            return s
        dfs(root)
        return [r[0] for r in d.values() if len(r) > 1]