class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        max_heap = [-pile for pile in piles]
        heapq.heapify(max_heap)

        while k > 0:
            largest = -heapq.heappop(max_heap)
            heapq.heappush(max_heap, -(largest - largest // 2))
            k -= 1

        return -sum(max_heap)