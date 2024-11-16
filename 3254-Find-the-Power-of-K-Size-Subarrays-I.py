class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:

        res = [-1] * (len(nums)-k+1)
        consec_cnt =0

        for i in range(len(nums)):
            if nums[i] == nums[i-1] +1:
                consec_cnt +=1
            else:
                consec_cnt =1
            
            if consec_cnt >=k:
                res[i-k+1] = nums[i]

        return res
        
