class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        res = right
        while left <= right:
            mid = (left + right) // 2
            count = 1
            sums = 0
            for i in nums:
                sums += i
                if sums > mid:
                    count += 1
                    sums = i  
            if count <= k:
                right = mid - 1
                res = mid
            else:
                left = mid + 1
                
        return res                        