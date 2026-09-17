class Solution {
public:
    int climbStairs(int n) {
        int one = 1;
        int tow = 1;
        for (int i = 0; i < n - 1; i++){
            int temp = tow;
            tow = one;
            one = one + temp;
        }
        return one;
    }
};
