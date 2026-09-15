class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        last = -1
        cnt = 0

        def isPal(s):
            return s == s[::-1]

        for j in range(len(s)):
            for i in range(j + 1):

                temp = s[i : j + 1]

                if i > last and isPal(temp) and len(temp) >= k:
                    cnt += 1
                    last = j
        return cnt
