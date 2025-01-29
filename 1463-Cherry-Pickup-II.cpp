class Solution {
public:

    int dfs(int i, int j1, int j2,int m , int n, vector<vector<int>>& grid, vector<vector<vector<int>>>& dp){
        if(j1<0|| j1>=n|| j2<0 || j2>=n){
            return -1e9;
        }

        if(dp[i][j1][j2]!=-1){
            return dp[i][j1][j2];
        }

        if(i==m-1){
            if(j1==j2){
                return grid[i][j1];
            }
            return grid[i][j1]+grid[i][j2];
        }

        int maxi = INT_MIN;
    
    for (int di = -1; di <= 1; di++) {
        for (int dj = -1; dj <= 1; dj++) {
            int ans;
            
            if (j1 == j2)
                ans = grid[i][j1] + dfs(i + 1, j1 + di, j2 + dj, m, n, grid, dp);
            else
                ans = grid[i][j1] + grid[i][j2] + dfs(i + 1, j1 + di, j2 + dj, m, n, grid, dp);
            
            maxi = max(maxi, ans);
        }
    }
    
    return dp[i][j1][j2] = maxi;

    }
    int cherryPickup(vector<vector<int>>& grid) {

        int m = grid.size();
        int n = grid[0].size();

        vector<vector<vector<int>>> dp(m, vector<vector<int>>(n, vector<int>(n, -1)));
        return dfs(0,0, n-1,m, n, grid, dp);   
    }
};