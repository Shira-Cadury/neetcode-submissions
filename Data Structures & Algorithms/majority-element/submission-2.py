class Solution:
    def majorityElement(self, nums: List[int]) -> int:
       count = 0
       candidate = nums[0]
       for i in range(len(nums)):
        if candidate == nums[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            candidate = nums[i]
            count = 1  
       return candidate           