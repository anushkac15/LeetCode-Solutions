class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans =0
        cnt =0
        for i in range(len(nums)):
            if nums[i] ==0:
                cnt+=1
                ans+=cnt

            else:
                cnt =0
        return ans 