class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumNums = sum(nums)
        if sumNums % 2 != 0:
            return False
        target = sumNums // 2
        dp = {0}
        for n in nums:
            if n > target:
                continue
            newSums = set()
            for s in dp:
                newSum = s + n
                if newSum == target:
                    return True
                if newSum < target:
                    newSums.add(newSum)
            dp.update(newSums)   
        return False                     