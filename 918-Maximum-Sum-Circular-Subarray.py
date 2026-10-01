class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:

        if max(nums) < 0:
            return max(nums)

        maxi = float("-inf")
        maxSum = 0

        for n in nums:
            maxSum += n

            if maxSum < 0:
                maxSum = 0

            maxi = max(maxi, maxSum)

        mini = float("inf")
        minSum = 0

        for n in nums:
            minSum += n

            if minSum > 0:
                minSum = 0

            mini = min(mini, minSum)

        return max(maxi, sum(nums) - mini)
