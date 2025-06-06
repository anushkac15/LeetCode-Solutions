class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x : x[1])
        ans = 0
        prev_end = float('-inf')

        for i in intervals:
            if prev_end > i[0]:
                ans+=1
            else:
                prev_end = i[1]

        return ans
        