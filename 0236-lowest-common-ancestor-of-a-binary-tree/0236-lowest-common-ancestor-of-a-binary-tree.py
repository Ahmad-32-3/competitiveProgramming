# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        res = None
        def dfs(node, p, q):
            nonlocal res
            if not node:
                return None, False, False

            left_node, fp_left, fq_left = dfs(node.left, p, q)
            right_node, fp_right, fq_right = dfs(node.right, p, q)         
            
            fp = fp_left or fp_right or node == p
            fq = fq_left or fq_right or node == q

            
            if fp and fq and not res:
                res = node
            
            return node, fp, fq
        
        node, _, _ = dfs(root, p, q)
        return res
            
