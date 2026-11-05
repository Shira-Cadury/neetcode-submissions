class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_sum = 0
        heights.append(0)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                top_index = stack.pop()
                height = heights[top_index]
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i    
                max_sum = max(max_sum, height * width)
            stack.append(i)
        return max_sum        

        