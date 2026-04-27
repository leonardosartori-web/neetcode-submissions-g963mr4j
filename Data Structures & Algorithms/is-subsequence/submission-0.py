class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        n, m = len(t), len(s)
        while i < n and j < m:
            if s[j] == t[i]:
                j += 1
            i += 1
        return j == m