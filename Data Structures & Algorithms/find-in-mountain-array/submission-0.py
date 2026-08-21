class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()        
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left

        def binarySearch(low, high, target, is_ascending):
            while low <= high:
                mid = (low + high) // 2
                val = mountainArr.get(mid)
                
                if val == target:
                    return mid
                
                if is_ascending:
                    if val < target: low = mid + 1
                    else: high = mid - 1
                else:
                    if val > target: low = mid + 1
                    else: high = mid - 1
            return -1

        res = binarySearch(0, peak, target, True)
        if res != -1:
            return res
            
        return binarySearch(peak + 1, n - 1, target, False)