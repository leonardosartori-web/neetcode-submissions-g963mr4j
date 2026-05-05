"""
import copy
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(node):
            if node in seen:
                return seen[node]
            
            newN = Node(node.val)
            seen[node] = newN
            for neighbor in node.neighbors:
                newN.neighbors.append(dfs(neighbor))
            return newN
        return dfs(node) if node else None