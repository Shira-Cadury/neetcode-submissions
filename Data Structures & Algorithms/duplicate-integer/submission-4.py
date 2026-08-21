class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        double = set()
        for n in nums:
            if n in double:
                return True
            double.add(n)    
            
        return False         