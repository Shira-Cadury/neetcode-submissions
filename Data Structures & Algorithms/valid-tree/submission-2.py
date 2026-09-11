class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        length = len(edges)
        if length != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited = set()

        def dfs(node):
            visited.add(node)
            for n in adj[node]:
                if n not in visited:
                    dfs(n) 
            return

        dfs(0)
        if len(visited) == n:
            return True
        return False                           
        