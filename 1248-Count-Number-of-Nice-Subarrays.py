class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:

        l = 0
        odd = 0
        left_count = 0
        ans = 0

        for r in range(len(nums)):

            if nums[r] % 2 == 1:
                odd += 1

            if odd == k:

                left_count = 0

                while nums[l] % 2 == 0:
                    l += 1
                    left_count += 1

                l += 1
                odd -= 1
                left_count += 1

            if odd == k - 1:
                ans += left_count

        return ans
