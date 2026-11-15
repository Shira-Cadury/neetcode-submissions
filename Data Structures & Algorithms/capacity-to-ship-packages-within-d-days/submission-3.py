class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = left
        while left <= right:
            mid = (left + right) // 2
            current_load = 0
            num_days = 1
            for w in weights:
                if w + current_load > mid:
                    num_days += 1
                    current_load = 0
                current_load += w
            if num_days <= days:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res                       