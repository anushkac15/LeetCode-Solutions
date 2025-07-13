class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def solve(i, res, nums):

            if i>= len(nums):
                res.append(nums[:])
                return

            seen = set()

            for idx in range(i, len(nums)):
                if nums[idx] in seen:
                    continue

                seen.add(nums[idx])

                nums[i], nums[idx] = nums[idx], nums[i]
                solve(i+1,res, nums)
                nums[i], nums[idx] = nums[idx], nums[i]

        res = []
        solve(0, res, nums)
        return res