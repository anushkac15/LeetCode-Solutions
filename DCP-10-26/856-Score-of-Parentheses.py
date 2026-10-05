class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        depth = 0
        ans = 0

        for i in range(len(s)):
            if s[i] == "(":
                depth += 1
            else:
                depth -= 1

                if s[i - 1] == "(":
                    ans += 2**depth

        return ans
