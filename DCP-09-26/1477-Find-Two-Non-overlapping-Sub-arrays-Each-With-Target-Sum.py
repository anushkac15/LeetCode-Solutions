class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        inf = float("inf")
        l = 0
        ans = inf
        dp = [inf] * len(arr)
        curr = 0

        for r in range(len(arr)):

            curr += arr[r]

            while curr > target:
                curr -= arr[l]
                l += 1

            # 1. Carry the best previous subarray
            if r > 0:
                dp[r] = dp[r - 1]

            if curr == target:

                currLength = r - l + 1

                # 2. Combine with previous non-overlapping subarray
                ans = min(ans, currLength + dp[l - 1])

                # 3. Current subarray may be the best one
                dp[r] = min(dp[r], currLength)

        return -1 if ans == inf else ans
