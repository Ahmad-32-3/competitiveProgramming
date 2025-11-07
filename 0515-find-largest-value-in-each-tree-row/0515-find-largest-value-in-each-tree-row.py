# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            qlen = len(q)
            oak = float("-inf")
            for i in range(qlen):
                node = q.popleft()
                if node:
                    oak = max(oak, node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if root:
                res.append(oak)
        return res