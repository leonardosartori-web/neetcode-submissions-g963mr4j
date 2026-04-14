class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_1, rob_2 = 0, 0

        for num in nums:
            newRob = max(rob_2, rob_1+num)
            rob_1 = rob_2
            rob_2 = newRob
        return rob_2