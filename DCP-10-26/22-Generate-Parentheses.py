class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        def solve(open, close, res, temp):

            if open == n and close == n:
                res.append(temp)

            if open < n:
                solve(open + 1, close, res, temp + "(")
            if close < open:
                solve(open, close + 1, res, temp + ")")

        res = []
        solve(0, 0, res, "")
        return res
