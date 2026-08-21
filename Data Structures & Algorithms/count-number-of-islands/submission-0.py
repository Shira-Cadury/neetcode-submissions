class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        count = 0
        rows, cols = len(grid), len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    self.bfs(grid, r, c)

        return count 

    def bfs(self, grid, r, c):
        q = deque([(r, c)])
        grid[r][c] = "0"

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if (0 <= nr < len(grid) and 
                    0 <= nc < len(grid[0]) and 
                    grid[nr][nc] == "1"):
                    q.append((nr, nc))
                    grid[nr][nc] = "0" 
