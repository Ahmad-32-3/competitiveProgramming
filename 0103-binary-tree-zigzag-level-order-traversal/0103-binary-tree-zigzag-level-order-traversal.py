# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        level = 0
        res = []
        while q:
            level += 1
            subarray = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    subarray.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if subarray:
                if level % 2 == 0:
                    res.append(subarray[::-1])
                else:
                    res.append(subarray)
        return res
