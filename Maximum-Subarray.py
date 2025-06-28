class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum =0
        maxi =-inf
        
        for num in nums:

            sum+=num

            if(sum>maxi):
                maxi = max(sum, maxi)

            if(sum<0):
                sum=0
        
        return maxi

        