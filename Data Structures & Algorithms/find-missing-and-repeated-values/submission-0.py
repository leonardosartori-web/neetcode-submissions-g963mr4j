class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        s = (n*n)*((n*n)+1) // 2
        seen = set()
        res = [-1, -1]
        for row in grid:
            for col in row:
                if col in seen:
                    res[0] = col
                    s += col
                seen.add(col)
                s -= col
        res[1] = s
        return res