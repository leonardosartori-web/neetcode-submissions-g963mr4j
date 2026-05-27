class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        isThereOdd, res = False, 0
        for e, cnt in count.items():
            res += 2 * (cnt // 2)
            if not isThereOdd and cnt % 2 == 1:
                res += 1
                isThereOdd = True
        return res