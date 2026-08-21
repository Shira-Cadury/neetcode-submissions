class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(houses):
            if not houses: return 0
            if len(houses) == 1: return houses[0]
            
            rob1, rob2 = 0, 0
            
            for n in houses:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(helper(nums[1:]), helper(nums[:-1]))