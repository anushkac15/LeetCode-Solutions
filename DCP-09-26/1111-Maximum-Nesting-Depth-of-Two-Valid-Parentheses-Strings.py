class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:

        depth = 0
        res = [-1] * len(seq)

        for i in range(len(seq)):
            if seq[i] == "(":
                depth += 1
                if depth % 2 == 0:
                    res[i] = 0
                else:
                    res[i] = 1
            else:
                if depth % 2 == 0:
                    res[i] = 0
                else:
                    res[i] = 1

                depth -= 1

        return res
