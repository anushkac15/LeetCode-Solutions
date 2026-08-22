class Solution:
    def climbStairs(self, n: int) -> int:

        def solve(n,dp):
            if n<0:
                return 0

            if n==0 or n==1 or n==2:
                return n

            if dp[n]!=-1:
                return dp[n]

            step1 = solve(n-2, dp)
            step2 = solve(n-1,dp)

            dp[n] = step1 +step2 
            return dp[n]

        dp = [-1] *(n+1)
        return solve(n,dp)
        