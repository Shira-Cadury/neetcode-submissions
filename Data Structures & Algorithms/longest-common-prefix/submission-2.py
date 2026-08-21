class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = strs[0]

        for i in range(1, len(strs)):
            temp = strs[i]
            if ans == temp:
                continue
            j = 0
            while j < len(ans) and j < len(temp) and ans[j] == temp[j]:
                j += 1  
            ans = ans[0:j]
            if not ans:
                return ""
        return ans                