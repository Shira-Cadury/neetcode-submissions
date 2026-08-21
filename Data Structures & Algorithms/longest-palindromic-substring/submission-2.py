class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen, maxLeft, maxRight = 0, 0, 0

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
            return(left + 1, right)    

        for i in range(len(s)):
            left, right = expand(i, i)
            if (right - left) > maxLen:
                maxLen = right - left
                maxLeft, maxRight = left, right

            if i + 1 < len(s):
                left, right = expand(i, i + 1)
                if (right - left) > maxLen:
                    maxLen = right - left
                    maxLeft, maxRight = left, right
        return s[maxLeft: maxRight]        

            
        