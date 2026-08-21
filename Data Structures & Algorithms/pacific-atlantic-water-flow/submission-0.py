class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        p_visited = set()
        a_visited = set()
        p_q = deque()
        a_q = deque()

        for r in range(rows):
            p_q.append((r, 0))
            p_visited.add((r, 0))
            a_q.append((r, cols - 1))
            a_visited.add((r, cols - 1))

        for c in range(cols):
            p_q.append((0, c))
            p_visited.add((0, c))
            a_q.append((rows - 1, c))
            a_visited.add((rows - 1, c))

        def bfs(q, visited):
            while q:
                r, c = q.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        (nr, nc) not in visited and 
                        heights[nr][nc] >= heights[r][c]):
                        
                        visited.add((nr, nc))
                        q.append((nr, nc))

        bfs(p_q, p_visited)
        bfs(a_q, a_visited)

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in p_visited and (r, c) in a_visited:
                    res.append([r, c])
        
        return res