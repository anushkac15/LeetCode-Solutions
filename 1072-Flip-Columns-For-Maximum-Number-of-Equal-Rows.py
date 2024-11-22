class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        mp = defaultdict(int)

        for row in matrix:
            rowKaNature = ""
            firstVal = row[0]
            for col in range(n):
                rowKaNature += "S" if row[col] == firstVal else "B"
            mp[rowKaNature] += 1

        maxRows = 0
        for count in mp.values():
            maxRows = max(maxRows, count)

        return maxRows
