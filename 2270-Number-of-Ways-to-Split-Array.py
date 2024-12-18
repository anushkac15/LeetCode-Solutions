class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:

        left=0
        right = sum(nums)
        cnt=0

        for i in range(len(nums)-1):
            left+=nums[i]
            right-=nums[i]
            if left>= right:
                cnt+=1
        return cnt
        