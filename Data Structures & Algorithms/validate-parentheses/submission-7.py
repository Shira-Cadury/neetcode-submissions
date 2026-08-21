class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for b in s:
            if b in '([{':
                stack.append(b)
            else:
                if not stack:
                    return False
                
                top = stack.pop()
                if b == ')' and top != '(':
                    return False
                if b == ']' and top != '[':
                    return False
                if b == '}' and top != '{':
                    return False
                    
        return len(stack) == 0