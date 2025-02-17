class Solution {
public:

    void solve(vector<int>& candidate, int i, int target, vector<vector<int>>& ans, vector<int>& temp){

        if(target==0){
            ans.push_back(temp);
            return ;
        }

        if(i>=candidate.size() || target<0){
            return ;
        }

        temp.push_back(candidate[i]);
        solve(candidate, i, target-candidate[i], ans, temp);
        temp.pop_back();
        solve(candidate, i+1, target, ans, temp);
    }
    vector<vector<int>> combinationSum(vector<int>& candidate, int target) {

        vector<vector<int>> ans;
        vector<int> temp;
        solve(candidate, 0, target, ans, temp);

        return ans;
        
    }
};