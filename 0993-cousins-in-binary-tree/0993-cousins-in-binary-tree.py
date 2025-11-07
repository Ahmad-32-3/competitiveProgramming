# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = collections.deque()
        q.append((root, None))
        level = 0
        x_res = (None, None)
        y_res = (None, None)
        while q:
            qlen = len(q)
            for i in range(qlen):
                node, parent = q.popleft()
                if node:
                    if node.val == x:
                        x_res = (level, parent)
                    if node.val == y:
                        y_res = (level, parent)
                    q.append((node.left, node))
                    q.append((node.right, node))
            if x_res[0] == y_res[0] and x_res[1] != y_res[1]:
                return True
            level += 1
        return False

                    


            


