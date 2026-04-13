class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_occ = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]

        for e in nums:
            if e not in nums_occ:
                nums_occ[e] = 0
            nums_occ[e] += 1
        
        for e, cnt in nums_occ.items():
            freq[cnt].append(e)
        
        res = []
        i = len(freq) - 1
        while(k >= 0 and i >= 0):
            for e in reversed(freq[i]):
                if k > 0:
                    res.append(e)
                    k -= 1
            i -= 1
        return res