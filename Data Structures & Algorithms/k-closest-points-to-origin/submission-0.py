class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [[(x*x + y*y), x, y] for x, y in points ]
        heapq.heapify(distances)
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(distances)
            res.append([x, y])
            k -= 1
        return res