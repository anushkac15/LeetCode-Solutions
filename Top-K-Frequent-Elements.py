class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mp = defaultdict(int)
        
        for n in nums:

            mp[n]+=1

        
        heap = []

        for n, cnt in mp.items():
            heapq.heappush(heap, (-cnt, n))

        res = []

        for _ in range(k):

            res.append(heapq.heappop(heap)[1])

        return res