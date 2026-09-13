class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def solve(i, target, res, temp):

            if target==0:
                res.append(temp[:])
                return res

            if i==len(candidates) or target<0:
                return 0

            if candidates[i] <= target:
                temp.append(candidates[i])
                solve(i, target-candidates[i], res, temp)
                temp.pop()

            solve(i+1, target, res, temp)

        res = []
        solve(0, target, res, [])
        return res

