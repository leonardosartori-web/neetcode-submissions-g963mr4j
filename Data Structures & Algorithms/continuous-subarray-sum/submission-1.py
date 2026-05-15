class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        cnt = {0: -1}
        for i, n in enumerate(nums):
            prefix += n
            r = prefix % k
            if r not in cnt:
                cnt[r] = i
            elif i - cnt[r] > 1:
                return True
        return False