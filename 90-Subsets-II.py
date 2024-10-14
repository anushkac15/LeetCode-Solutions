class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def solve(start:int, temp:List[int]):
            res.append(temp.copy())

            for i in range(start,len(nums)):

                if i>start and nums[i]==nums[i-1]:
                    continue

                temp.append(nums[i])
                solve(i+1, temp)
                temp.pop()
        temp = []
        solve(0,temp)
        return res
        