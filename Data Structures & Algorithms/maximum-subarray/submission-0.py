class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = nums[0]
        maxSum = nums[0]

        for n in nums[1:]:
            currMax = max(n, currMax + n)
            maxSum = max(currMax, maxSum)

        return maxSum    