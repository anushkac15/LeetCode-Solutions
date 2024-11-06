class Solution:
    def canSortArray(self, nums):
        numOfSetBits = bin(nums[0]).count('1')
        maxOfSegment = nums[0]
        minOfSegment = nums[0]

        maxOfPrevSegment = float('-inf')

        for i in range(1, len(nums)):
            if bin(nums[i]).count('1') == numOfSetBits: 
                maxOfSegment = max(maxOfSegment, nums[i])  
                minOfSegment = min(minOfSegment, nums[i]) 
            else: 
                if minOfSegment < maxOfPrevSegment:  
                    return False
                
                maxOfPrevSegment = maxOfSegment

                maxOfSegment = nums[i]
                minOfSegment = nums[i]
                numOfSetBits = bin(nums[i]).count('1')

        if minOfSegment < maxOfPrevSegment:
            return False

        return True
