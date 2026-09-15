class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for (a, b), val in zip(equations, values):
            adj[a].append((b, val))         
            adj[b].append((a, 1.0 / val))

        def dfs(curr, target, visited):
            if curr == target:
                return 1.0
            visited.add(curr)    
            for neighbor, weight in adj[curr]:
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited)
                    if res != -1.0:
                        return weight * res
            return -1.0            

        results = []
        for c, d in queries:
            if c not in adj or d not in adj:
                results.append(-1.0)
            else:
                results.append(dfs(c, d, set()))
                
        return results                
        