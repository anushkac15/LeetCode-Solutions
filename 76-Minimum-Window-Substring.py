class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        l = 0
        r = 0
        cnt = len(t)
        mp = defaultdict(int)
        minlen = float("inf")
        minStart = 0

        for ch in t:
            mp[ch] += 1

        while r < len(s):

            if mp[s[r]] > 0:
                cnt -= 1

            mp[s[r]] -= 1

            while cnt == 0:

                if minlen > (r - l + 1):
                    minlen = min(minlen, r - l + 1)
                    minStart = l

                mp[s[l]] += 1

                if mp[s[l]] > 0:
                    cnt += 1

                l += 1

            r += 1

        return "" if minlen == float("inf") else s[minStart : minlen + minStart]
