class Solution:
    def mincostToHireWorkers(self, quality, wage, k):

        workers = []

        for i in range(len(quality)):
            ratio = wage[i] / quality[i]
            workers.append((ratio, quality[i]))

        workers.sort()

        max_heap = []
        total_quality = 0
        ans = float('inf')

        for ratio, q in workers:

            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                removed = -heapq.heappop(max_heap)
                total_quality -= removed

            if len(max_heap) == k:
                cost = total_quality * ratio
                ans = min(ans, cost)

        return ans