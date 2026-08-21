class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        cols = len(matrix[0])
        while left <= right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False        