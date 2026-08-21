class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows * cols) - 1
        while left <= right:
            mid_index = (left + right) // 2
            row = mid_index // cols
            col = mid_index % cols
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                right =  mid_index - 1
            else:
                left =  mid_index + 1
        return False            
