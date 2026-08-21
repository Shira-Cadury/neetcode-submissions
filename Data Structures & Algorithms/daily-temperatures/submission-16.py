class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stuck = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stuck and temperatures[stuck[-1]] < temperatures[i]:
                index = stuck.pop()
                res[index] = i - index
            stuck.append(i)    
        return res             