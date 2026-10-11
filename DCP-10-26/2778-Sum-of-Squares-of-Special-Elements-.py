class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        sum = 0
        n = len(nums)

        for i in range(0, len(nums)):

            if n % (i + 1) == 0:
                sum += nums[i] ** 2

        return sum
