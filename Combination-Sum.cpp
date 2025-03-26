class Solution {
public:

    void solve(vector<int>& nums, vector<vector<int>>& res, vector<int>& temp, int target, int i ){

        if(target==0){
            res.push_back(temp);
            return ;
        }

        for(int idx =i;idx<nums.size();idx++){

            if(nums[idx]>target){
                break;
            }
            temp.push_back(nums[idx]);
            solve(nums, res, temp, target-nums[idx], idx);
            temp.pop_back();
        }
    }
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {

        sort(nums.begin(), nums.end());

        vector<vector<int>> res;
        vector<int> temp;

        solve(nums, res, temp, target, 0);
        return res;


        
    }
};