class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(i, curr, target):
            if target == 0:
                res.append(curr[:])
                return
            if i >= len(nums) or target < 0:
                return
            curr.append(nums[i])
            dfs(i, curr, target-nums[i])
            curr.pop()
            dfs(i+1, curr, target)

        dfs(0,[],target)
        return res              
        
        