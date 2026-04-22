class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        sub_n = len(s1)

        if n < sub_n:
            return False
        
        cnt_sub = [0] * 26
        cnt_s2 = [0] * 26
        
        for c in s1:
            cnt_sub[ord(c) - ord("a")] += 1
        
        for i in range(sub_n):
            cnt_s2[ord(s2[i]) - ord("a")] += 1

        match = 0        
        for i in range(26):
            if cnt_sub[i] > 0 and cnt_sub[i] == cnt_s2[i]:
                match += cnt_sub[i]
                if match == sub_n:
                    return True

        for i in range(sub_n, n):
            cnt_s2[ord(s2[i - sub_n]) - ord("a")] -= 1
            cnt_s2[ord(s2[i]) - ord("a")] += 1
            match = 0        
            for i in range(26):
                if cnt_sub[i] > 0 and cnt_sub[i] == cnt_s2[i]:
                    match += cnt_sub[i]
                    if match == sub_n:
                        return True
        return False
