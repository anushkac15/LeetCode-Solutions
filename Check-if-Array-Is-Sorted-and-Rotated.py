class Solution:
    def check(self, nums: List[int]) -> bool:

        cnt =0
        n = len(nums)

        if(nums[0]<nums[n-1]):
            cnt+=1

        for i in range(0, n-1):
            if(nums[i]>nums[i+1]):
                cnt= cnt+1
        
        return cnt<=1
        

        