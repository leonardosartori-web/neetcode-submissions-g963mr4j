class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            if n == 1:
                return True
            seen.add(n)
            newN = 0
            while n:
                d = n % 10
                d *= d
                newN += d
                n //= 10
            n = newN
        return False