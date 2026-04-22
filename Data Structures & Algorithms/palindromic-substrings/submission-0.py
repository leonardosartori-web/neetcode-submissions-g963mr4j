class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)

        for i in range(n):
            # Two times cause before check odd then even
            for k in range(2):
                l, r = i, i + k
                while l >= 0 and r < n and s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
        return res