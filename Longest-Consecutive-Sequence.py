class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st = set(nums)
        res = 0

        for n in st:

            if n-1 not in st:
                len = 1

                while n+1 in st:
                    n = n+1
                    len+=1

                res = max(res,len)        

        return res