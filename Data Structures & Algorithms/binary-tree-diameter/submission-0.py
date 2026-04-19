# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(r):
            nonlocal res

            if not r:
                return 0
            sx = dfs(r.left)
            dx = dfs(r.right)
            res = max(res, sx + dx)

            return 1 + max(sx, dx)
        dfs(root)
        return res
