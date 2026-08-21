class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maximum=0
        while left < right:
            sum=(right - left)*(min(heights[left], heights[right]))
            if sum > maximum:
                maximum=sum
            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        return maximum              