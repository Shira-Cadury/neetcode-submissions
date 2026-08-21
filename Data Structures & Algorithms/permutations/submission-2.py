class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
            for n in nums:
                if n in curr:
                    continue;
                curr.append(n) 
                helper(curr)
                curr.pop()
        helper([])       
        return res            
        