class Solution {
private:
    void dfs(int node, const vector<vector<int>>& adj, vector<bool>& visited){
        visited[node] = true;
        for (int a : adj[node]){
            if (!visited[a]){
                dfs(a, adj, visited);
            }
        }
        return;
    }    
public:
    int countComponents(int n, vector<vector<int>>& edges) {
        int count = 0;
        vector<vector<int>> adj(n);
        for (const auto& edg : edges) {
        int a = edg[0];
        int b = edg[1];
        adj[b].push_back(a); 
        adj[a].push_back(b);
        }
        vector<bool> visited(n, false);

        for (int i = 0; i < n; i++){
            if (!visited[i]){
                count++;
                dfs(i, adj, visited);
            }
        }
        return count;
        

    }
};
