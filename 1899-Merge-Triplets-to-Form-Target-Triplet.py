class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:

        t1 = False
        t2 = False
        t3 = False

        for t in triplets:

            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:

                t1 = t1 or (t[0] == target[0])
                t2 = t2 or (t[1] == target[1])
                t3 = t3 or (t[2] == target[2])

        return t1 and t2 and t3
