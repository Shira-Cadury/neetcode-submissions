class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]

        def dfs(curr, target, visited):
            if curr == target:
                return True
            if curr in visited:
                return False    
            visited.add(curr)    

            for c in adj[curr]:
                if c not in visited:
                    if dfs(c, target, visited):
                        return True 
            return False                   

        for a, b in edges:
            visited = set()
            if dfs(a, b, visited):
                return [a, b]
            adj[a].append(b)
            adj[b].append(a)                