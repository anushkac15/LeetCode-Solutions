class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def solve(start: int, k:int,temp:List[int]):

            if k ==0:
                res.append(temp.copy())
                return 
            if start>n:
                return 

            temp.append(start)
            solve(start+1, k-1, temp)
            temp.pop()
            solve(start+1, k, temp)
        
        temp  = []
        solve(1,k, temp)
        return res