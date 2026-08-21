class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right
        while left <= right:
            mid = (left + right) // 2
            current_load = 0
            used_days = 1

            for w in weights:
                if current_load + w > mid:
                    used_days += 1
                    current_load = 0
                current_load += w

            if used_days <= days:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res            
