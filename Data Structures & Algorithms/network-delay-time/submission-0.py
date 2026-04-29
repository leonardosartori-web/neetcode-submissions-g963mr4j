class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dists = {node: float("inf") for node in range(1, n+1)}
        dists[k] = 0

        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        q = [(0, k)]

        while q:
            curr_distance, curr_node = heapq.heappop(q)

            if dists[curr_node] >= curr_distance:
                for neighbor, weight in graph[curr_node]:
                    n_dist = curr_distance + weight

                    if n_dist < dists[neighbor]:
                        dists[neighbor] = n_dist
                        heapq.heappush(q, (n_dist, neighbor))
            
        max_dist = max(dists.values())
        return max_dist if max_dist != float("inf") else -1