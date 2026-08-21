class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def helper(s,r, l):
            if (2 * n) == len(s):
                result.append(s)
                return
            if l < n:
                helper(s + "(", r, l + 1)
            if  r < l:
                helper(s + ")", r + 1, l)    
        helper("", 0, 0)
        return result    