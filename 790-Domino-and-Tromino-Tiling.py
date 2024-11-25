class Solution:
    def numTilings(self, n: int) -> int:
        dp = [1,1,2]
        if n <= 2:
            return dp[n]
        for i in range(3, n + 1):
            dp.append(2 * dp[i - 1] + dp[i - 3])
        return dp[n] % (10**9 + 7)
