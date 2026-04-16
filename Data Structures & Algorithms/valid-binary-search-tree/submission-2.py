# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValidBSTAux(root: Optional[TreeNode], lowerbound: float, upperbound: float):
            
            if not root:
                return True
            
            if root.val >= upperbound or root.val <= lowerbound:
                return False
            
            return isValidBSTAux(root.left, lowerbound, root.val) and isValidBSTAux(root.right, root.val, upperbound)
        
        return isValidBSTAux(root, float("-inf"), float("inf"))
        