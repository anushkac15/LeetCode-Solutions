class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        squareCnt =0
        st = set(nums)

        for num in nums:
            curr_cnt =0
            curr = num

            while curr in st:
                curr_cnt+=1

                if curr*curr >10**5:
                    break
                    
                curr= curr*curr

            squareCnt = max(squareCnt,curr_cnt)

        if squareCnt>1:
            return squareCnt
        else:
            return -1 