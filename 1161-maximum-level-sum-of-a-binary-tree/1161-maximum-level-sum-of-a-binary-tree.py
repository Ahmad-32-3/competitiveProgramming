# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        q.append(root)
        res = 0
        level = 1
        max_sum = float('-inf')

        while q:
            qlen = len(q)
            currSum = 0
            
            for i in range(qlen):
                node = q.popleft()
                
                if node:
                    currSum += node.val
                    level += 1
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            if currSum > max_sum:
                max_sum = currSum
                res = level
        return res
