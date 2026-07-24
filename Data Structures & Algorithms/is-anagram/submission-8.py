class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cntS, cntT = Counter(s), Counter(t)
        return cntS == cntT