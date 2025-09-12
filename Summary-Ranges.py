class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        st = set(nums)
        res = []

        for n in nums:
            if n-1 not in st:

                start = n
                end = n

                while end+1 in st:
                    end+=1

                if start ==end:
                    res.append(f"{n}")
                else:
                    res.append(f"{start}->{end}")

        return res      