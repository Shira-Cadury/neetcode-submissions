class Solution {
    public int maxArea(int[] heights) {
        int left=0, right=heights.length-1, max=0;
        while(left < right)
        {
            int sum=(right - left)* (Math.min(heights[left], heights[right]));
            if(sum > max)
            {
                  max=sum; 
            } 
                 if(heights[left] < heights[right])
                    left++;
                 else
                    right--;   
        }
        return max;
    }
}
