class Solution {
public:
    long long minimumReplacement(vector<int>& nums) {

        int n = nums.size();

        long long ans =0, prev = nums[n-1];

        for(int i =n-2;i>=0;i--){

            if(nums[i]> prev){
                int t = nums[i]/prev;

                if(nums[i]%prev!=0){
                    t++;
                }
                    prev = nums[i]/t;
                    ans+= t-1;
            }
            else{
                prev = nums[i];
            }


        }

        return ans;
        
    }
};