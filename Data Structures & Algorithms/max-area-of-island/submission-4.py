class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        maxArea = 0

        def dfs(i, j):
            if i >= row or i < 0 or j >= col or j < 0 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
           

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea                        