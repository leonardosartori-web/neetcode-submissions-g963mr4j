class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        left = 0
        res = 0

        for right in range(len(s)):
            cnt[s[right]] = 1 + cnt.get(s[right], 0)
            maxf = max(cnt.values())

            while right - left + 1 - maxf > k:
                cnt[s[left]] -= 1
                left += 1
            res = max(res, right-left+1)
        return res