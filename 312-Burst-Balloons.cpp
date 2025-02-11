class Solution {
public:
    int n;
    int t[501][501]; 
    int solve(vector<int> &nums, int i, int j){
\t\tif(i > j)
\t\t\treturn 0;
        if(i == j){    
            int temp = nums[i];
            if(i - 1 >= 0)  
                temp *= nums[i - 1];
            if(i + 1 < n)
                temp *= nums[i + 1];
            return temp;
        }
\t\tif(t[i][j] != -1) 
\t\t\treturn t[i][j];
        int ans = 0;
\t\t
\t\t
        for(int k = i; k <= j; k++){
\t\t
            int temp = nums[k];
\t\t\t
            if(j + 1 < n)  
                temp *= nums[j + 1];
\t\t\t\t
            if(i - 1 >= 0) 
                temp *= nums[i - 1];
\t\t\t\t
            temp += (solve(nums, i, k - 1) + solve(nums, k + 1, j));
\t\t\t
            ans = max(ans, temp);
        }
        return t[i][j] = ans;
    }
    
    int maxCoins(vector<int>& nums) {
        memset(t, -1, sizeof(t));
\t\t
\t\tvector<int> arr = {1};
        for(int x: nums) 
\t\t\tarr.push_back(x);
        arr.push_back(1);
        n = arr.size();
\t\t
        return solve(arr, 1, arr.size() - 2);
    }
};