class Solution:
    def isPalindrome(self, st: str) -> bool:
        '''s = ""
        for c in st:
            if c.isalnum():
                s += c
        i = 0
        while i <= (len(s)-1)//2:
            if s[i].lower() != s[-1-i].lower():
                return False
            i += 1
        return True'''
        l, r = 0, len(st) - 1
        while l <= r:
            if not st[l].isalnum():
                l += 1
                continue
            if not st[r].isalnum():
                r -= 1
                continue
            if st[l].lower() != st[r].lower():
                return False
            l += 1
            r -= 1
        return True