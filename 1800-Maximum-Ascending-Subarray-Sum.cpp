class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {

        int maxsum =nums[0];
        int  currsum =nums[0];

        for(int i =1;i<nums.size();i++){
            if(nums[i]>nums[i-1]){
                currsum+=nums[i];
                maxsum= max(maxsum, currsum);
            }
            else{
                currsum=nums[i];
            }
        }
        
        return maxsum;
    }
};