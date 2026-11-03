class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        rest, sold, hold = 0, 0, prices[0] * -1
        for price in prices:
            prev_rest, prev_sold, prev_hold = rest, sold, hold
            hold = max(prev_hold, prev_rest - price)
            sold = prev_hold + price
            rest = max(prev_rest, prev_sold)
        return max(rest, sold)    
