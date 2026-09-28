class Solution:
    def maxDepth(self, s: str) -> int:

        ans, openBrackets = 0, 0

        for c in s:
            if c == "(":
                openBrackets += 1
            elif c == ")":
                openBrackets -= 1

            ans = max(ans, openBrackets)

        return ans
