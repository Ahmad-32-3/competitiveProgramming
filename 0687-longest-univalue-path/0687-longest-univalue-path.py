# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        maxCounter = 0
        def dfs(node):
            nonlocal maxCounter
            if not node:
                return 0
            
            
            left = dfs(node.left)
            
            right = dfs(node.right)

            leftOrk = 0
            rightOrk = 0
            if node.left and node.left.val == node.val:
                leftOrk = left + 1
            if node.right and node.right.val == node.val:
                rightOrk = right + 1
            
            maxCounter = max(maxCounter, leftOrk + rightOrk)

            return max(leftOrk,rightOrk)
        dfs(root)
        return maxCounter