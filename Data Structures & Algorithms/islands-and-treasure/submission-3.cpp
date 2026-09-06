class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {
        if (grid.empty() || grid[0].empty()){
            return;
        }
        int rows = grid.size();
        int cols = grid[0].size();

        std::queue<std::pair<int, int>> q;
        vector<vector<bool>> visited(rows, vector<bool>(cols, false));

        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                if (grid[r][c] == 0){
                    q.push({r, c});
                    visited[r][c] = true;
                }
            }
        }

        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
            while (!q.empty()){
            auto [r, c] = q.front();
            q.pop();
            for (auto [dr, dc] : directions) {
            int nr = r + dr;
            int nc = c + dc;
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols) {
                    if (!visited[nr][nc] && grid[nr][nc] != -1){
                        grid[nr][nc] = grid[r][c] + 1;
                        visited[nr][nc] = true;
                        q.push({nr, nc});
                    }
                }
            }
        }
    }
};
