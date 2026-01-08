# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        res = None

        def dfs(node, pflag, qflag):
            nonlocal res

            if not node:
                return False, False

            left_p, left_q = dfs(node.left, pflag, qflag)
            right_p, right_q = dfs(node.right, pflag, qflag)

            if node.val == p.val:
                pflag = True
            if node.val == q.val:
                qflag = True

            pflag = pflag or left_p or right_p
            qflag = qflag or left_q or right_q

            if pflag and qflag and res is None:
                res = node

            return pflag, qflag

        dfs(root, False, False)
        return res

            
