class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int rows = grid.size();
        int cols = grid[0].size();
        std::queue<std::pair<int, int>> q;
        int freshCount = 0;

        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                if (grid[r][c] == 2){
                     q.push({r, c});
                }
                if (grid[r][c] == 1){
                    freshCount ++;
                }
            }
        }
        if (freshCount == 0){
            return 0;
        }

        int time = 0;
        while(!q.empty() && freshCount > 0){
            time ++;
            int sz = q.size();
            for (int i = 0; i < sz; i++){
                auto [r, c] = q.front();
                q.pop();

                vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
                for (auto [dr, dc] : directions) {
                    int nr = r + dr;
                    int nc = c + dc;
                    if (nr >= 0 and nr < rows and nc >= 0 and nc < cols){
                        if (grid[nr][nc] == 1){
                            grid[nr][nc] = 2;
                            freshCount --;
                            q.push({nr, nc});
                        }

                    }
            
            } 
                
            }
        }
        if (freshCount == 0){
            return time;
        }
        return -1;
    }
};
