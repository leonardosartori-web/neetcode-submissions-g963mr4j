class Solution:
    def climbStairs(self, n: int) -> int:
        res1, res2 = 0, 1

        while n > 0:
            tmp = res1 + res2
            res1 = res2
            res2 = tmp
            n -= 1
        return res2
