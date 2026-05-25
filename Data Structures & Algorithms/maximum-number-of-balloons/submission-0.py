class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        txtCnt = Counter(text)
        balloonCnt = Counter("balloon")

        res = len(text)

        for e, cnt in balloonCnt.items():
            res = min(res, txtCnt[e] // cnt)
        
        return 0 if res == len(text) else res