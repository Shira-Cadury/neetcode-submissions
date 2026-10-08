class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, majority = 0, -1
        for n in nums:
            if count == 0:
                count = 1
                majority = n
            elif n == majority:
                count += 1
            else:
                count -= 1
        return majority               
       