class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]

        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))
        visited = set()    
        while heap:
            d, u = heapq.heappop(heap)  
            if u in visited:
                continue
            visited.add(u)
            for v, w in adj[u]:
                if w + dist[u] < dist[v]:
                    dist[v] = w +dist[u]
                    heapq.heappush(heap, (dist[v], v))
        if len(visited) != n:
            return -1
        return max(dist[1:])                

