class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        counterT = Counter(t)
        window = {}

        windowCommonChars = 0
        tDifferntChars = len(counterT)

        l = 0
        res, resLen = [-1, -1], float("inf")
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            if char in counterT and window[char] == counterT[char]:
                windowCommonChars += 1
            while windowCommonChars == tDifferntChars:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in counterT and window[s[l]] < counterT[s[l]]:
                    windowCommonChars -= 1
                l += 1
        return s[res[0]:res[1]+1] if resLen != float("inf") else ""
        