class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        mp =defaultdict(int)
        cnt =0

        for i in range(len(nums)):
            mp[nums[i]]+=1

            if mp[nums[i]]<=2:
                nums[cnt] = nums[i]

                cnt+=1

        return cnt
        