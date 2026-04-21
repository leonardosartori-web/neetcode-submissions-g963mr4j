class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False

        parents = list(range(n))

        def find(e):
            if parents[e] != e:
                parents[e] = find(parents[e])
            return parents[e]
        
        def union(x, y):
            rX = find(x)
            rY = find(y)

            if rX == rY:
                return False

            parents[rY] = rX
            return True

        for u,v in edges:
            if not union(u, v):
                return False
        return True