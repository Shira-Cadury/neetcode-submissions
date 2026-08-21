class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        
        left_half = self.sortArray(nums[:mid])
        right_half = self.sortArray(nums[mid:])
        
        return self.merge(left_half, right_half)

    def merge(self, L: List[int], R: List[int]) -> List[int]:
        result = []
        i = j = 0 
        
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                result.append(L[i])
                i += 1
            else:
                result.append(R[j])
                j += 1
        
        result.extend(L[i:])
        result.extend(R[j:])
        
        return result