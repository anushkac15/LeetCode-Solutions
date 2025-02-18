#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int rows, cols;

    void dfs(vector<vector<int>>& heights, vector<vector<int>>& visited, int i, int j) {
        if (i < 0 || j < 0 || i >= rows || j >= cols || visited[i][j] == 1) {
            return;  
        }

        visited[i][j] = 1; 

        if (i + 1 < rows && heights[i + 1][j] >= heights[i][j]) {
            dfs(heights, visited, i + 1, j);
        }
        if (i - 1 >= 0 && heights[i - 1][j] >= heights[i][j]) {
            dfs(heights, visited, i - 1, j);
        }
        if (j + 1 < cols && heights[i][j + 1] >= heights[i][j]) {
            dfs(heights, visited, i, j + 1);
        }
        if (j - 1 >= 0 && heights[i][j - 1] >= heights[i][j]) {
            dfs(heights, visited, i, j - 1);
        }
    }

    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        rows = heights.size();
        cols = heights[0].size();
        vector<vector<int>> pacific(rows, vector<int>(cols, 0));
        vector<vector<int>> atlantic(rows, vector<int>(cols, 0));
        vector<vector<int>> ans;

        for (int i = 0; i < rows; i++) {
            dfs(heights, pacific, i, 0);  
        }
        for (int j = 0; j < cols; j++) {
            dfs(heights, pacific, 0, j);  
        }

        for (int i = 0; i < rows; i++) {
            dfs(heights, atlantic, i, cols - 1);  
        }
        for (int j = 0; j < cols; j++) {
            dfs(heights, atlantic, rows - 1, j);  
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (pacific[i][j] == 1 && atlantic[i][j] == 1) {
                    ans.push_back({i, j});
                }
            }
        }

        return ans;
    }
};


       
