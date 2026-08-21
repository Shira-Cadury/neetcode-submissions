class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      stuck = [] 
      for t in tokens:
        if t not in "+-*/":
            stuck.append(int(t)) 
        elif t == '+':
            temp = stuck.pop()
            stuck.append(temp + (stuck.pop()))
        elif t == '-':
            temp = stuck.pop()
            stuck.append((stuck.pop()) - temp)
        elif t == '*':
            temp = stuck.pop()
            stuck.append((stuck.pop()) * temp)    
        else:
            temp = stuck.pop()
            stuck.append(int(stuck.pop() / temp))   
      return stuck.pop()              