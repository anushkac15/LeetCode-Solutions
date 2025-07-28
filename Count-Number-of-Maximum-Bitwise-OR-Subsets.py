class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        n = len(nums)

        maxi =0

        for num in nums:
            maxi|=num

        def solve(curr,i):
            if i==n and curr !=maxi:
                return 0

            if curr ==maxi:
                return 2**(n-i)

            cnt =0

            cnt+=solve(curr|nums[i],i+1)

            cnt+=solve(curr,i+1)

            return cnt

        return solve(0,0)