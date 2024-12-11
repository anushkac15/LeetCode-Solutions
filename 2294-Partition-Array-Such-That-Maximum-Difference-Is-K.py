class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        array = 0
        left =0

        for right in range(len(nums)):
            if nums[right]-nums[left] > k:
                array+=1
                left = right
        return array+1

        