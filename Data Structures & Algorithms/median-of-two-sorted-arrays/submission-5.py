class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
            
        total = len(A) + len(B)
        half = (total + 1) // 2 
        
        left, right = 0, len(A)
        
        while left <= right:
            i = (left + right) // 2 
            j = half - i            
            
            L1 = A[i - 1] if i > 0 else float("-inf")
            R1 = A[i] if i < len(A) else float("inf")
            
            L2 = B[j - 1] if j > 0 else float("-inf")
            R2 = B[j] if j < len(B) else float("inf")
            
            if L1 <= R2 and L2 <= R1:
                
                if total % 2:
                    return float(max(L1, L2))
                
                return (max(L1, L2) + min(R1, R2)) / 2.0
                
            elif L1 > R2:
                right = i - 1
            else:
                left = i + 1