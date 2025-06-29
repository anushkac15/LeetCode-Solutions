class Solution:
    def countSubstrings(self, s: str) -> int:

        def count(i, j):

            cnt =0

            while i >=0 and j< len(s) and s[i] == s[j]:
                cnt+=1
                i-=1
                j+=1

            return cnt


        res =0
        for i in range(len(s)):
            res+=count(i,i)
            res+=count(i,i+1)

        return res       