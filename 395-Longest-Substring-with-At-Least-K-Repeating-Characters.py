class Solution:
    def longestSubstring(self, s: str, k: int) -> int:

        ans = 0

        for unique in range(1, 27):

            freq = defaultdict(int)

            l = 0
            r = 0
            cnt = 0
            good = 0

            while r < len(s):

                n = s[r]

                if freq[n] == 0:
                    cnt += 1

                freq[n] += 1

                if freq[n] == k:
                    good += 1

                while cnt > unique:

                    if freq[s[l]] == k:
                        good -= 1

                    freq[s[l]] -= 1

                    if freq[s[l]] == 0:
                        cnt -= 1

                    l += 1

                if cnt == unique and good == unique:
                    ans = max(ans, r - l + 1)

                r += 1

        return ans