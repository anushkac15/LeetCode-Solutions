class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {

        int n = nums.size();
        int maxLis = INT_MIN;

        vector<int>t(n,1);

        for(int i =0;i<n;i++){
            for(int j =0;j<i;j++){

                if(nums[i]>nums[j]){
                    t[i] = max(t[i], t[j]+1);
                }

            }
            maxLis = max(t[i], maxLis);
        }
        return maxLis;
        
    }
};