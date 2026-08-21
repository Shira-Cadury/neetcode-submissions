class Solution {
    public boolean isPalindrome(String s) {
        int i=0, j=s.length()-1;
        while(i < j)
        {
            if(Character.toLowerCase(s.charAt(i)) == Character.toLowerCase(s.charAt(j)))
            {
                i++;
                j--;
            }
            else if(s.charAt(i) == ' ' || !Character.isLetterOrDigit(s.charAt(i)))
            {
                i++;
            }
            else if(s.charAt(j) == ' ' || !Character.isLetterOrDigit(s.charAt(j)))
            {
                j--;
            }
            else if(s.charAt(i) != s.charAt(j))
            {
                return false;
            }           
        }
        return true;
    }
}
