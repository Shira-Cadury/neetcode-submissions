class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        visited = set()
        totalCost = 0
        heap = [(0, 0)]
        n = len(points)

        while heap:
            cost, u = heapq.heappop(heap)
            if u in visited:
                continue
            visited.add(u)
            totalCost += cost
            if len(visited) == n:
                break
            for v in range(n):
                if v not in visited:
                    dist = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    heapq.heappush(heap, (dist, v))   
        return totalCost              
        