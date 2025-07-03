class Solution:
    def rob(self, nums: List[int]) -> int:

        def solve(i, dp):

            if i>= len(nums):
                return 0

            if dp[i] !=-1:
                return dp[i]

            take = solve(i+2, dp)+nums[i]
            notTake = solve(i+1, dp)

            dp[i] = max(take, notTake)
            return dp[i]

        dp = [-1 for _ in range(len(nums))]
        return solve(0, dp)
        