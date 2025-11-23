# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        arr = []

        def dfs(node, flag):
            nonlocal arr
            if not node:
                return
            dfs(node.left, True)
            if not node.left and not node.right and flag:
                arr.append(node.val)
            dfs(node.right, False)
            

        dfs(root, flag = False)
        res = 0
        for val in arr:
            res += val
        return res