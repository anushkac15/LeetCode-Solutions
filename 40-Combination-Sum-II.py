class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def solve(i, res, temp, target):

            if target == 0:
                res.append(temp[:])
                return res

            if i==len(candidates) or target<0:
                return 0

            for idx in range(i, len(candidates)):

                if idx> i and candidates[idx] == candidates[idx-1]:
                    continue


                temp.append(candidates[idx])
                solve(idx+1, res, temp, target-candidates[idx])
                temp.pop()

        res = []
        candidates.sort()
        solve(0, res, [], target)
        return res
