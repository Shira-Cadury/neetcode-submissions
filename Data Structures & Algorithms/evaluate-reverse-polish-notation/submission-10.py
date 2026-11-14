class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            elif t == '+':
                temp = stack.pop()
                stack.append(stack.pop() + temp)
            elif t == '-':
                temp = stack.pop()
                stack.append(stack.pop() - temp)
            elif t == '*':
                temp = stack.pop()
                stack.append(stack.pop() * temp)
            else:
                temp = stack.pop()
                division = stack.pop() / temp
                stack.append(int(division))
        return stack[-1]                   