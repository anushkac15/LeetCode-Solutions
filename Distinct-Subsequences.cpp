class Solution {
public:

    int solve(string&s, string& t, int i, int j, vector<vector<int>>&dp){

        int m = s.size();
        int n = t.size();

        if(j==n){
            return 1;
        }
        if(i==m){
            return 0;
        }

        if(dp[i][j]!=-1){
            return dp[i][j];
        }

        int notTake = solve(s, t, i+1, j, dp);

        int take =0;
        if(s[i]==t[j]){
            take = solve(s, t, i+1, j+1, dp);
        }

        return dp[i][j] = take +notTake;
    }
    int numDistinct(string s, string t) {

        int m = s.size();
        int n = t.size();

        vector<vector<int>> dp(m, vector<int>(n, -1));

        return solve(s, t, 0, 0, dp);
        
    }
};