class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        occ = [0] * 26

        for e in s:
            occ[ord(e)-ord('a')] += 1
        
        for e in t:
            occ[ord(e)-ord('a')] -= 1
        
        for e in occ:
            if e > 0:
                return False
        return True