class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False

        def solve(i, target, dp):

            if target == 0:
                return True

            if target < 0 or i >= len(nums):
                return False

            if dp[i][target] != -1:
                return dp[i][target]

            take = solve(i + 1, target - nums[i], dp)
            notTake = solve(i + 1, target, dp)

            dp[i][target] = max(take, notTake)
            return dp[i][target]

        target = sum(nums) // 2
        dp = [[-1] * (target + 1) for _ in range(len(nums))]
        return solve(0, target, dp)
