class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        q = deque()
        l = 0
        res = []

        for r in range(len(nums)):

            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            if q[0] < l:
                q.popleft()

            if r - l + 1 >= k:
                res.append(nums[q[0]])
                l += 1

        return res
