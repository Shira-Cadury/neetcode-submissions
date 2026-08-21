class Solution:
    def countSubstrings(self, s: str) -> int:
        totalCount = 0

        def expand(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
                    count += 1
            return count  

        for i in range(len(s)):
            totalCount += expand(i, i)
            if i + 1 < len(s):
                totalCount += expand(i, i + 1)
        return totalCount        
            
        