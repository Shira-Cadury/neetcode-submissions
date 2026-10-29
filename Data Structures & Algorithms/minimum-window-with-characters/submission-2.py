class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""
        
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
            
        required = len(count_t)
        formed = 0
        count_s = {}
        
        res = [-1, -1]
        res_len = float('inf')
        
        left = 0
        for right in range(len(s)):
            c = s[right]
            count_s[c] = count_s.get(c, 0) + 1
            
            if c in count_t and count_s[c] == count_t[c]:
                formed += 1
                
            while formed == required:
                if (right - left + 1) < res_len:
                    res_len = (right - left + 1)
                    res = [left, right]
                    
                left_char = s[left]
                count_s[left_char] -= 1
                if left_char in count_t and count_s[left_char] < count_t[left_char]:
                    formed -= 1
                left += 1
                
        return s[res[0]:res[1] + 1] if res_len != float('inf') else ""