class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        double = set()
        for i in range(len(nums)):
            if nums[i] in double:
                return True
            double.add(nums[i])
        return False        