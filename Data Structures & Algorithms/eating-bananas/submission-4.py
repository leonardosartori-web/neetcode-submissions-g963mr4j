class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = 0
        for p in piles:
            mx = max(mx, p)
        l, r = 1, mx
        res = r
        while l<=r:
            m = (l+r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            if hours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res