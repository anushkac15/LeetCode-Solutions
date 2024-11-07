class Solution:
    def canJump(self, nums: List[int]) -> bool:
        howFar =0
        for num in nums:
            if howFar<0:
                return False
            elif num>howFar:
                howFar =num
            howFar-=1
        return True