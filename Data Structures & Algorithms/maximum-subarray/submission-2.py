class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        max_sum = nums[0]

        for n in nums:
            curr_max = max(n, n + curr_max)
            max_sum = max(max_sum, curr_max)

        return max_sum    
           