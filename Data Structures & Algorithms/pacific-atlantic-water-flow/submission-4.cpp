class Solution {
private:
    void dfs(int r, int c, int rows, int cols, vector<vector<bool>>& visited, int prev, const vector<vector<int>>& heights) {
        if (r < 0 || r >= rows || c < 0 || c >= cols || visited[r][c] || heights[r][c] < prev) {
            return; 
        }
        visited[r][c] = true;
        
        dfs(r - 1, c, rows, cols, visited, heights[r][c], heights);
        dfs(r + 1, c, rows, cols, visited, heights[r][c], heights);
        dfs(r, c - 1, rows, cols, visited, heights[r][c], heights);
        dfs(r, c + 1, rows, cols, visited, heights[r][c], heights);
    }    

public:
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        if (heights.empty() || heights[0].empty()) {
            return {};
        }

        int rows = heights.size();
        int cols = heights[0].size();

        vector<vector<bool>> pac(rows, vector<bool>(cols, false));
        vector<vector<bool>> atl(rows, vector<bool>(cols, false));
        vector<vector<int>> ans;

        for (int i = 0; i < rows; i++) {
            dfs(i, 0, rows, cols, pac, -1, heights);
            dfs(i, cols - 1, rows, cols, atl, -1, heights);
        }

        for (int j = 0; j < cols; j++) {
            dfs(0, j, rows, cols, pac, -1, heights);
            dfs(rows - 1, j, rows, cols, atl, -1, heights);
        }

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (pac[r][c] && atl[r][c]) {
                    ans.push_back({r, c});
                }
            }
        }
        return ans;
    }
};