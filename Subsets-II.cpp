class Solution {
public:

    void solve(vector<int>& nums, vector<vector<int>>& res, vector<int>& temp, int i){

        res.push_back(temp);

        for(int idx = i;idx<nums.size();idx++){
            if(i!=idx && nums[idx] == nums[idx-1]){
                continue;
            }

            temp.push_back(nums[idx]);
            solve(nums, res, temp, idx+1);
            temp.pop_back();
        }
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {

        sort(nums.begin(), nums.end());
        vector<int> temp;
        vector<vector<int>> res;

        solve(nums, res, temp, 0);

        return res;
        
    }
};