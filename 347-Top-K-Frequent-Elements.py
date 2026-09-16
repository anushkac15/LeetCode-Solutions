class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

        mp = defaultdict(int)

        res = []

        for n in nums:
            mp[n] += 1

        heap = []

        for n, cnt in mp.items():
            heapq.heappush(heap, (-cnt, n))

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
