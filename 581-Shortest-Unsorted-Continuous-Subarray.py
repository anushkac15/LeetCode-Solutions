class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start = 0
        while start < len(nums) - 1 and nums[start] <= nums[start + 1]:
            start += 1
        
        if start == len(nums) - 1:
            return 0
        
        end = len(nums) - 1
        while end > 0 and nums[end] >= nums[end - 1]:
            end -= 1
        
        mini = min(nums[start:end + 1])
        maxi = max(nums[start:end + 1])

        while start > 0 and nums[start - 1] > mini:
            start -= 1
        while end < len(nums) - 1 and nums[end + 1] < maxi:
            end += 1

        return end - start + 1
