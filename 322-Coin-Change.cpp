class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {

        vector<int> dp(amount+1, INT_MAX);

        dp[0] =0;

        for(int num:coins){
            for(int i =num; i<=amount;i++){
                if(dp[i-num] != INT_MAX){
                    dp[i] = min(dp[i], dp[i-num]+1);
                }
            }
        }

        if(dp[amount]==INT_MAX){
            return -1;
        }
        else{
            return dp[amount];
        }

        
    }
};