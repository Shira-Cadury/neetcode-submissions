class Solution:
    def climbStairs(self, n: int) -> int:
        one, tow = 1, 1
        for _ in range(n - 1): 
            one, tow = one + tow, one
        return one    
