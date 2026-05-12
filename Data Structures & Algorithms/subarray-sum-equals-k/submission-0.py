class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Idea: at every moment we have the sum(0, i) = S
        # If we have seen S - k => the interval sum to k
        prefix = 0
        res = 0
        prefixCounts = {0: 1}
        for n in nums:
            prefix += n
            diff = prefix - k
            if diff in prefixCounts:
                res += prefixCounts[diff]
            prefixCounts[prefix] = prefixCounts.get(prefix, 0) + 1
        return res
            
