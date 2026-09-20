class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def solve(i, j):

            if i == len(s) and j == len(p):
                return True

            if j == len(p):
                return False

            if i == len(s):

                if j + 1 < len(p) and p[j + 1] == "*":
                    return solve(i, j + 2)

                return False

            if dp[i][j] != -1:
                return dp[i][j]

            take1 = take2 = False

            if s[i] == p[j] or p[j] == ".":
                take1 = solve(i + 1, j + 1)

            if j + 1 < len(p) and p[j + 1] == "*":

                take2 = solve(i, j + 2)

                if s[i] == p[j] or p[j] == ".":
                    take2 = take2 or solve(i + 1, j)

            dp[i][j] = take1 or take2

            return dp[i][j]

        dp = [[-1] * len(p) for _ in range(len(s))]
        return solve(0, 0)
