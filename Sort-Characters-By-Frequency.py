class Solution:
    def frequencySort(self, s: str) -> str:

        mp = defaultdict(int)

        for c in s:
            mp[c]+=1

        key = sorted(mp, key = mp.get, reverse=True)

        res =""

        for i in range(len(key)):
            res+= key[i]*mp[key[i]]

        return res

        