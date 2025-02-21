class Solution {
public:

    int solve(int i, int j, string& s, string& t, vector<vector<int>>& dp){
        if(j==t.length()){
            return 1;
        }
        if(i==s.length()){
            return 0;
        }

        if(dp[i][j]!=-1){
            return dp[i][j];
        }

        int notTake = solve(i+1,j, s, t, dp);

        int take =0;

        if(s[i]==t[j]){
            take = solve(i+1, j+1, s, t, dp);
        }

        return dp[i][j] = take+notTake;
    }
    int numDistinct(string s, string t) {

        vector<vector<int>> dp(s.length(), vector<int>(t.length(), -1));

        return solve(0,0, s, t, dp);
        
    }
};