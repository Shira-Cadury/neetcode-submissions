class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) <= len(nums2):
            A = nums1
            B = nums2
        else:
            B = nums1
            A = nums2    
        left, right = 0, len(A)
        total = len(A) + len(B)
        half = (total + 1) // 2
        while left <= right:
            i = (left + right) // 2   
            j = half - i
            A_left  = A[i-1] if i > 0 else float('-inf')
            A_right = A[i]   if i < len(A) else float('inf')
    
            B_left  = B[j-1] if j > 0 else float('-inf')
            B_right = B[j]   if j < len(B) else float('inf')
            if A_left <= B_right and B_left <= A_right:
                if total % 2 != 0:
                    return max(A_left, B_left)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2    
            elif A_left > B_right:
                right = i - 1
            else:
                left = i + 1        
