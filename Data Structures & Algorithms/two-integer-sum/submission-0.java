class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> temp=new HashMap<>();
        int[] res={-1,-1};
        for(int i=0; i<nums.length; i++)
        {
            if(temp.containsKey(target-nums[i]))
            {
                res[0]=temp.get(target-nums[i]);
                res[1]=i;
                break;
            }
            else{
                temp.put(nums[i], i);
            }
        }
        return res;
    }
}
