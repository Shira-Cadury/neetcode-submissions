class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        nums.sort()  

        def backtracking(index):
            if index == len(nums):
                res.append(current.copy())
                return

            current.append(nums[index])
            backtracking(index + 1)
            current.pop()

            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            backtracking(index + 1)

        backtracking(0)
        return res