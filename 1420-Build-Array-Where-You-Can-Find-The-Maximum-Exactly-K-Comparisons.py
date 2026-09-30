class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:

        def solve(i, prev, k):

            mod = 10**9 + 7

            if i == n:
                if k == 0:
                    return 1
                else:
                    return 0

            if k < 0:
                return 0

            ans = 0

            if dp[i][prev][k] != -1:
                return dp[i][prev][k]

            for num in range(1, m + 1):
                if num > prev:
                    ans += solve(i + 1, num, k - 1)
                else:
                    ans += solve(i + 1, prev, k)

            dp[i][prev][k] = ans % mod
            return dp[i][prev][k]

        dp = [[[-1] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        return solve(0, 0, k)
