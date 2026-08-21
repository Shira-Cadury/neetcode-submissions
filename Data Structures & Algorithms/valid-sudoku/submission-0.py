class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9  
        squares = [0] * 9
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                val = int(board[r][c]) - 1
                if (1 << val) & rows[r]:
                    return False
                if (1 << val) & cols[c]:
                    return False
                
                sq_idx = (r // 3) * 3 + (c // 3)
                if (1 << val) & squares[sq_idx]:
                    return False

                rows[r] |= (1 << val)
                cols[c] |= (1 << val)
                squares[sq_idx] |= (1 << val)

        return True