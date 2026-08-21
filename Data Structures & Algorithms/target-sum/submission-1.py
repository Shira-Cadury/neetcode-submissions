class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for n in nums:
            temp = {}
            for currSum, count in dp.items():
                plus = currSum + n
                temp[plus] = temp.get(plus, 0) + count
                minus = currSum - n
                temp[minus] = temp.get(minus, 0) + count
            dp = temp
        return dp.get(target, 0)        