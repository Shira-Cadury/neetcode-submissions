class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        maxLen = 0
        for n in nums:
            if (n - 1) not in num_set:
                current_num = n
                current_len = 1
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_len += 1
                maxLen = max(maxLen, current_len)
        return maxLen            