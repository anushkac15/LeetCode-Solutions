class Solution {
public:

    int solve(string& s, string& t, int i, int j, vector<vector<int>>& dp){
        if(i<0){
            return j+1;
        }
        if(j<0){
            return i+1;
        }

        if(dp[i][j]!=-1){
            return dp[i][j];
        }

        if(s[i]==t[j]){
            return dp[i][j] = solve(s, t, i-1, j-1, dp);
        }

        int insert = solve(s, t, i, j-1, dp);
        int del = solve(s, t, i-1, j, dp);
        int replace = solve(s, t, i-1, j-1, dp);

        return dp[i][j] = 1+(min(insert, min(del, replace)));

    }
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();
        vector<vector<int>>dp(m, vector<int>(n, -1));

        return solve(word1, word2, m-1, n-1, dp);
        
    }
};