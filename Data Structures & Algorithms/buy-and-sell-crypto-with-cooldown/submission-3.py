from functools import cache
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        @cache
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                skip = dfs(i + 1, True)
                return max(buy, skip)
            else:
                sell = dfs(i + 2, True) + prices[i]
                hold = dfs(i + 1, False)
                return max(sell, hold)

        return dfs(0, True)