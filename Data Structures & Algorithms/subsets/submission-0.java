class Solution {
    public List<List<Integer>> subsets(int[] nums) {
       List<List<Integer>> result = new ArrayList<>(); 
       backtrack(result, new ArrayList<>(), nums, 0);
       return result;
    }

    private void backtrack(List<List<Integer>> result, List<Integer> currentPath, int[] nums, int start)
    {
        result.add(new ArrayList<>(currentPath));
        for(int i=start; i<nums.length; i++)
        {
            currentPath.add(nums[i]);
            backtrack(result, currentPath, nums, i + 1);
            currentPath.remove(currentPath.size() - 1);
        }
    }
}
