class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.mat = [[0] * (cols + 1) for _ in range(rows + 1)]
    
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                val = matrix[r-1][c-1]
                self.mat[r][c] = val + self.mat[r-1][c] + self.mat[r][c-1] - self.mat[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.mat[r2][c2] - self.mat[r1 - 1][c2] - self.mat[r2][c1 - 1] + self.mat[r1 - 1][c1 - 1]
             


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)