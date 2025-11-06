# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        res = 0

        q.append((root, 1))

        if not root:
            return 0
        while q:
                node, depth = q.popleft()

                if node:

                    if not node.left and not node.right:
                        return depth
                    q.append((node.left, depth + 1))
                    q.append((node.right, depth + 1))