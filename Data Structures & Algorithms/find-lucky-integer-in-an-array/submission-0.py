class Solution:
    def findLucky(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        res = -1
        for e, freq in cnt.items():
            if e == freq:
                res = max(res, e)
        return res