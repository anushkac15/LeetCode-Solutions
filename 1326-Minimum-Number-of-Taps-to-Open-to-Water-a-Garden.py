class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        startEnd = [0]*(n+1)

        for i in range(len(ranges)):

            left = max(0, i-ranges[i])
            right = min(i+ranges[i], len(ranges))

            startEnd[left] = max(startEnd[left], right)

        maxEnd =0
        currEnd =0
        taps=0

        for i in range(len(ranges)):

            if i>maxEnd :
                return -1

            if i>currEnd:
                taps+=1
                currEnd = maxEnd

            maxEnd = max(maxEnd, startEnd[i])

        return taps