class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        cntT, window = {}, {}

        for c in t:
            cntT[c] = cntT.get(c, 0) + 1
        
        windowCommonCharSize, tLen = 0, len(cntT)
        l = 0
        res, resLen = [-1, -1], float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in cntT and window[c] == cntT[c]:
                windowCommonCharSize += 1
            
            while windowCommonCharSize == tLen:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in cntT and window[s[l]] < cntT[s[l]]:
                    windowCommonCharSize -= 1
                l += 1
        return s[res[0]: res[1]+1] if resLen != float("inf") else ""