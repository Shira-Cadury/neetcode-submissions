class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> visited(deadends.begin(), deadends.end());
        
        if (visited.count("0000")) {
            return -1;
        }
        
        if (target == "0000") {
            return 0;
        }

        queue<pair<string, int>> q;
        q.push({"0000", 0});
        visited.insert("0000");

        while (!q.empty()) {
            auto [code, steps] = q.front();
            q.pop();

            for (int i = 0; i < 4; i++) {
                string up = code;
                up[i] = (code[i] == '9') ? '0' : code[i] + 1;

                string down = code;
                down[i] = (code[i] == '0') ? '9' : code[i] - 1;

                for (const string& next_code : {up, down}) {
                    if (next_code == target) {
                        return steps + 1;
                    }
                    if (!visited.count(next_code)) {
                        visited.insert(next_code);
                        q.push({next_code, steps + 1});
                    }
                }
            }
        }
        return -1;
    }
};