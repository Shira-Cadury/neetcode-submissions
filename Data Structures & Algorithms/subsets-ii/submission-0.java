class Solution {
    private List<List<Integer>> ans;
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        this.ans = new ArrayList<>();
        helper(nums,new ArrayList<>(), 0);
        return ans;
    }
    private void helper( int[] nums,List<Integer> curr, int index)
    {
        ans.add(new ArrayList<>(curr));
        for(int i=index; i<nums.length; i++)
        {
            if (i > index && nums[i] == nums[i-1])
                continue;   
            curr.add(nums[i]);
            helper(nums,curr, i+1);
            curr.remove(curr.size() - 1);    
        }
    }
}
