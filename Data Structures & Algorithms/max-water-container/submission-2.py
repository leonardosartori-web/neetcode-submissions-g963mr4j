class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mx = 0

        while l < r:
            min_height = min(heights[l], heights[r])
            curr_area = (r - l) * min_height
            if min_height == heights[r]:
                r -= 1
            else:
                l += 1
            mx = max(mx, curr_area)
        return mx
