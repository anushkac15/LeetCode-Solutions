class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mp = defaultdict(list)

        for s in strs:

            mp[''.join(sorted(s))].append(s)

        return list(mp.values())
        