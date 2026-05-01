class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, mx = 0, 0
        for n in nums:
            if n:
                curr += 1
            else:
                curr = 0
            mx = max(mx, curr)
        return mx