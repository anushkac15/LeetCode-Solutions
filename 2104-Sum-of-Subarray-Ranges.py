class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        NSL = [0] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            NSL[i] = stack[-1] if stack else -1
            stack.append(i)

        NSR = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            NSR[i] = stack[-1] if stack else n
            stack.append(i)

        NGL = [0] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            NGL[i] = stack[-1] if stack else -1
            stack.append(i)

        NGR = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            NGR[i] = stack[-1] if stack else n
            stack.append(i)

        total_sum = 0
        for i in range(n):
            max_contribution = nums[i] * (i - NGL[i]) * (NGR[i] - i)
            min_contribution = nums[i] * (i - NSL[i]) * (NSR[i] - i)
            total_sum += (max_contribution - min_contribution)

        return total_sum
