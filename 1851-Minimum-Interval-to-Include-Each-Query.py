class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()

        minHeap = []
        i =0
        res = {}

        for q in sorted(queries):

            while i<len(intervals) and intervals[i][0] <= q:
                l,r = intervals[i]
                length = r-l+1

                heapq.heappush(minHeap,(length, r))

                i+=1

            while minHeap and minHeap[0][1] <q:
                heapq.heappop(minHeap)

            if minHeap:
                res[q] = minHeap[0][0]
            else:
                res[q]  = -1

        return [res[q] for q in queries]
        