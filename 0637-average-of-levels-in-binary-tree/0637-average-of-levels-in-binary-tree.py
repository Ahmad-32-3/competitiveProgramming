# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = collections.deque()

        average = []
        

        q.append(root)

        while q:
            level = []
            qlen = len(q)
            tot = 0

            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            for e in level:
                tot += e

            if len(level) != 0:
                average.append(tot/(len(level)))

        return average