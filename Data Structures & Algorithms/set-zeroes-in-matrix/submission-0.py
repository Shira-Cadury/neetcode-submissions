class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        row_zero = False

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    if r == 0:
                        row_zero = True
                    else:
                        matrix[r][0] = 0
                        matrix[0][c] = 0

        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            for r in range(m):
                matrix[r][0] = 0

        if row_zero:
            for c in range(n):
                matrix[0][c] = 0