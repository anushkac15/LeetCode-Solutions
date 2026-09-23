class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
