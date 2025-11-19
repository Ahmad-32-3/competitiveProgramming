# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        flag = True
        def dfs(node, target):
            nonlocal flag
            if node.val != target:
                flag = False
            
            if node.left:
                dfs(node.left, target)
            if node.right:
                dfs(node.right, target)

        dfs(root, root.val)
        return flag