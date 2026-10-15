class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = sorted(Counter(nums).items(), key=lambda i: -i[1])
        res = deque()
        for i in range(k):
            res.append(counter[i][0])
        return list(res)