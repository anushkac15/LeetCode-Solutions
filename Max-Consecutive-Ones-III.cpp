class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {

        int n = nums.size();
        int left = 0, right = 0, length = 0, maxLength = 0, zeros = 0;
        while(right<n){
            if(nums[right] == 0) zeros++;
            if(zeros>k){
                if(nums[left] == 0) zeros--;
                left++;
            }
            if(zeros<=k){
                length = right - left + 1;
                maxLength = max(length, maxLength);
            }
            right++;
        }
        return maxLength;
        
    }
};