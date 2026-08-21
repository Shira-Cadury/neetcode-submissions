class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        def helper(r, c, k):
            if k == len(word):
                return True
            if (r < 0 or r >= ROWS or  c < 0 or c >= COLS or board[r][c] != word[k]):
               return False
            temp = board[r][c]
            board[r][c] = "#"
            res = (helper(r+1, c, k+1) or helper(r-1, c, k+1) or helper(r, c+1, k+1) or helper(r, c-1, k+1))
            board[r][c] = temp
            return res       
                    

        for i in range(ROWS):
            for j in range(COLS):
                if helper(i, j, 0):
                    return True
        return False

        
        