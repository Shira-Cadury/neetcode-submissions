class Solution {
    private List<List<Integer>> ans;
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        this.ans = new ArrayList<>();
        helper(new ArrayList<>(), target, 0, nums);
        return ans;
    }

    private void helper(List<Integer> curr, int target, int i, int[] nums)
    {
        if(i >= nums.length)
            return;
        if(target == 0)
        {
            ans.add(new ArrayList<>(curr));
            return;
        }
        if(target < 0)
            return;
        curr.add(nums[i]);
        helper(curr, target-nums[i], i, nums);    

        curr.remove(curr.size()-1);
        helper(curr, target, i+1,nums);
    }
}
