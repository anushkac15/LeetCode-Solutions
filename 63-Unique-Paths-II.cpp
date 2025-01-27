class Solution {
public:

    int ways(int i, int j, vector<vector<int>> &memo,vector<vector<int>>& obstacleGrid){
        if(i==0 && j==0){
            return 1;
        }

        if(i<0 || j<0){
            return 0;
        }

        if(memo[i][j] != -1){
            return memo[i][j];
        }
        if(obstacleGrid[i][j]==1){
            return 0;
        }
        int left = ways(i,j-1, memo,obstacleGrid);
        int up = ways(i-1,j, memo, obstacleGrid);

        return memo[i][j] = up+left;
    }
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        vector<vector<int>> memo(m,vector<int>(n,-1));

        if(obstacleGrid[0][0]==1){
            return 0;
        }
        return ways(m-1,n-1,memo, obstacleGrid);
        
    }
};