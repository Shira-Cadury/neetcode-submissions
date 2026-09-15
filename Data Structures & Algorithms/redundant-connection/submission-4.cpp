class Solution {
private:
    bool dfs(int curr, int target, const vector<vector<int>>& adj, vector<bool>& visited){
        if (curr == target){
            return true;
        }
        visited[curr] = true;
        for (int a : adj[curr]){
            if (!visited[a]){
                if (dfs(a, target, adj, visited)){
                return true;
                }
            } 
        }
        return false;
    }    
public:
    vector<int> findRedundantConnection(vector<vector<int>>& edges) {
        int n = edges.size();
        vector<vector<int>> adj(n + 1);
        for (const auto& edge : edges){
            int a = edge[0];
            int b = edge[1]; 
            vector<bool> visited(n + 1, false);
            if (dfs(a, b, adj, visited)){
                return {a, b};
            }
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        return {};
    }
};
