class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        mx = curr = curr_v = 0

        for num in seen:
            if num - 1 not in seen:
                curr = 1
                curr_v = num
                while curr_v + 1 in seen:
                    curr += 1
                    curr_v += 1
                mx = max(mx, curr)
        return mx
