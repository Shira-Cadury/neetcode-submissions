class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        rows = len(grid)
        cols = len(grid[0])
        
        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visited and grid[nr][nc] != -1:
                        grid[nr][nc] = grid[r][c] + 1
                        visited.add((nr, nc))
                        q.append((nr, nc))