class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def solve(i, amount, dp):

            if amount == 0:
                return 0

            if i >= len(coins) or amount < 0:
                return float("inf")

            if dp[i][amount] != -1:
                return dp[i][amount]

            take = solve(i, amount - coins[i], dp) + 1
            notTake = solve(i + 1, amount, dp)

            dp[i][amount] = min(take, notTake)
            return dp[i][amount]

        dp = [[-1] * (amount + 1) for _ in range(len(coins))]
        return solve(0, amount, dp) if solve(0, amount, dp) != float("inf") else -1
