class Solution:
    def sortVowels(self, s: str) -> str:
        v = "aeiouAEIOU"
        x = sorted([c for c in s if c in v])
        j = 0
        r = []
        for c in s:
            if c in v:
                r.append(x[j])
                j += 1
            else:
                r.append(c)
        return "".join(r)
