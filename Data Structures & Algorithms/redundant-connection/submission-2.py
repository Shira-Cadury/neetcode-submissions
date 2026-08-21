class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        
        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
            
        def union(i, j):
            root1 = find(i)
            root2 = find(j)
            
            if root1 != root2:
                parent[root1] = root2
                return True 
            return False
            
        for u, v in edges:
            if not union(u, v):
                return [u, v]