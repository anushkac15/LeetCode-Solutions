class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def solve(i, res, temp):

            if i== len(nums):
                res.append(temp[:])
                return 

            temp.append(nums[i])
            solve(i+1, res, temp)

            temp.pop()
            solve(i+1, res, temp)

        res = []
        solve(0, res, [])
        return res
        