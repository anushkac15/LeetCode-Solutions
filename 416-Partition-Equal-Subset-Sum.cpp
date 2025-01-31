class Solution {
public:
    bool canPartition(vector<int>& nums) {

        int total_sum =0;

        for(int i =0;i<nums.size();i++){
            total_sum+=nums[i];
        }
        if(total_sum%2!=0){
            return false;
        }
        int target_sum = total_sum/2;


        vector<bool>dp(target_sum+1, false);
        dp[0] =true;

        for(int num: nums){
            for(int i =target_sum;i>=num;i--){
                dp[i]=dp[i] || dp[i-num];
            }
        }

        return dp[target_sum];
    }
};