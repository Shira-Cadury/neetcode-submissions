class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6" : "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []
        curr = []

        def dfs(i):
            if i == len(digits):
                res.append("".join(curr))
                return
            digit = digits[i]
            letters = mapping[digit]
            for c in letters:
                curr.append(c)
                dfs(i + 1)
                curr.pop()

        dfs(0)
        return res           