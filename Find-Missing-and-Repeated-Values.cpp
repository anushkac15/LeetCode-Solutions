class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {

        int n = grid.size();
        unordered_set<int> st;
        vector<int> ans;

        for(int i =0;i<grid.size();i++){
            for(int j=0;j<grid.size();j++){
                if(st.find(grid[i][j]) != st.end()){
                    ans.push_back(grid[i][j]);
                }
                st.insert(grid[i][j]);
            }
        }

        for(int i =1;i<= n*n;i++){
            if(st.find(i) == st.end()){
                ans.push_back(i);
            }
        }

        return ans;

        
    }
};