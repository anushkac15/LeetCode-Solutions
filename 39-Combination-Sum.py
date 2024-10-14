class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def solve(start:int, temp:List[int], rem:int):
            if rem==0:
                res.append(temp.copy())
                return
            
            if rem<0:
                return 

            if start<len(candidates):
                temp.append(candidates[start])
                solve(start,temp, rem - candidates[start])
                temp.pop()
                solve(start+1, temp, rem)

        temp = []
        solve(0,temp,target)
        return res