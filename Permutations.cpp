class Solution {
public:

    void solve(vector<int>&nums, vector<vector<int>>& res, int i ){

        if(i>= nums.size()){
            res.push_back(nums);
            return ;
        }

        for(int idx =i;idx<nums.size();idx++){
            swap(nums[i], nums[idx]);
            solve(nums, res, i+1);
            swap(nums[i], nums[idx]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {

        vector<vector<int>>res;
        solve(nums, res,0);
        return res;
        
    }
};