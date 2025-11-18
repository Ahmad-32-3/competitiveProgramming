# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return []

        def dfs(node, path, total):
            if not node.left and not node.right:
                if total == targetSum:
                    res.append(path)
            
            if node.left:
                new_path = path + [node.left.val]
                dfs(node.left, new_path, total + node.left.val)
            if node.right:
                new_path = path + [node.right.val]
                dfs(node.right, new_path, total + node.right.val)
        
        dfs(root, [root.val], root.val)
        return res