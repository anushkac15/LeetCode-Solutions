class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def solve(prev, curr, dp):

            if curr == len(nums):
                return 0

            if dp[prev][curr]!=-1:
                return dp[prev][curr]

            take =0

            if prev==-1 or nums[prev] <nums[curr]:
                take = solve(curr, curr+1, dp)+1
            
            notTake = solve(prev, curr+1, dp)

            dp[prev][curr] = max(take, notTake)

            return dp[prev][curr]

        dp = [[-1]* len(nums) for _ in range (len(nums)+1)]

        return solve(-1,0,dp)


        