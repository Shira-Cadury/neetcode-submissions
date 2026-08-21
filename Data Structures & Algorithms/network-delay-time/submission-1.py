class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))

        distances = [float('inf')] * (n + 1)
        distances[k] = 0 
        min_heap = [(0, k)] 
        visited = set()

        while min_heap:
            d, u = heapq.heappop(min_heap)            
            if u in visited:
                continue            
            visited.add(u)            
            for v, weight in adj[u]:
                new_dist = d + weight
                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(min_heap, (new_dist, v))

        if len(visited) != n:
            return -1
            
        return int(max(distances[1:]))