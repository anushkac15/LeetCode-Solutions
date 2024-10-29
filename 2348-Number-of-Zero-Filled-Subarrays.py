class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans =0
        cnt =1
        for i in range(len(nums)):
            if nums[i] ==0:
                ans+=cnt
                cnt+=1

            else:
                cnt =1
        return ans

        