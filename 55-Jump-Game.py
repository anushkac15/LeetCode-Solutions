class Solution:
    def canJump(self, nums: List[int]) -> bool:
        

        maxInd =0

        for i in range(len(nums)):

            if i>maxInd:
                return False

            maxInd = max(maxInd, i+nums[i])

        return True