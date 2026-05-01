class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = cnt = 0

        for n in nums:
            if cnt == 0:
                curr = n
            cnt += 1 if curr == n else -1
        return curr