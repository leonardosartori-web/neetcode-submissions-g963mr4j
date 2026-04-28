class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        seen = set()

        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    seen.add((i, j))
                    q.append([i, j])
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        t = 1
        
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                for d in directions:
                    r, c = row + d[0], col + d[1]
                    if r in range(rows) and c in range(cols):
                        if grid[r][c] >= 0 and (r, c) not in seen:
                            grid[r][c] = t
                            seen.add((r, c))
                            q.append([r, c])
            t += 1



