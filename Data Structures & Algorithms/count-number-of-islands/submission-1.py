class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()
        
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def breadth_first_search(row, col):
            q = deque()
            seen.add((row, col))
            q.append((row, col))

            while q:
                row, col = q.popleft()
                for direction in directions:
                    r, c = row + direction[0], col + direction[1]
                    if r in range(rows) and c in range(cols):
                        if grid[r][c] == "1" and (r, c) not in seen:
                            q.append((r, c))
                            seen.add((r, c))
            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    breadth_first_search(row, col)
                    res += 1
        
        return res