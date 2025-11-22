# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 1
        compare = root.val
        if not root:
            return 0
        def dfs(node):
            nonlocal counter
            if not node:
                return None 
            
            left = dfs(node.left)
            right = dfs(node.right)
            flag = True
            if left:
                if left >= compare:
                    counter += 1
                    flag = False
            if right: 
                if right >= compare and flag:
                    counter += 1
            print("counter:", counter)
            return node.val
        
        dfs(root)
        return counter