class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def helper(index: int):
            prev = ""
            for s in strs:
                if index < len(s):
                    if prev:
                        if s[index] != prev:
                            return ""
                    else:
                        prev = s[index]
                else:
                    return ""
            return prev + helper(index + 1)
        return helper(0)