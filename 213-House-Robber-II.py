class Solution:
    def rob(self, nums: List[int]) -> int:

        def solve(i, end, dp):

            if i>end:
                return 0

            if dp[i]!=-1:
                return dp[i]

            take = solve(i+2,end, dp)+nums[i]
            notTake= solve(i+1,end,dp)

            dp[i] = max(take, notTake)
            return dp[i]

        dp1 = [-1]*len(nums)
        dp2 = [-1] *len(nums)

        if len(nums) ==1:
            return nums[0]

        return max(solve(0,len(nums)-2, dp1), solve(1, len(nums)-1, dp2))

            
        