class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1 = len(s1) 
        if lens1 > len(s2):
            return False
        freqS1 = {} 
        freqS2 = {}
        for letter in s1:
            if letter in freqS1:
                freqS1[letter] += 1
            else:
                freqS1[letter] = 1

        for i in range(len(s2)):
            if i >= lens1:
                freqS2[s2[i - lens1]] -= 1 
                if freqS2[s2[i - lens1]] == 0:
                    del freqS2[s2[i - lens1]]  
            
            if s2[i] not in freqS2:
                freqS2[s2[i]] = 1
            else:
                freqS2[s2[i]] += 1     
            if freqS2 == freqS1:
                return True   
        return False                          
        