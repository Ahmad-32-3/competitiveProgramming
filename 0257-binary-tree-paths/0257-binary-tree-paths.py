# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        result = []

        def dfs(node, path):
            # If this node is a leaf, we finalize the path
            if not node.left and not node.right:
                result.append(path)
                return

            # If left child exists → continue path
            if node.left:
                dfs(node.left, path + "->" + str(node.left.val))

            # If right child exists → continue path
            if node.right:
                dfs(node.right, path + "->" + str(node.right.val))

        # Start DFS with the root value as the initial path
        dfs(root, str(root.val))
        return result
