class Solution:
    def countHomogenous(self, s: str) -> int:
        ans =0
        cnt = 0
        m = (10**9)+7

        for i in range(len(s)):
            if i==0 or s[i]==s[i-1]:
                cnt+=1
            else:
                cnt = 1

            ans+=cnt

        return ans %m


        