class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n * (n + 1) // 2
        for e in nums:
            res -= e
        return res