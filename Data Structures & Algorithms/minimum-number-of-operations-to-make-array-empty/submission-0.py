class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        res = 0
        for e, cnt in count.items():
            if cnt < 2:
                return -1
            res += math.ceil(cnt / 3)
        return res
            