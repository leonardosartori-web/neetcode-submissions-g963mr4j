class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        i, j = row1, col1
        while i <= row2:
            j = col1
            while j <= col2:
                res += self.matrix[i][j]
                j += 1
            i += 1
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)