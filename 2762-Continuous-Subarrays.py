class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        right = left = 0
        window_len = total = 0

        cur_min = cur_max = nums[right]

        for right in range(len(nums)):
            cur_min = min(cur_min, nums[right])
            cur_max = max(cur_max, nums[right])

            if cur_max - cur_min > 2:
                window_len = right - left
                total += window_len * (window_len + 1) // 2

                left = right
                cur_min = cur_max = nums[right]

                while left > 0 and abs(nums[right] - nums[left - 1]) <= 2:
                    left -= 1
                    cur_min = min(cur_min, nums[left])
                    cur_max = max(cur_max, nums[left])

                if left < right:
                    window_len = right - left
                    total -= window_len * (window_len + 1) // 2

        window_len = right - left + 1
        total += window_len * (window_len + 1) // 2

        return total