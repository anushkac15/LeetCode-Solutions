class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        mp ={}

        for i in range(len(nums)):
            val = nums[i]

            if val in mp and i- mp[val] <=k:
                return True

            mp[val] = i

        return False

            
        