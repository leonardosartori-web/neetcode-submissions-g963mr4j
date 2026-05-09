class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def help(a, b):
            seen = {}

            for i in range(len(a)):
                if a[i] not in seen:
                    seen[a[i]] = b[i]
                else:
                    if seen[a[i]] != b[i]:
                        return False
            return True
        
        return help(s, t) and help(t, s)