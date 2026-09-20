class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False

        def solve(i, j):

            k = i + j

            if i == len(s1) and j == len(s2) and k == len(s3):
                return True

            if k == len(s3):
                return False

            if dp[i][j] != -1:
                return dp[i][j]

            take1 = take2 = False

            if i < len(s1) and s1[i] == s3[k]:
                take1 = solve(i + 1, j)
            if j < len(s2) and s2[j] == s3[k]:
                take2 = solve(i, j + 1)

            dp[i][j] = take1 or take2
            return dp[i][j]

        dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        return solve(0, 0)
