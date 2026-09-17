class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):

            temp = prices.copy()
            for u, v, price in flights:
                if prices[u] == float('inf'):
                    continue
                if prices[u] + price < temp[v]:
                    temp[v] = prices[u] + price

            prices = temp.copy()
        if prices[dst] == float('inf'):
            return -1
        return prices[dst]                    
        