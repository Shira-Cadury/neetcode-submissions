class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []

        def backtracking(index):
            if index ==  len(nums):
                res.append(current.copy())
                return
            current.append(nums[index])
            backtracking(index + 1)
            current.pop()
            backtracking(index + 1)

        backtracking(0)
        return res    