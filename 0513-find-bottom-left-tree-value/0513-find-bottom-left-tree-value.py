# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        res = []
        while q:
            qlen = len(q)
            counter = 0
            for i in range(qlen):
                node = q.popleft()
                if node:
                    counter += 1
                    q.append(node.left)
                    q.append(node.right)
                if node and counter == 1:
                    res.append(node.val)
        return res[len(res) - 1]
