class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def backtracking(index, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or index == len(nums):
                return

            curr.append(nums[index])
            backtracking(index, total + nums[index])
            curr.pop()
            backtracking(index + 1, total)

        backtracking(0, 0)
        return res    
        