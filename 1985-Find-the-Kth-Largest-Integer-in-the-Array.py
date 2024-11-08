class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        s = [int(num) for num in nums]

        heap = s[:k]
        heapq.heapify(heap)

        for num in s[k:]:
            if num>heap[0]:
                heapq.heappush(heap,num)
                heapq.heappop(heap)

        return str(heap[0])