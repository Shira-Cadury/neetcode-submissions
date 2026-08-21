class Solution {
    private List<List<Integer>> ans;
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        this.ans = new ArrayList<>();
        Arrays.sort(candidates);
        helper(candidates, target, 0,new ArrayList<>());
        return ans;
    }

    private void helper(int[] candidates, int target, int i, List<Integer> curr)
    {
        if(target == 0)
        {
            ans.add(new ArrayList<>(curr));
            return;
        }
        if(target < 0)
            return;

        for(int j=i; j<candidates.length; j++)
        {
            if (j > i && candidates[j] == candidates[j-1])
                continue;
            curr.add(candidates[j]);
            helper(candidates, target-candidates[j], j+1, curr);
            curr.remove(curr.size()-1);    
        }    
    }
}
