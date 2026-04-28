class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c, seen, prevHeight):
            if r in range(rows) and c in range(cols) and (r, c) not in seen and heights[r][c] >= prevHeight:
                seen.add((r, c))
                for d in directions:
                    dfs(r + d[0], c + d[1], seen, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols-1, atl, heights[r][cols-1])

        res = []
        for e in pac:
            if e in atl:
                res.append(e)
        return res