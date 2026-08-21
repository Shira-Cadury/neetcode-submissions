class MedianFinder {
    private PriorityQueue<Integer> minHeap;//for numbers  big than the midel
    private PriorityQueue<Integer> maxHeap;
    public MedianFinder() {
        minHeap=new PriorityQueue<>((a,b) -> b-a);
        maxHeap=new PriorityQueue<>((a,b) -> a-b);
    }
    
    public void addNum(int num) {
       maxHeap.add(num);
       minHeap.add(maxHeap.poll());
       if(maxHeap.size() > minHeap.size())
            minHeap.add(maxHeap.poll());
       if(minHeap.size() > maxHeap.size())
            maxHeap.add(minHeap.poll());      
    }
    
    public double findMedian() {
        if(minHeap.size() == maxHeap.size())
        {
            return (double)(minHeap.peek() + maxHeap.peek())/2;
        }
        else{
            if(minHeap.size() > maxHeap.size())
            {
                return (double)minHeap.peek();
            }
            else{
                return (double)maxHeap.peek();
            }
        }
    }
}
