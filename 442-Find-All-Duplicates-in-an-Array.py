class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicates = []

        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)

        return duplicates
        