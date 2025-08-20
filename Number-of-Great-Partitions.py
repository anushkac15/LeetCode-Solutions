class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:

        total = sum(nums)
        mod = 10**9+7

        if total < 2*k:
            return 0

        dp=[[-1  for _ in range(k)] for _ in range(len(nums))]

        def solve(i, sum):

            if i==len(nums):
                return 1

            if dp[i][sum]!=-1:
                return dp[i][sum]

            notTake = solve(i+1, sum)

            if sum+nums[i]<k:
                notTake =(notTake+solve(i+1, sum+nums[i]))%mod

            dp[i][sum]=notTake 
            return dp[i][sum]

        TotalPoss = pow(2,len(nums),mod)
        badPart = (solve(0,0)*2)%mod

        return (TotalPoss-badPart)%mod     