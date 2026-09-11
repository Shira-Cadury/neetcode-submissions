class Solution {
private:
    void dfs(int node, int &count, const vector<vector<int>>& adj, vector<bool>& visited){
        visited[node] = true;
        count++;
        for (int n: adj[node]){
            if (!visited[n]){
                dfs(n, count, adj, visited);
            }
        }
        return;
    }    
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        int length = edges.size();
        int count = 0;
        if (length != n - 1){
            return false;
        }

        vector<bool> visited(n, false);
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
        int a = edge[0];
        int b = edge[1];
        adj[b].push_back(a); 
        adj[a].push_back(b);
        }
        dfs(0, count, adj, visited);
        if (count == n){
            return true;
        }
        return false;
        
    }
};
