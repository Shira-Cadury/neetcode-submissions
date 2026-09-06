class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        row = len(grid)
        col = len(grid[0])

        q = deque()
        visited = set()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        direction = [(1, 0), (-1, 0), (0, 1), (0,-1)]
        while q:
            r, c = q.popleft()
            for dr, dc in direction:
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    if (nr, nc) not in visited and grid[nr][nc] != -1:
                        grid[nr][nc] = grid[r][c] + 1
                        visited.add((nr, nc))
                        q.append((nr, nc))