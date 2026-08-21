class Solution {
    private List<List<Integer>> ans;
    public List<List<Integer>> permute(int[] nums) {
        this.ans = new ArrayList<>();
        helper(nums,new ArrayList<>());
        return ans;
    }

    private void helper(int[] nums, List<Integer> curr) 
    {
        if (curr.size() == nums.length) {
        ans.add(new ArrayList<>(curr));
        return;
        }
        for(int i=0; i<nums.length; i++)
        {
            if(curr.contains(nums[i]))
                continue;
            curr.add(nums[i]);
            helper(nums,curr);
            curr.remove(curr.size() - 1);    
        }
    }
}
