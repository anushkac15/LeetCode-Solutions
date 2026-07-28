class Solution:
    def smallestPalindrome(self, s: str) -> str:

        mid = len(s)//2

        left = sorted(s[:mid])

        ans = ""

        for ch in left:
            ans+=ch

        if len(s)%2==1:
            ans+=s[mid]

        for i in range(len(left)-1,-1,-1):
            ans+=left[i]

        return ans

