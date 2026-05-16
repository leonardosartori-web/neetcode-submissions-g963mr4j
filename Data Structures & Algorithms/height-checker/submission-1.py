class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = Counter(heights)
        expected = deque()
        for h in range(1, 101):
            cnt = count[h]
            for _ in range(cnt):
                expected.append(h)
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                res += 1
        return res
