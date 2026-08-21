class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        res = 0 
        while left <= right:
            mid = (left + right) // 2
            q = mid * mid
            
            if q == x:
                return mid 
            
            if q < x:
                res = mid 
                left = mid + 1
            else:
                right = mid - 1
                
        return res