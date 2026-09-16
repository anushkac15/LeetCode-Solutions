class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def solve(i, j, dp):

            if i < 0:
                return j + 1

            if j < 0:
                return i + 1

            if dp[i][j] != -1:
                return dp[i][j]

            if word1[i] == word2[j]:
                dp[i][j] = solve(i - 1, j - 1, dp)
                return dp[i][j]

            insert = solve(i, j - 1, dp)
            delete = solve(i - 1, j, dp)
            replace = solve(i - 1, j - 1, dp)

            dp[i][j] = 1 + min(insert, min(delete, replace))

            return dp[i][j]

        dp = [[-1] * len(word2) for _ in range(len(word1))]
        return solve(len(word1) - 1, len(word2) - 1, dp)
