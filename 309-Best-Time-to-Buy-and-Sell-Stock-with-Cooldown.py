class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        def solve(i, buy):

            if i >= len(prices):
                return 0

            if dp[i][buy] != -1:
                return dp[i][buy]

            if buy:

                take = solve(i + 1, 0) - prices[i]
                notTake = solve(i + 1, 1)

                dp[i][buy] = max(take, notTake)

            else:
                sell = solve(i + 2, 1) + prices[i]
                notSell = solve(i + 1, 0)

                dp[i][buy] = max(sell, notSell)

            return dp[i][buy]

        dp = [[-1] * 2 for _ in range(len(prices))]

        return solve(0, 1)
