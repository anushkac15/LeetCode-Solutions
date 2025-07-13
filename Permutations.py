class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def solve(i, nums, res):

            if i>= len(nums):
                res.append(nums[:])
                return

            for idx in range(i,len(nums)):

                nums[i], nums[idx] = nums[idx], nums[i]
                solve(i+1, nums,res)
                nums[i],nums[idx]= nums[idx],nums[i]

        res = []
        solve(0,nums, res)
        return res   