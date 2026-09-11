class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()

        def dfs(node):
            visited.add(node)
            for a in adj[node]:
                if a not in visited:
                    dfs(a)
            return

        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        return count                         
        