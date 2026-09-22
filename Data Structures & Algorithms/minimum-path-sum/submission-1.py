class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)] 
        

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    dp[0][0] = grid[0][0]
                    continue

                if r == 0:
                    dp[r][c] = dp[r][c - 1] + grid[r][c]
                    continue

                if c == 0:
                    dp[r][c] = dp[r - 1][c] + grid[r][c]
                    continue

                dp[r][c] = min(dp[r - 1][c] , dp[r][c - 1]) + grid[r][c]
        return dp[rows - 1][cols - 1]                       
        