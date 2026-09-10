class Solution {
private:
    bool dfs(int course, const vector<vector<int>>& adj, vector<int>& color, vector<int>& result){
        if (color[course] == 1){
            return false;
        }
        if (color[course] == 2){
            return true;
        }

        color[course] = 1;
        for(int n : adj[course]){
            bool ans = dfs(n, adj, color, result);
            if(!ans){
                return false;
            }
        }

        color[course] = 2;
        result.push_back(course);
        return true;
    }    
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<vector<int>> adj(numCourses);
        for (const auto& pre : prerequisites) {
        int a = pre[0];
        int b = pre[1];
        adj[b].push_back(a); 
        }
        vector<int> color(numCourses, 0);
        vector<int> result;
        for(int i = 0; i < numCourses; i++){
            if (color[i] == 0){
                bool ans = dfs(i, adj, color, result);
                if(!ans){
                    return {};
                }
            }
        }
        reverse(result.begin(), result.end());
        return result;
        
    }
};
