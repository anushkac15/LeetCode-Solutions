class Solution {
public:

    void solve(vector<int>& nums, vector<vector<int>>& res, vector<int>& temp, int target, int i){

        if(target==0){
            res.push_back(temp);
            return;
        }

        for(int idx =i;idx<nums.size();idx++){
            if(i!= idx && nums[idx]==nums[idx-1]){
                continue;
            }
            if(nums[i]>target){
                break;
            }

            temp.push_back(nums[idx]);
            solve(nums, res, temp, target - nums[idx], idx+1);
            temp.pop_back();
        }

    }
    vector<vector<int>> combinationSum2(vector<int>& nums, int target) {

        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> temp;
        solve(nums, res, temp, target, 0);
        return res;
        
    }
};