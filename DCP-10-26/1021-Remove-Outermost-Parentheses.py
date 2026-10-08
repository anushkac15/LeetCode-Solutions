class Solution:
    def removeOuterParentheses(self, s: str) -> str:

        res = ""
        level = 0

        for ch in s:

            if ch == ")":
                level -= 1
            if level > 0:
                res += ch
            if ch == "(":
                level += 1

        return res
