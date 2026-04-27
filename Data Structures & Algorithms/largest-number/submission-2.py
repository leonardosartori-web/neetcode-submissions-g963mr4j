from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(a, b):
            return -1 if a + b > b + a else 1
        
        res = sorted([str(x) for x in nums], key=cmp_to_key(compare))

        return str(int("".join(res)))
