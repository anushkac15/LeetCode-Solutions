class Solution:
    def partitionLabels(self, s: str) -> list[int]:

        size = 0
        end = 0
        lastIndex = {}
        res = []

        for i, c in enumerate(s):
            lastIndex[c] = i

        for i, c in enumerate(s):

            size += 1

            end = max(end, lastIndex[c])

            if i == end:
                res.append(size)
                size = 0

        return res
