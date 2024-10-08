class Solution:
    def minSwaps(self, s: str) -> int:
        ans =0
        for ch in s:
            if ch == '[':
                ans+=1
            elif ans>0:
                ans-=1
        return (ans+1)//2
        