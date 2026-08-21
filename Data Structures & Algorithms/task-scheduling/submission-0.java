class Solution {
    public int leastInterval(char[] tasks, int n) {
        int[] freq=new int[26];
        for(char c: tasks)
            freq[c-'A']++;
        Arrays.sort(freq);
        int max=freq[25]-1;
        int idle=max*n;
        for(int i=24; i>=0; i--)
        {
            if(freq[i] >0)
               idle-=Math.min(freq[i],max);
        }
        return idle > 0 ? tasks.length + idle : tasks.length;      
    }
}
