class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Idea: dfs two side: include nums[i] or skip
        res = []

        def dfs(i: int, curr: List[int], totalCurr: int):
            if totalCurr == target:
                res.append(curr[:])
                return
            if i >= len(nums) or totalCurr > target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, totalCurr + nums[i])
            curr.pop()
            dfs(i+1, curr, totalCurr)
        dfs(0, [], 0)
        return res