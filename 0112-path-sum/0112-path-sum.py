# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        flag = False
        def dfs(node, sum):
            nonlocal flag
            if not node.left and not node.right:
                if sum == targetSum:
                    flag = True
                return
            
            if node.left:
                dfs(node.left, sum + node.left.val)
            if node.right:
                dfs(node.right, sum + node.right.val)
        dfs(root, root.val)
        return flag
            