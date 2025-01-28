class Solution {
public:
    
    int DFS(vector<vector<int>>& grid, vector<vector<bool>>& visited, int m, int n){

        if(m<0 || m>=grid.size() || n<0 || n>=grid[0].size() || grid[m][n] ==0 || visited[m][n]){
            return 0;
        }
        visited[m][n] = true;

        return grid[m][n]+DFS(grid, visited, m, n+1)+DFS(grid, visited, m, n-1)+ DFS(grid, visited, m-1, n)+DFS(grid, visited, m+1, n);

        


    }
    int findMaxFish(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<bool>> visited(m, vector<bool>(n, false));

        int res =0;

        for(int i =0;i<m;i++){
            for(int j =0;j<n;j++){
                if(grid[i][j] >0 && !visited[i][j]){
                    res = max(res, DFS(grid, visited, i,j));
                }
            }
        }
        return res;

    }
};