class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-val for val in gifts]
        heapq.heapify(heap)

        while k>0:
            largest = -heapq.heappop(heap)

            heapq.heappush(heap, -math.floor(math.sqrt(largest)))
            k-=1

        return -sum(heap)


        