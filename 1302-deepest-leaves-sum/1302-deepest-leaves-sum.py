# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        if root is None:
            return 0

        while q:
            res = 0
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    res += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        return res