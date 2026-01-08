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
            qlen = len(q)
            
            currAve = 0
            for i in range(qlen):
                node = q.popleft()
                currAve += node.val
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            average.append(currAve / qlen)
        return average