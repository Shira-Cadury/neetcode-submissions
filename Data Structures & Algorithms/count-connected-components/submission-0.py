class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        count = n        
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
            return False#ה
            
        for u, v in edges:
            if union(u, v):
                count -= 1 # הצלחנו לאחד שתי קבוצות, אז מספר הרכיבים ירד
                
        return count