class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == '/':
                temp = stack.pop()
                stack.append(int(stack.pop() / temp))
            elif c == '+':
                temp = stack.pop()
                stack.append(temp + stack.pop())
            elif c == '-':
                temp = stack.pop()
                stack.append(stack.pop() - temp)
            elif c == '*':
                temp = stack.pop()
                stack.append(temp * stack.pop())
            else:
                stack.append(int(c))
        return stack.pop()                