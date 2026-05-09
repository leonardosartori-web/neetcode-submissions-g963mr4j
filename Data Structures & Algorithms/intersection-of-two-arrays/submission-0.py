class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        res = deque()
        for n in nums2:
            if n in nums1_set:
                res.append(n)
        return list(set(res))