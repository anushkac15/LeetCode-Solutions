class Solution {
public:
    bool canPartition(vector<int>& nums) {

        int sum =0;
        int n = nums.size();

        for(int i =0;i<nums.size();i++){
            sum+=nums[i];
        }

        if(sum%2!=0){
            return false;
        }

        int target = sum/2;

        vector<bool>dp(target+1, false);
        dp[0] = true;

        for(auto num : nums){
            for(int i = target;i>num-1;i--){
                dp[i] = dp[i] || dp[i-num];
            }
        }

        return dp[target];


        
    }
};