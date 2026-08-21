class Solution:
    def isValid(self, s: str) -> bool:
        ls=[]
        for c in s:
            if c == '(' or c == '{' or c == '[':
                ls.append(c)
            elif not ls or c == ')':
                if not ls or ls.pop() != '(':
                    return False
            elif not ls or c == '}':
                if ls.pop() != '{':
                    return False
            elif not ls or c == ']':
                if ls.pop() != '[':
                    return False
        if not ls:
            return True 
        return False                             