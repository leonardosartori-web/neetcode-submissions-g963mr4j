# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        nodes = []
        def serialize(root: Optional[TreeNode]):
            if not root:
                return "null"
            else:
                nodes.append("#" + str(root.val))
                return "#" + str(root.val) + serialize(root.left) + serialize(root.right)
        
        subs = serialize(root).split(serialize(subRoot))
        return len(subs) > 1
