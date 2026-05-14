class Solution:
    def reverse(self, x: int) -> int:
        orig = x
        x = abs(x)
        res = int(str(x)[::-1])
        if orig < 0:
            res = -res
        if res < -(1 << 31) or res > (1 << 31) - 1:
            return 0
        return res