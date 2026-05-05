# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            
            l, r = max(dfs(node.left), 0), max(dfs(node.right), 0)

            res[0] = max(res[0], node.val + l + r)
            return node.val + max(l, r)
        
        dfs(root)
        return res[0]