class KthLargest {
    PriorityQueue<Integer> minHeap;
    int k;
    public KthLargest(int k, int[] nums) {
        minHeap=new PriorityQueue<>();
        this.k=k;
        for (int num : nums) 
            add(num);
        
    }
    
    public int add(int val) {
        minHeap.add(val);
        if(k < (minHeap.size()))
            minHeap.poll();
        return minHeap.peek();    
    }
}
