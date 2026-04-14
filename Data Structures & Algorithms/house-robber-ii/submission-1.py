class Solution:
    def rob(self, nums: List[int]) -> int:
        def linearRob(nums: List[int]):
            rob1, rob2 = 0, 0
            for e in nums:
                tmp = max(rob2, e + rob1)
                rob1 = rob2
                rob2 = tmp
            return rob2
        return max(nums[0], linearRob(nums[1:]), linearRob(nums[:-1]))