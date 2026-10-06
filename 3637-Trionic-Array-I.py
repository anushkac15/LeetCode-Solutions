class Solution:
    def isTrionic(self, nums: List[int]) -> bool:

        i = 1
        n = len(nums) - 1

        while i <= n and nums[i - 1] < nums[i]:
            i += 1

        if i == 1:
            return False

        start = i
        while i <= n and nums[i - 1] > nums[i]:
            i += 1

        if i == start:
            return False

        start = i
        while i <= n and nums[i - 1] < nums[i]:
            i += 1

        if i == start:
            return False

        return i == n + 1
