class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}
        for num in nums:
            temp = {}
            for curr_sum, count in dp.items():
                plus = curr_sum + num
                temp[plus] = temp.get(plus, 0) + count
                minus = curr_sum - num
                temp[minus] = temp.get(minus, 0) + count
            dp = temp
        return dp.get(target, 0)         
        