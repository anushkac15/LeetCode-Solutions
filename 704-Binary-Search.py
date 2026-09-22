class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if target > nums[mid]:
                l  = mid+1
            elif target < nums[mid]:
                r = mid-1

            else:
                return mid

        return -1
