class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        seen = set()

        for n in nums:
            if n in seen:
                return n

            seen.add(n)

        return -1
