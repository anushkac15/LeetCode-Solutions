class Solution {
public:
    bool solver(vector<int>& nums, vector<int>& visited, int start_index, int k, int current_sum, int target) {
        if (k == 0) return true;  
        if (current_sum == target) {
            
            return solver(nums, visited, 0, k - 1, 0, target);
        }

        for (int i = start_index; i < nums.size(); i++) {
            if (!visited[i] && current_sum + nums[i] <= target) {
                visited[i] = 1;  
                if (solver(nums, visited, i + 1, k, current_sum + nums[i], target)) {
                    return true;
                }
                visited[i] = 0;  
               if (current_sum == 0)
                    return false;
            }
        }

        return false;
    }

    bool canPartitionKSubsets(vector<int>& nums, int k) {
        int sum = accumulate(nums.begin(), nums.end(), 0);
        if (sum % k != 0) return false;  

        int target = sum / k;
        vector<int> visited(nums.size(), 0);
        sort(nums.begin(), nums.end(), greater<int>()); 
        return solver(nums, visited, 0, k, 0, target);
    }
};