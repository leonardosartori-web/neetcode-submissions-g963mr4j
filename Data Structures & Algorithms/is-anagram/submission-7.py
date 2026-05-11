class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Idea: we count the occurencies of every char in s (+1) and t (-1): if a char has more than 
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