class Solution {
    public int findKthLargest(int[] nums, int k) {
      PriorityQueue<Integer> minHeap = new PriorityQueue<>();
      minHeap.add(nums[0]);
      int i=1;
      while(i < nums.length)  
      {
         minHeap.add(nums[i]);
        if(k < minHeap.size())
        {  
            minHeap.poll();           
        }  
        i++;    
      } 
      return minHeap.peek();       
    }
}
