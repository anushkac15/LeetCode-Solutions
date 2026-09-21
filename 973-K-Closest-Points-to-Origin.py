class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:

        dist = []

        for i in range(len(points)):

            d = points[i][0] ** 2 + points[i][1] ** 2
            dist.append((d, points[i]))

        heapq.heapify(dist)
        res = []

        for i in range(k):

            d, point = heapq.heappop(dist)
            res.append(point)

        return res
