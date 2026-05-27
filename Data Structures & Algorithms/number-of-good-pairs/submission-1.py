class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for e, cnt in count.items():
            res += (cnt * (cnt - 1)) // 2
        return res