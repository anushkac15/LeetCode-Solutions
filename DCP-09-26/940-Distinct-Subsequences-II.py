class Solution:
    def distinctSubseqII(self, s):
        n = len(s)
        MOD = 10**9 + 7

        countEndWith = [0] * 26
        total = 0

        for i in range(n):
            idx = ord(s[i]) - ord('a')

            cur = (1 + total - countEndWith[idx] + MOD) % MOD

            total = (total + cur) % MOD

            countEndWith[idx] = (countEndWith[idx] + cur) % MOD

        return total