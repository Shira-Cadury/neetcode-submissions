class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            if tok not in {"+", "-", "*", "/"}:
                stack.append(int(tok))
            elif tok == '+':
                temp = stack.pop()
                stack.append(temp + stack.pop())
            elif tok == '-':
                temp = stack.pop()
                stack.append(stack.pop() - temp)
            elif tok == '*':
                temp = stack.pop()
                stack.append(stack.pop() * temp)
            else:
                temp = stack.pop()
                stack.append(int(stack.pop() / temp))
        return stack.pop()                        
