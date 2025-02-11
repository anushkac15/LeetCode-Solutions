class Solution {
public:

    void dfs(vector<vector<int>>& image, int i, int j, int val, int color){
        if(i<0||i>=image.size()||j<0||j>=image[0].size()|| image[i][j] == color|| image[i][j]!=val){
            return ;
        }
        image[i][j] =color;
        dfs(image, i+1, j,val, color);
        dfs(image, i-1,j,val,color);
        dfs(image, i, j-1, val,color);
        dfs(image, i, j+1, val,color);
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {

        int val = image[sr][sc];

        dfs(image, sr,sc, val, color);
        return image;
        
    }
};