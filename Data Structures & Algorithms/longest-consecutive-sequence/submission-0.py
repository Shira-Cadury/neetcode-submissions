class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        maxSequence = 0
        for n in nums_set:
            if n - 1 in nums_set:
                continue
            count = 1
            while (n + count)  in nums_set:  
                count += 1
            maxSequence = max(maxSequence, count)
        return maxSequence          