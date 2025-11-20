# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        freq = collections.defaultdict(int)
        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            total = left + right + node.val
            freq[total] += 1
            return total
        
        dfs(root)
        most = 0
        res = []
        for i in freq:
            most = max(most,freq[i])
        for i in freq:
            if freq[i] == most:
                res.append(i)
        return res
