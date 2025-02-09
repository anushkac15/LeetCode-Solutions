class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int n = nums.size();

        int gola_idx = -1;

        for(int i = n-1;i>0;i--){
            if(nums[i-1]<nums[i]){
                gola_idx = i-1;
                break;
            }
        }


        if(gola_idx != -1){

            int swap_idx = gola_idx;

            for(int j =n-1;j>=gola_idx+1;j--){

                if(nums[j]>nums[gola_idx]){
                    swap_idx = j;
                    break;
                }

                
            }
            swap(nums[swap_idx], nums[gola_idx]);

        }

        reverse(nums.begin()+gola_idx+1, nums.end());        
    }
};