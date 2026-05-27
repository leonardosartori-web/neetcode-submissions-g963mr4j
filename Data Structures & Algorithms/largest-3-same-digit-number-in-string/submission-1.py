class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr, l = "", 0
        resC = ""
        for c in num:
            if curr == c:
                l += 1
            else:
                curr = c
                l = 1
            if l == 3 and (resC == "" or resC < c):
                resC = c
        return resC * 3
        