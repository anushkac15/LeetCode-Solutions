class Solution {
public:
    long long minimumReplacement(vector<int>& nums) {

        long long ans =0;
        int n =  nums.size();

        for(int i =n-2;i>=0;i--){
            if(nums[i+1]>=nums[i]){

                continue;

            }
            int t= nums[i]/nums[i+1];

            if(nums[i]%nums[i+1]!=0){
                t++;
            }
            nums[i]/=t;
            ans+=t-1;
        }

        return ans;
        
    }
};