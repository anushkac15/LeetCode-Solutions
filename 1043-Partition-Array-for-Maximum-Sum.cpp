class Solution {
public:

    int solve(vector<int>& arr, int i, int k, vector<int>&dp){

        if(i>=arr.size()){
            return 0;
        }

        if(dp[i]!=-1){
            return dp[i];
        }

        int maxi = 0;
        int end = min(int(arr.size()), i+k);

        int ans =0;


        for(int idx =i;idx<end;idx++){

            maxi = max(maxi, arr[idx]);
            ans = max(ans, maxi*(idx-i+1) + solve(arr, idx+1, k, dp));

        }

        return dp[i]=ans;
    }
    int maxSumAfterPartitioning(vector<int>& arr, int k) {

        vector<int> dp(arr.size(), -1);
        return solve(arr, 0, k,dp);
 
        
    }
};