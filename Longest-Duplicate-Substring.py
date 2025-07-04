class Solution:
    def longestDupSubstring(self, s: str) -> str:

        j=1
        res =""

        for i in range(len(s)):

            window = s[i:i+j]
            look = s[i+1:]

            while window in look:
                res = window
                j+=1
                window = s[i:i+j]

        return res
        