class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        chars = set(allowed)
        for word in words:
            for c in word:
                if c not in chars:
                    res -= 1
                    break
            res += 1
        return res
