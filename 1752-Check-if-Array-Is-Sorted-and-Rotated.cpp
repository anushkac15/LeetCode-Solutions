class Solution {
public:
    bool check(vector<int>& nums) {

        int cnt =0;
        
        for(int i =0;i<nums.size()-1;i++){
            if(nums[i]>nums[i+1]){
                cnt+=1;
            }
        }
        if(nums[0]<nums[nums.size()-1]){
            cnt+=1;
        }

        return cnt<=1;
    }
};