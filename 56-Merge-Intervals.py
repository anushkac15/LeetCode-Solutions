class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        merged = []
        intervals.sort()

        for i in intervals:

            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1][1] = max(merged[-1][1], i[1])

        return merged
