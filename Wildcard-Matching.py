class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def solve(i1, i2, dp):

            if i1==len(s) and i2 == len(p):
                return True

            if i1<len(s) and i2==len(p):
                return False

            if i1==len(s) and i2 <len(p):

                for i in range(i2, len(p)):
                    if p[i] !='*':
                        return False
                return True

            if dp[i1][i2] !=-1:
                return dp[i1][i2]

            if s[i1] ==p[i2] or p[i2] == '?':
                dp[i1][i2] = solve(i1+1, i2+1, dp)
                return dp[i1][i2]

            if p[i2] =='*':
                dp[i1][i2] = solve(i1+1, i2, dp) or solve(i1, i2+1, dp)
                return dp[i1][i2]

            dp[i1][i2] = False
            return dp[i1][i2]

        dp = [[-1 for _ in range(len(p))] for _ in range(len(s))]

        return solve(0, 0, dp)