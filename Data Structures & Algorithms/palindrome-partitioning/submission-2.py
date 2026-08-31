class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr = []

        def dfs(i):
            if i == len(s):
                res.append(curr.copy())
                return
            for j in range(i, len(s)):
                sub = s[i: j + 1]
                if isPalindrome(sub):
                    curr.append(sub)
                    dfs(j + 1)
                    curr.pop()
                 

        def isPalindrome(s: str) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        dfs(0)
        return res    