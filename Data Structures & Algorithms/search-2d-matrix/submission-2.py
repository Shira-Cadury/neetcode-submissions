class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) * len(matrix[0]) - 1
        cols = len(matrix[0])
        while left <= right:
            mid = (left + right) // 2
            col = mid // cols
            row = mid % cols
            if matrix[col][row] == target:
                return True
            if matrix[col][row] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False               
               