class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        left = right = 0

        for ch in s:
            if ch == "(":
                left += 1
            elif ch == ")":
                if left > 0:
                    left -= 1
                else:
                    right += 1

        res = set()

        def solve(i, leftCnt, rightCnt, bal, temp):

            if leftCnt < 0 or rightCnt < 0:
                return
            if bal < 0:
                return

            if i == len(s):

                if leftCnt == 0 and rightCnt == 0 and bal == 0:
                    res.add(temp)
                return

            # skip :

            if s[i] == "(" and leftCnt > 0:
                solve(i + 1, leftCnt - 1, rightCnt, bal, temp)
            elif s[i] == ")" and rightCnt > 0:
                solve(i + 1, leftCnt, rightCnt - 1, bal, temp)

            # take :

            if s[i] == "(":

                solve(i + 1, leftCnt, rightCnt, bal + 1, temp + s[i])
            elif s[i] == ")":
                solve(i + 1, leftCnt, rightCnt, bal - 1, temp + s[i])

            else:
                solve(i + 1, leftCnt, rightCnt, bal, temp + s[i])

        solve(0, left, right, 0, "")
        return list(res)
