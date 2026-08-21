class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
       res = [-1, -1]
       left, right = 0, len(numbers) - 1
       while left < right:
            sums = numbers[left] + numbers[right]
            if sums == target:
                res[0] = left + 1
                res[1] = right + 1
                return res
            elif sums < target:
                left += 1
            else:
                right -= 1
