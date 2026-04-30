class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = list(range(n))
        rank = [0] * n

        def find(e):
            if parents[e] != e:
                parents[e] = find(parents[e])
            return parents[e]

        def union(u, v):
            rU = find(u)
            rV = find(v)

            if rU == rV:
                return False

            if rank[rU] < rank[rV]:
                parents[rU] = rV
            elif rank[rV] < rank[rU]:
                parents[rV] = rU
            else:
                parents[rU] = rV
                rank[rV] += 1
            return True
        
        res = n
        for u,v in edges:
            res -= 1 if union(u, v) else 0
        
        return res