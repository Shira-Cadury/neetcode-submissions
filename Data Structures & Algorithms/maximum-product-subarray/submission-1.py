class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) 
        currMin, currMax = 1, 1
        
        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue
            
            oldMax = currMax
            currMax = max(n, n * currMax, n * currMin)
            currMin = min(n, n * oldMax, n * currMin)
            
            res = max(res, currMax)
            
        return res