# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(r: Optional[TreeNode]):
            if not r:
                return [True, 0]
            sx = dfs(r.left)
            dx = dfs(r.right)
            balanced = sx[0] and dx[0] and abs(sx[1] - dx[1]) < 2

            return [balanced, max(sx[1], dx[1]) + 1]
        return dfs(root)[0]