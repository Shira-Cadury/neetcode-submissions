class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2

        for n in nums:
            expected_sum -= n
        return expected_sum    
        