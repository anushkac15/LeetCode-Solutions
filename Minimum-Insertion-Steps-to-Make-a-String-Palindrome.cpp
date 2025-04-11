class Solution {
public:

    int solve(string& s, int i, int j, vector<vector<int>>& dp){
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
            return dp[i][j] = solve(s, i+1, j-1, dp)+2;
        }
        else{
            return dp[i][j] = max(solve(s, i+1, j, dp), solve(s, i, j-1, dp));
        }
    }
    int minInsertions(string s) {

        vector<vector<int>> dp(s.size()+1, vector<int>(s.size()+1, -1));

        return s.size() - solve(s, 0, s.size()-1, dp);
        
    }
};