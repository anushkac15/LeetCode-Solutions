class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def solve(openP, closeP, res, temp):

            if openP + closeP == 2*n:
                res.append(temp)

            if openP<n:
                solve(openP+1, closeP, res, temp+"(")
            if closeP < openP:
                solve(openP, closeP+1, res, temp+")")

        res = []
        solve(0, 0, res, "")
        return res

        