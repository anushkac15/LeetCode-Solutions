class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        open = close = 0

        for ch in s:

            if ch == "(":
                open += 1

            elif ch == ")":
                if open > 0:
                    open -= 1
                else:
                    close += 1

        return open + close
