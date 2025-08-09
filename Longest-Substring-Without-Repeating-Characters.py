class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l=0
        r=0
        maxi =0
        st = set()

        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l+=1
            
            st.add(s[r])
            maxi = max(maxi, r-l+1)

        return maxi