class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minii = min(nums)
        ans =0

        for i in range(len(nums)):
            ans+=nums[i] - minii
        return ans

        