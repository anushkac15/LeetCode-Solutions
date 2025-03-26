class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {

        vector<int> nums;

        for(int i=0;i<grid.size();i++){
            for(int j =0;j<grid[0].size();j++){
                nums.push_back(grid[i][j]);
            }
        }

        sort(nums.begin(), nums.end());
        int n = nums.size();
        int rem = nums[0] %x;

        for(int num : nums){
            if(num%x != rem){
                return -1;
            }
        }

        int med = nums[n/2];
        int cnt =0;

        for(int i =0;i<n;i++){
            cnt+= abs(med-nums[i]) /x;
        }

        return cnt;
        
    }
};