class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        
        rows, cols = len(matrix), len(matrix[0])

        zeroes = []

        for r in range(rows):
            for c in range(cols):
                if not matrix[r][c]:
                    zeroes.append((r, c))
        
        for zero in zeroes:
            for row in range(rows):
                matrix[row][zero[1]] = 0
            for col in range(cols):
                matrix[zero[0]][col] = 0
