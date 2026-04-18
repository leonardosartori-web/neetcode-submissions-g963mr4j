class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = l + ((r - l) // 2)

            d = nums[m] - target

            if not d:
                return m
            elif d > 0:
                r = m
            else:
                l = m + 1
        return -1

        