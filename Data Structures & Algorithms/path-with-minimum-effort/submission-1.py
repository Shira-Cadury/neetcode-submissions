class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        
        efforts = [[float('inf')] * cols for _ in range(rows)]
        efforts[0][0] = 0
        
        heap = [(0, 0, 0)]
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while heap:
            curr_effort, r, c = heapq.heappop(heap)
            
            if r == rows - 1 and c == cols - 1:
                return curr_effort
            
            if curr_effort > efforts[r][c]:
                continue
                
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < rows and 0 <= nc < cols:
                    edge_cost = abs(heights[r][c] - heights[nr][nc])
                    next_effort = max(curr_effort, edge_cost)
                    
                    if next_effort < efforts[nr][nc]:
                        efforts[nr][nc] = next_effort
                        heapq.heappush(heap, (next_effort, nr, nc))
        return 0            
        