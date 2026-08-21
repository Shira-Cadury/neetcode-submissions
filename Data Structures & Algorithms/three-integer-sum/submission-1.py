class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0 and i < (len(nums) - 1) and nums[i] == nums[i - 1]:
                continue
            target = nums[i] * -1
            j, k = (i + 1), len(nums) - 1
            while j < k:
                val = nums[j] + nums[k]
                if val == target:
                    ans.append([nums[j], nums[i], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1    
                elif val > target:
                    k -= 1
                else: 
                    j += 1 
        return ans                   
