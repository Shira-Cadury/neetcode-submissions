class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int[] result=new int[2];
        int start=0, end=numbers.length-1;
        while(numbers[start] + numbers[end] != target)
        {
            if(numbers[start] + numbers[end] < target)
            {
                start++;
            }
            else
                end--;
        }
        start++;
        end++;
        result[0]=start;
        result[1]=end;
        return result;
    }
}
