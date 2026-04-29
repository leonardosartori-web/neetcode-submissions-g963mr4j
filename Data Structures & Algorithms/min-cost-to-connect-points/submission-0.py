class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        seen = set()
        min_dist = [float("inf")] * n

        heap = [(0, 0)]
        res = 0

        while heap:
            cost, u = heapq.heappop(heap)

            if u not in seen:
                seen.add(u)
                res += cost
                x1, y1 = points[u]

                for v in range(n):
                    if v not in seen:
                        x2, y2 = points[v]
                        dist = abs(x1-x2) + abs(y1-y2)

                        if dist < min_dist[v]:
                            min_dist[v] = dist
                            heapq.heappush(heap, (dist, v))
        return res
