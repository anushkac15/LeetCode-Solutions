class Solution {
public:

    int solve(string& s, string& t){

        int m = s.size();
        int n = t.size();
        vector<vector<int>>dp(m+1, vector<int>(n+1, -1));

        for(int i =0;i<=n;i++){
            dp[0][i] =0;
        }

        for(int j =0;j<=m;j++){
            dp[j][0] =0;
        }

        for(int i =1;i<=m;i++){
            for(int j =1;j<=n;j++){
                if(s[i-1]==t[j-1]){
                    dp[i][j] = 1+dp[i-1][j-1];
                }
                else{
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }

        return dp[m][n];
    }
    int minDistance(string word1, string word2) {
        int m = word1.size();
        int n = word2.size();

        int k = solve(word1, word2);

        return (m-k) + (n-k);
    }
};