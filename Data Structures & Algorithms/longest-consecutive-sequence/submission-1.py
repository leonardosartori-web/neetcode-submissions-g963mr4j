class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        res = 0

        for n in seen:
            # Only case that can be the start of a sequence
            if n - 1 not in seen:
                curr_count, curr_value = 1, n
                while curr_value + 1 in seen:
                    curr_count += 1
                    curr_value += 1
                res = max(res, curr_count)
        return res