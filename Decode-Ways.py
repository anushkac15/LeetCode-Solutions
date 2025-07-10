class Solution:
    def numDecodings(self, s: str) -> int:

        def solve(i,dp):

            if i==len(s):
                return 1

            if s[i]=='0':
                return 0

            if dp[i] !=-1:
                return dp[i]

            cnt = solve(i+1,dp)

            if i+1<len(s) and 10<=int(s[i:i+2])<=26:
                cnt += solve(i+2,dp)

            dp[i] = cnt
            return dp[i]

        dp = [-1 for _ in range(len(s))]
        return solve(0,dp)     