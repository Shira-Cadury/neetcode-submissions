class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> temp=new HashMap<>();
        for(int num: nums)
        {
            temp.put(num, temp.getOrDefault(num, 0) + 1);
        }
        List<Integer>[] buckets = new List[nums.length + 1];
        for (int num : temp.keySet())
        {
            int f=temp.get(num);
            if (buckets[f] == null) 
            buckets[f] = new ArrayList<>();
            buckets[f].add(num);
        }
        int[] res=new int[k];
        for(int i=0, j=buckets.length-1; i<res.length; j--)
        {
            if(buckets[j] != null)
            {
                for (int num : buckets[j])
                {
                    if(i == k)
                    return res;
                    res[i]=num;
                    i++;
                }    
            }
        }
        return res;
    }
}
