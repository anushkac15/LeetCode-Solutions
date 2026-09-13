class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def solve(i, res, temp):

            res.append(temp[:])

            for idx in range(i, len(nums)):
                if idx>i and nums[idx] == nums[idx-1]:
                    continue

                temp.append(nums[idx])
                solve(idx+1, res, temp)
                temp.pop()

        res =[]
        nums.sort()
        solve(0, res, [])
        return res
        