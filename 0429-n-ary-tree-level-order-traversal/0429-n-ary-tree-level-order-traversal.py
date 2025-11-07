"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res= []
        while q:
            level = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    for i in range(len(node.children)):
                        q.append(node.children[i])
            if level:
                res.append(level)

        return res