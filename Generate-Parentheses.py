class Solution:


        
    def generateParenthesis(self, n: int) -> List[str]:

        res =[]
        temp = \\

        def solve(openP, closeP, n, res, temp):

            if (openP+closeP == n*2):
                res.append(temp)
                return
            
            if(openP<n):
                solve(openP+1, closeP, n, res, temp+\(\)

            if(closeP<openP):
                solve(openP, closeP+1, n, res, temp+\)\)

        solve(0, 0, n, res, temp)
        return res


        