class Solution {
    public int lastStoneWeight(int[] stones) {
        if(stones.length <= 0)
            return 0;
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
         for (int num : stones) 
            maxHeap.add(num);    
        int x,y;    
        while(maxHeap.size() > 1) 
        {
            x=maxHeap.poll();
            y=maxHeap.poll();
            if(x != y)
                maxHeap.add(x-y);       
        }   
        if(maxHeap.size() == 1)
            return maxHeap.peek();
        return 0;    
    }
}
