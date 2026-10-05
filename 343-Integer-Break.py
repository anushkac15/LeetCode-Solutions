class Solution:
    def integerBreak(self, n: int) -> int:

        def solve(num):

            if dp[num] != -1:
                return dp[num]

            for i in range(1, num):

                val = max(i * (num - i),
                          i * solve(num - i))

                dp[num] = max(dp[num], val)

            return dp[num]

        dp = [-1] * (n + 1)

        return solve(n)