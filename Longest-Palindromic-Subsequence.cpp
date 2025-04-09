class Solution {
public:

    int solve(string& s, int i, int j, vector<vector<int>>&dp){

        if(i>j){
            return 0;
        }

        if(i==j){
            return 1;
        }

        if(dp[i][j]!=-1){
            return dp[i][j];
        }

        if(s[i]==s[j]){
            dp[i][j] = solve(s, i+1, j-1, dp)+2;
        }

        else{
            dp[i][j] = max(solve(s, i+1, j, dp), solve(s, i, j-1, dp));
        }

        return dp[i][j];
    }
    int longestPalindromeSubseq(string s) {

        int n = s.size();

        vector<vector<int>>dp(n+1, vector<int>(n+1, -1));

        return solve(s, 0, n-1,dp);

        
    }
};