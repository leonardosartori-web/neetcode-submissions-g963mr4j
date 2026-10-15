class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            seen[n] = seen.get(n, 0) + 1
        
        freq = [deque() for _ in range(len(nums)+1)]

        for n, cnt in seen.items():
            freq[cnt].append(n)
        
        return [n for bucket in reversed(freq) for n in bucket][:k]
        