# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        absMin = float('inf')

        if not root:
            return 0
        prev = None
        def dfs(node):
            nonlocal absMin, prev
            if not node:
                return None
            dfs(node.left)
            if prev:
                absMin = min(absMin, abs(prev - node.val))
            prev = node.val
            dfs(node.right)
        dfs(root)
        return absMin

            