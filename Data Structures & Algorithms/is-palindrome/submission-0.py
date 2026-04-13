class Solution:
    def isPalindrome(self, st: str) -> bool:
        s = ""
        for c in st:
            if c.isalnum():
                s += c
        i = 0
        while i <= (len(s)-1)//2:
            if s[i].lower() != s[-1-i].lower():
                return False
            i += 1
        return True