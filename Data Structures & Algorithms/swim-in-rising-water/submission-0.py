class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        minHeap = [(grid[0][0], 0, 0)]
        visited = {(0, 0)}
        
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            
            if r == n - 1 and c == n - 1:
                return t
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    new_time = max(t, grid[nr][nc])                    
                    heapq.heappush(minHeap, (new_time, nr, nc))
                    
        return -1 