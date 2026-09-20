class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_min, curr_max = 1, 1

        for n in nums:
            if n == 0:
                curr_max, curr_min = 1, 1
                continue
            old_max = curr_max
            curr_max = max(n, n * old_max, n * curr_min)
            curr_min = min(n, n * old_max, n * curr_min)

            res = max(curr_max, res)

        return res        
