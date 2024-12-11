class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        left =0
        for right in range(len(nums)):
            if nums[right] - nums[left] >2*k:
                left+=1
        return right-left+1
