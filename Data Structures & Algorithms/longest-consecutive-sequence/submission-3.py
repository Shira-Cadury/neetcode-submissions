class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for n in num_set:
            if (n - 1) not in num_set:
                curr_num = n
                curr_len = 1
                while (curr_num + 1) in num_set:
                    curr_num += 1
                    curr_len += 1
                max_len = max(curr_len, max_len)
        return max_len            
        