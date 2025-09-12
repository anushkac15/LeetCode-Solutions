class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mp = {}

        for i in range(len(s)):

            if s[i] in mp:

                if mp[s[i]]!=t[i]:
                    return False

            elif t[i] in mp.values():
                return False

            mp[s[i]] = t[i]

        return True