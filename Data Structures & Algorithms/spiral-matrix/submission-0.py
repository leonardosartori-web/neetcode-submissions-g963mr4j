class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix[0]), len(matrix)
        rightBound, lowerBound = m, n
        leftBound, upperBound = 0, 0
        
        res = deque()
        while leftBound < rightBound and upperBound < lowerBound:
            for i in range(leftBound, rightBound):
                res.append(matrix[upperBound][i])
            upperBound += 1
            for i in range(upperBound, lowerBound):
                res.append(matrix[i][rightBound - 1])
            rightBound -= 1
            if not (leftBound < rightBound and upperBound < lowerBound):
                break 
            for i in range(rightBound - 1, leftBound - 1, -1):
                res.append(matrix[lowerBound - 1][i])
            lowerBound -= 1
            for i in range(lowerBound - 1, upperBound - 1, -1):
                res.append(matrix[i][leftBound])
            leftBound += 1
        return list(res)
