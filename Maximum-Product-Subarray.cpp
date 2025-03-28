class Solution {
public:
    int maxProduct(vector<int>& nums) {

        int pro1 = nums[0];
        int pro2 = nums[0];
        int res =nums[0];

        for(int i =1;i< nums.size();i++){
            int temp = max({nums[i], pro1*nums[i], pro2*nums[i]});
            pro2 = min({nums[i], pro1*nums[i], pro2*nums[i]});
            pro1 = temp;
            res = max(pro1, res);
        }
        return res;
        
    }
};