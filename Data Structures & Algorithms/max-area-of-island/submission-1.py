class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        seen = set()

        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        def find_connected_islands(row, col):
            q = deque()
            seen.add((row, col))
            q.append((row, col))
            curr = 1
            while q:
                row, col = q.popleft()
                for dir in directions:
                    r, c = row + dir[0], col + dir[1]
                    if r in range(rows) and c in range(cols):
                        if grid[r][c] and (r, c) not in seen:
                            curr += 1
                            seen.add((r, c))
                            q.append((r, c))

            return curr
            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] and (row, col) not in seen:
                    curr = find_connected_islands(row, col)
                    print(curr)
                    res = max(res, curr)
        return res