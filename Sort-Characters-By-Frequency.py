class Solution:
    def frequencySort(self, s: str) -> str:

        mp = defaultdict(int)

        for c in s:
            mp[c]+=1

        heap = []

        for char, cnt in mp.items():
            heapq.heappush(heap, (-cnt, char))

        res = ""

        while heap:
            cnt, char = heapq.heappop(heap)
            res+= (-cnt)*char

        return res