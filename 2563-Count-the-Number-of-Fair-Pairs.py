class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:

        nums.sort()
        n = len(nums)

        def count(target):
            left =0
            right = n-1
            cnt =0
            while left<right:
                if nums[left]+nums[right]<=target:
                    cnt+=(right -left)
                    left+=1

                else:
                    right-=1
            return cnt

        return count(upper) - count(lower-1)

        