class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:

        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i

            last[ch] = i

        candidates = []

        for ch in first:

            l = first[ch]
            r = last[ch]

            valid = True
            i = l

            while i <= r:

                ch2 = s[i]

                # Complete range of ch2 starts before ours
                if first[ch2] < l:
                    valid = False
                    break

                # Expand if necessary
                r = max(r, last[ch2])

                i += 1

            if valid:
                sub = s[l:r+1]

                candidates.append(
                    (len(sub), l, r, sub)
                )

        # Smaller substrings first
        candidates.sort()

        ans = []
        used = []

        for length, l, r, sub in candidates:

            overlap = False

            for left, right in used:

                if not (r < left or l > right):
                    overlap = True
                    break

            if not overlap:
                ans.append(sub)
                used.append((l, r))

        return ans