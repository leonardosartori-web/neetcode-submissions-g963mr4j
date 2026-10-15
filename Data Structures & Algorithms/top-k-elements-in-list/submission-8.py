class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = sorted(Counter(nums).items(), key=lambda i: -i[1])
        i = 0
        res = deque()
        while i < len(counter) and k != 0:
            res.append(counter[i][0])
            k -= 1
            i += 1
        return list(res)