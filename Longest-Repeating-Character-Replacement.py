class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l =0
        dict = defaultdict(int)
        maxFreq =0
        maxi =0

        for r in range(len(s)):
            dict[s[r]]+=1
            maxFreq=max(maxFreq, dict[s[r]])

            while (r-l+1) -maxFreq >k:
                dict[s[l]]-=1
                l+=1
            maxi = max(maxi, r-l+1)

        return maxi