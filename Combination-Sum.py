class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def solve(i, res, temp, target):
            if target==0:
                res.append(temp[:])
                return

            for idx in range(i,len(candidates)):

                if candidates[idx]>target:
                    break

                temp.append(candidates[idx])
                solve(idx, res, temp, target-candidates[idx])
                temp.pop()
        candidates.sort()
        res =[]
        solve(0, res, [], target)
        return res