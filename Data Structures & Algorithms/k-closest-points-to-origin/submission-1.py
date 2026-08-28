class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dis = (x**2 + y**2) ** 0.5
            if len(heap) < k:
                heapq.heappush(heap, [-dis, [x, y]])
            elif -heap[0][0] > dis:
                heapq.heappushpop(heap, [-dis, [x,y]])    
        return [point for neg_dist, point in heap]         

        