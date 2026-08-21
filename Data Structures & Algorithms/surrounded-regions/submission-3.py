class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        reachable = set()
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == "O":
                    q.append((r, c))
                    reachable.add((r, c))

        while q: 
            r, c = q.popleft()
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    board[nr][nc] == "O" and (nr, nc) not in reachable):
                    reachable.add((nr, nc))
                    q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in reachable:
                    board[r][c] = "X"                             