# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        def dfs(node, ork):
            print(node.val)
            if not node.left and not node.right:
                res.append(ork)
                return
            
            if node.left:
                dfs(node.left, ork + str(node.left.val))
            if node.right:
                dfs(node.right, ork + str(node.right.val))
        
        dfs(root, str(root.val))
        tot = 0
        for i in range(len(res)):
            tot += int(res[i])
        return tot