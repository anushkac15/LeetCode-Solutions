class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        st = set(nums)
        res = 0

        for n in st:

            if n - 1 not in st:  # this gives the starting of sequence
                len = 1

                while n + 1 in st:
                    n += 1
                    len += 1

                res = max(res, len)

        return res
