class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        best = max(nums)
        if best <= 0:
            return best

        maxSum=float('-inf')
        currMax=0

        for s in nums:

            currMax+=s

            if currMax<0:
                currMax=0

            if currMax>maxSum:
                maxSum = max(currMax, maxSum)

        minSum=float('inf')
        currSum=0

        for s in nums:

            currSum +=s

            if currSum>0:
                currSum =0

            if minSum>currSum:
                minSum = min(minSum, currSum)



        return max(maxSum,sum(nums)-minSum)