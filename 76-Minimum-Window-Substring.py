class Solution:
    def minWindow(self, s: str, t: str) -> str:

        m = len(s)
        n = len(t)

        if m < n:
            return ""

        hashArr = [0] * 128

        for i in range(n):
            hashArr[ord(t[i])] += 1

        l = 0
        r = 0

        ct = 0
        minLen = float('inf')
        sIndex = -1

        while r < m:

            rightChar = s[r]

            if hashArr[ord(rightChar)] > 0:
                ct += 1

            hashArr[ord(rightChar)] -= 1

            while ct == n:

                if r - l + 1 < minLen:
                    minLen = r - l + 1
                    sIndex = l

                leftChar = s[l]

                hashArr[ord(leftChar)] += 1

                if hashArr[ord(leftChar)] > 0:
                    ct -= 1

                l += 1

            r += 1

        if sIndex == -1:
            return ""

        return s[sIndex:sIndex + minLen]