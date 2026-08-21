class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                continue
            val = prices[i] - minPrice
            if val > maxProfit:
                maxProfit = val
        return maxProfit                