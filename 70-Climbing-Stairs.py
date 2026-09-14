class Solution:
    def climbStairs(self, n: int) -> int:

        def solve(i, dp):

            if i<0:
                return 
            
            if i==0 or i==1 or i==2:
                return i

            if dp[i] !=-1:
                return dp[i]

            step1 = solve(i-1, dp)
            step2 = solve(i-2, dp)

            dp[i] = step1 +step2
            return dp[i]

        dp = [-1] * (n+1)
        return solve(n, dp)

            