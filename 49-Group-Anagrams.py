class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = defaultdict(list)

        for s in strs:
            chars = sorted(s)
            key = ' '.join(chars)

            if key not in mp:
                mp[key]: []

            mp[key].append(s)

        return list(mp.values())
        