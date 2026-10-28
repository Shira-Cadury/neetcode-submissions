class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[i-len(word):i] == word:
                    if dp[i-len(word)] == True:
                        dp[i] = True
                        continue
        if dp[-1] == True:
            return True
        return False                    
             
