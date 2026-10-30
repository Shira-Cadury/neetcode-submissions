class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stuck = []
        for op in operations:
            if op == '+':
                stuck.append(stuck[-2] + stuck[-1])
            elif op == 'D':
                stuck.append(2 * stuck[-1])    
            elif op == 'C':
                stuck.pop()
            else:
                stuck.append(int(op))
        return sum(stuck)                