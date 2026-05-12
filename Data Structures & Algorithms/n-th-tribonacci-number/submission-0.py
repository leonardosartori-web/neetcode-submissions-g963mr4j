class Solution:
    def tribonacci(self, n: int) -> int:
        fib1, fib2, fib3 = 0, 1, 1
        for _ in range(n):
            tmp = fib1 + fib2 + fib3
            fib1 = fib2
            fib2 = fib3
            fib3 = tmp
        return fib1