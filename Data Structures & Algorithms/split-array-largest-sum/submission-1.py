class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        res = right
        while left <= right:
            mid = (left + right) // 2
            count, sums = 1, 0
            for n in nums:
                if sums + n > mid:
                    count += 1
                    sums = 0
                sums += n

            if count <= k:
                right = mid -1
                res = mid
            else:
                left = mid + 1    
        return res