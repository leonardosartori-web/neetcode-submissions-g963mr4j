class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = res = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                curr = 0
            curr += nums[i]
            res = max(res, curr)
        return res