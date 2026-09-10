class Solution {
private:
    bool dfs(int course, const vector<vector<int>>& adj, vector<int>& color)
    {
        if (color[course] == 1){
            return false;
        }

        if (color[course] == 2){
            return true;
        }
        color[course] = 1;
        for (int n : adj[course]) {
            bool ans = dfs(n, adj, color);
            if (!ans){
                return false;
            }
        }
        color[course] = 2;
        return true;

    }    
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        for (const auto& pre : prerequisites) {
        int a = pre[0];
        int b = pre[1];
        adj[b].push_back(a); 
        }
        vector<int> color(numCourses, 0);
        
        for (int i = 0; i < numCourses; i++){
            if (color[i] == 0){
                bool ans = dfs(i, adj, color);
                if (!ans){
                    return false;
                }
            }
        }
        return true;
        
    }
};
