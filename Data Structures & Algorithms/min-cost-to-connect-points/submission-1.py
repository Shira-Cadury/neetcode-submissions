class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        min_dist = [float('inf')] * n
        min_dist[0] = 0 
        visited = [False] * n
        total_cost = 0
        
        for _ in range(n):
            
            curr_u = -1
            for i in range(n):
                if not visited[i] and (curr_u == -1 or min_dist[i] < min_dist[curr_u]):
                    curr_u = i
            
            visited[curr_u] = True
            total_cost += min_dist[curr_u]
            
            x1, y1 = points[curr_u]
            for v in range(n):
                if not visited[v]:
                    x2, y2 = points[v]
                    dist = abs(x1 - x2) + abs(y1 - y2)
                    
                    if dist < min_dist[v]:
                        min_dist[v] = dist
        
        return total_cost