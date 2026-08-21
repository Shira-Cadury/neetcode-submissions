class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        
        countT = {}
        for char in t:
            countT[char] = countT.get(char, 0) + 1
            
        window = {}
        have, need = 0, len(countT)
        
        res, resLen = [-1, -1], float('inf')
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            
            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1
                
                left_char = s[left]
                window[left_char] -= 1
                
                if left_char in countT and window[left_char] < countT[left_char]:
                    have -= 1
                
                left += 1  
        l, r = res
        return s[l : r + 1] if resLen != float('inf') else ""          