class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if word1 == "": return word2
        if word2 == "": return word1
        ans = ""
        length = min(len(word1), len(word2))
        for i in range(length):
            ans += word1[i]
            ans += word2[i]
        if length < len(word1):
            ans += word1[length:]
        if length < len(word2):
            ans += word2[length:]
        return ans             
        