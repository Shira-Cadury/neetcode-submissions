class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        res=[]    
        digit_map = {
             "2": "abc",
             "3": "def",
             "4": "ghi",
             "5": "jkl",
             "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }   
        def helper(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            current_digit = digits[i]
            letters = digit_map[current_digit]
            for char in letters:
                helper(i + 1, curr + char)

        helper(0, "")
        return res        
