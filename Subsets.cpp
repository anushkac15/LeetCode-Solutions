class Solution {
public:

    void solve(vector<int>& nums, vector<vector<int>>& res, vector<int>& temp, int i){

        res.push_back(temp);

        for(int idx =i;idx<nums.size();idx++){

            temp.push_back(nums[idx]);
            solve(nums, res, temp, idx+1);
            temp.pop_back();
        }
    }
    vector<vector<int>> subsets(vector<int>& nums) {

        vector<int>temp;
        vector<vector<int>> res;

        solve(nums, res, temp, 0);
        return res;
        
    }
};