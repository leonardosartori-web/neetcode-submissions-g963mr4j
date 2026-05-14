class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        curr = intervals[0] # [1, 5]
        res = deque()
        for start, end in intervals:
            if start <= curr[1]:
                curr[1] = max(curr[1], end)
            else:
                res.append(curr)
                curr = [start, end]
        res.append(curr)
        return list(res)