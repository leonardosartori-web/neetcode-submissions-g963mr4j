class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Idea: dynamic programming: at every moment add and subtract num
        # to each sum already seen
        dp = defaultdict(int)
        dp[0] = 1
        
        for n in nums:
            tmpDp = defaultdict(int)
            for sum_, count in dp.items():
                tmpDp[sum_ + n] += count
                tmpDp[sum_ - n] += count
            dp = tmpDp
        return dp[target]