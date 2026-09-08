class Solution {
private:
    void dfs(int r, int c, int rows, int cols, vector<vector<char>>& board){
        if ( r < 0 || r >= rows || c < 0 || c >= cols || board[r][c] != 'O'){
            return;
        }
        board[r][c] = 'T';
        dfs(r - 1, c, rows, cols, board);
        dfs(r + 1, c, rows, cols, board);
        dfs(r , c - 1, rows, cols, board);
        dfs(r , c + 1, rows, cols, board);


    }    
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty() || board[0].empty()){
            return;
        }

        int rows = board.size();
        int cols = board[0].size();

        for (int r = 0; r < rows; r++){
            dfs(r, 0, rows, cols, board);
            dfs(r, cols - 1, rows, cols, board);
        }

        for (int c = 0; c < cols; c++){
            dfs(0, c, rows, cols, board);
            dfs(rows - 1, c, rows, cols, board);
        }

        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                if (board[r][c] == 'T'){
                    board[r][c] = 'O';
                }
                 else if ( board[r][c] == 'O'){
                    board[r][c] = 'X';
                }
            }
        }

    }
};
