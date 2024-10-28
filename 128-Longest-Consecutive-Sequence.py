class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
        st = set(nums)
        ConseCnt= 0

        for num in st:

            if num-1 not in st:
                
                curr = num
                currCnt =1

                while curr+1 in st:
                    curr +=1
                    currCnt+=1

                ConseCnt = max(currCnt,ConseCnt)

        return ConseCnt