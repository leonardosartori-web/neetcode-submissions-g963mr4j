# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered_tree = []

        def dfs(root: Optional[TreeNode]):
            if len(ordered_tree) == k:
                return ordered_tree[-1]
            if not root:
                return
            dfs(root.left)
            ordered_tree.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return ordered_tree[k-1]