class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        mp ={}

        words = s.split()

        if len(words)!= len(pattern):
            return False

        for i in range(len(pattern)):

            if words[i] in mp:
                if mp[words[i]] != pattern[i]:
                    return False

            elif pattern[i] in mp.values():
                return False

            mp[words[i]] = pattern[i]

        return True