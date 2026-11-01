class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in '({[':
                stack.append(b)
                continue   
            if not stack:
                return False    
            top = stack.pop()
            if top == '(' and b != ')':
                return False
            if top == '{' and b != '}':
                return False
            if top == '[' and b!= ']':
                return False
        return len(stack) == 0                   