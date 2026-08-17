class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        Sum = [0] * (n + 1)
        for i in range(n):
            Sum[i + 1] = Sum[i] + stoneValue[i]

        dp = [[-1] * n for _ in range(n)]

        def f(l, r):
            if dp[l][r] != -1:
                return dp[l][r]

            ans = 0

            for m in range(l, r):
                Lsum = Sum[m + 1] - Sum[l]
                Rsum = Sum[r + 1] - Sum[m + 1]

                if Lsum <= Rsum:
                    ans = max(ans, Lsum + f(l, m))

                if Lsum >= Rsum:
                    ans = max(ans, Rsum + f(m + 1, r))

                if 2 * min(Lsum, Rsum) <= ans:
                    break

            dp[l][r] = ans
            return ans

        return f(0, n - 1)