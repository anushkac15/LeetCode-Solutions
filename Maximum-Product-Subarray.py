class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        pre = 1
        suff =1

        maxi = -inf

        for i in range(len(nums)):
            
            if(pre==0):
                pre=1
            
            if(suff==0):
                suff =1

            pre*= nums[i]
            suff *= nums[len(nums)-i-1]

            maxi = max(maxi, max(pre,suff))

        return maxi
        