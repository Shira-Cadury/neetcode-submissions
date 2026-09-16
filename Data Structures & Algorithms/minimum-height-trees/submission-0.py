class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)    
        degree = [0] * n
        for u, v in edges:
            degree[u] += 1
            degree[v] += 1 
        totalNodes = n 
        leaves = [i for i in range(n) if degree[i] == 1]
        while totalNodes > 2:
            totalNodes -= len(leaves)
            newLeaves = []
            for leaf in leaves:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    newLeaves.append(neighbor)
            leaves = newLeaves 
        return leaves    

        