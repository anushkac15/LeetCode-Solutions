class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7

        dp = [[0] * k for _ in range(n)]

        for i in range(m):
            for j in range(n):

                curr = [0] * k
                val = grid[i][j] % k

                if i == 0 and j == 0:
                    curr[val] = 1

                else:
                    if i > 0:
                        for rem in range(k):
                            new_rem = (rem + val) % k
                            curr[new_rem] += dp[j][rem]
                            curr[new_rem] %= MOD

                    if j > 0:
                        for rem in range(k):
                            new_rem = (rem + val) % k
                            curr[new_rem] += dp[j - 1][rem]
                            curr[new_rem] %= MOD

                dp[j] = curr

        return dp[n - 1][0]