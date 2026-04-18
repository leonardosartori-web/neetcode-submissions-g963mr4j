class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = l + (r - l) // 2
            i, j = mid // n, mid % n

            d = matrix[i][j] - target

            if not d:
                return True
            elif d > 0:
                r = mid - 1
            else:
                l = mid + 1
        return False