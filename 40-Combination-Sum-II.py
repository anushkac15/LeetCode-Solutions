class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        def solve(start:int, temp:List[int], rem:int):
            if rem ==0:
                res.append(temp.copy())
                return
            
            if rem<0:
                return 

            for i in range(start, len(candidates)):

                if i>start and candidates[i] == candidates[i-1]:
                    continue
                
                temp.append(candidates[i])
                solve(i+1, temp, rem-candidates[i])
                temp.pop()

        temp = []
        solve(0,temp,target)
        return res

