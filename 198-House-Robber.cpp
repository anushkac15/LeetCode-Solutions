class Solution {
public:
    int rob(vector<int>& nums) {

        vector<int> res(nums.size() +1, 0);

        res[0] =0;
        res[1] = nums[0];

        for (int i=2;i<=nums.size();i++){
            int steal = nums[i-1] +res[i-2];
            int skip = res[i-1];

            res[i] = max(steal,skip);
        }
        return res[nums.size()];
    }
};