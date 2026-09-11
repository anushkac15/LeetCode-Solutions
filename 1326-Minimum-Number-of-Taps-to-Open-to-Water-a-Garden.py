class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:

        startEnd = [0]*(n+1)

        for i in range(len(ranges)):

            left = max(0, i-ranges[i])
            right = min(i+ranges[i], n)

            startEnd[left] = max(startEnd[left], right)

        maxInd =0
        currInd =0
        taps =0

        for i in range(len(ranges)):

            if i>maxInd :
                return -1

            if i>currInd:
                currInd = maxInd
                taps +=1

            maxInd = max(maxInd, startEnd[i])

        return taps
                
        