class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        q = deque()
        res, fresh = 0, 0

        rows, cols = len(grid), len(grid[0])

        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        # Count fresh and queue rotten
        for row in range(rows):
            for col in range(cols):
                cell = grid[row][col]
                if cell > 0:
                    if cell == 1:
                        fresh += 1
                    else:
                        q.append((row, col))
        
        # BFS
        while q and fresh > 0:
            # In q only rotten fruit at same time
            for _ in range(len(q)):
                row, col = q.popleft()
                for direction in directions:
                    r, c = row + direction[0], col + direction[1]
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
            res += 1
        return res if fresh < 1 else -1
            



