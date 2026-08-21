class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        def helper(curr, index):
            res.append(curr.copy())
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                helper(curr, i+1)
                curr.pop()
        helper([], 0)
        return res           
