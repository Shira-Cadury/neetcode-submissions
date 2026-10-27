class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1
        for n in nums:
            old_max = curr_max
            curr_max = max(n, old_max * n, curr_min * n)
            curr_min = min(n, old_max * n, curr_min * n)
            res = max(res, curr_max)
        return res    