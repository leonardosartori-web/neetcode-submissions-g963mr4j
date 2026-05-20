class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        seen = {}
        for s in arr:
            seen[s] = seen.get(s, 0) + 1
        for s, cnt in seen.items():
            if cnt == 1:
                k -= 1
                if not k:
                    return s
        return ""
