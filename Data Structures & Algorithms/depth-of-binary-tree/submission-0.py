# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mx_l = self.maxDepth(root.left)
        mx_r = self.maxDepth(root.right)
        return max(mx_l, mx_r) + 1