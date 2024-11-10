class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        l =0
        r=0
        zeroes =0
        max_len =0

        for r in range(len(nums)):
            if nums[r] ==0:
                zeroes+=1
            if zeroes>k:
                if nums[l] ==0:
                    zeroes-=1
                l+=1

        return r-l+1

        