public class Solution {
    public int findUnsortedSubarray(int[] nums) {
        int start = 0;
        while (start < nums.length - 1 && nums[start] <= nums[start + 1]) {
            start++;
        }
        
        if (start == nums.length - 1) {
            return 0;
        }
        
        int end = nums.length - 1;
        while (end > 0 && nums[end] >= nums[end - 1]) {
            end--;
        }
        
        int mini = Integer.MAX_VALUE, maxi = Integer.MIN_VALUE;
        for (int i = start; i <= end; i++) {
            mini = Math.min(mini, nums[i]);
            maxi = Math.max(maxi, nums[i]);
        }
        
        while (start > 0 && nums[start - 1] > mini) {
            start--;
        }
        
        while (end < nums.length - 1 && nums[end + 1] < maxi) {
            end++;
        }
        
        return end - start + 1;
    }
}
