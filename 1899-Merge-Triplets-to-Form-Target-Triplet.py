class Solution:
    def mergeTriplets(self, triplets: list[list[int]], target: list[int]) -> bool:
        a = b = c = False
        for t in triplets:
            if t[0] <= target[0] and t[1] <= target[1] and t[2] <= target[2]:
                a = a or t[0] == target[0]
                b = b or t[1] == target[1]
                c = c or t[2] == target[2]
        return a and b and c
