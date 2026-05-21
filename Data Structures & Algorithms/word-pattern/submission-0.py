class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def help_(a, b):
            if len(a) != len(b):
                return False
            seen = {}
            for i in range(len(a)):
                if a[i] in seen:
                    if b[i] != seen[a[i]]:
                        return False
                else:
                    seen[a[i]] = b[i]
            return True
        return help_(pattern, s.split(" ")) and help_(s.split(" "), pattern)