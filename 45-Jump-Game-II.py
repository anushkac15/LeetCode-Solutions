class Solution:
    def jump(self, nums: List[int]) -> int:
        

        maxInd =0
        currInd =0
        jump =0

        for i in range(len(nums)-1):

            maxInd = max(maxInd, i+nums[i])

            if i==currInd :
                currInd = maxInd 
                jump+=1

            if i>=len(nums):
                break

        return jump
