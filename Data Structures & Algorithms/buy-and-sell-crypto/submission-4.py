class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                continue
            val = prices[i] - min_price
            if val > max_profit:
                max_profit = val
        return max_profit          
        