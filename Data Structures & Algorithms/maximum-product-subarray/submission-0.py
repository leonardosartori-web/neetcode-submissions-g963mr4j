class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)

        mx, mn = 1, 1
        for n in nums:
            currMax, currMin = mx * n, mn * n
            mx = max(currMin, currMax, n)
            mn = min(currMin, currMax, n)
            res = max(res, mx)
        return res