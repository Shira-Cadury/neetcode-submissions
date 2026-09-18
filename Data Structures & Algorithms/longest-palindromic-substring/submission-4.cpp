class Solution {
private:
    pair<int, int> lenPalindrome(int left, int right, const string s){
        while (left >= 0 && right < size(s) and s[left] == s[right]){
            left--;
            right++;
        }
        return {left + 1, right};
    }    
public:
    string longestPalindrome(string s) {
        if (size(s) == 0){
            return "";
        }
        int maxLen = 0;
        int maxLeft = 0;
        int maxRight = 0;

        for (int i = 0; i < size(s); i++){
            pair<int, int> bounds = lenPalindrome(i, i, s);
            int left = bounds.first;
            int right = bounds.second;

            if ((right - left) > maxLen){
                maxLen = right - left;
                maxLeft = left;
                maxRight = right;
            } 

            bounds = lenPalindrome(i, i + 1, s);
            left = bounds.first;
            right = bounds.second;

            if ((right - left) > maxLen){
                maxLen = right - left;
                maxLeft = left;
                maxRight = right;
            } 
        }
        return s.substr(maxLeft, maxLen);
        
    }
};
