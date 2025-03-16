class Solution {
public:
    int minimumDeletions(vector<int>& nums) {

        int n = nums.size();

        int l =0, l1 =0;
        int r = n-1, r1 = n-1;
        int maxi = *max_element(nums.begin(), nums.end());  
        int mini = *min_element(nums.begin(), nums.end());

        while(nums[l]!= maxi){
            l++;
        }
        while(nums[r]!= maxi){
            r--;
        }
        while(nums[l1] != mini){
            l1++;
        }
        while(nums[r1]!= mini){
            r1--;
        }
        int ans1 = max(l1, l) + 1;      
        int ans2 = max(n - r, n - r1);  
        int ans3 = l1 + (n - r) + 1;    
        int ans4 = l + (n - r1) + 1;   

        return min({ans1, ans2, ans3, ans4});

        
    }
};