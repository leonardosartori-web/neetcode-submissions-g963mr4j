class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = nums.copy()
        for i in range(1, len(nums)):
            self.prefix[i] += self.prefix[i-1]


    def sumRange(self, left: int, right: int) -> int:
        sumL = self.prefix[left - 1] if left > 0 else 0
        return self.prefix[right] - sumL
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)