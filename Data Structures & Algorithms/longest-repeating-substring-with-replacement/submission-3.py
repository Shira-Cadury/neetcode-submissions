class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_freq = 0
        dic_freq = {}
        ans = 0

        for right in range(len(s)):

            char_right = s[right]
            dic_freq[char_right] = dic_freq.get(char_right, 0) + 1
            max_freq = max(max_freq, dic_freq[char_right])
            if(right - left + 1) - max_freq > k:
                char_left = s[left]
                dic_freq[char_left] -= 1
                left += 1

            ans = max(ans, right - left + 1)
        return ans                    