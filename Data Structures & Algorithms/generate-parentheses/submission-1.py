class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(openp, close):
            if openp == close == n:
                res.append("".join(curr))
                return

            if openp < n:
                curr.append('(')
                dfs(openp + 1, close)  
                curr.pop()

            if close < openp:
                curr.append(')')
                dfs(openp, close + 1)
                curr.pop()

        dfs(0, 0)
        return res        