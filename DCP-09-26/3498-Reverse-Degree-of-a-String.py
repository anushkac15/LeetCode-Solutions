class Solution:
    def reverseDegree(self, s: str) -> int:

        sum = 0

        for i in range(1, len(s) + 1):

            sum += i * (ord("z") - ord(s[i - 1]) + 1)

        return sum
